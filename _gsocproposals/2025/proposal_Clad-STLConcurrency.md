---
title: Enable automatic differentiation of C++ STL concurrency primitives in Clad
layout: gsoc_proposal
project: Clad
year: 2025
difficulty: medium
duration: 350
mentor_avail: June-October
organization:
  - CompRes
project_mentors:
  - name: "Vassil Vassilev"
    email: "vvasilev@cern.ch"
  - name: "David Lange"
    email: "david.lange@cern.ch"
---

## Description

Clad is an automatic differentiation (AD) clang plugin for C++. Given a C++ source code of a mathematical function, it can automatically generate C++ code for computing derivatives of the function. This project focuses on enabling automatic differentiation of codes that utilise C++ concurrency features such as `std::thread`, `std::mutex`, atomic operations and more. This will allow users to fully utilize their CPU resources.

## Expected Results

* Explore C++ concurrency primitives and prepare a report detailing the associated challenges involved and the features that can be feasibly supported within the given timeframe.
* Add concurrency primitives support in Clad’s forward-mode automatic differentiation.
* Add concurrency primitives support in Clad’s reverse-mode automatic differentiation.
* Add proper tests and documentation.
* Present the work at the relevant meetings and conferences.

An example demonstrating the use of differentiation of codes utilizing parallelization primitives:

```
#include <cmath>
#include <iostream>
#include <mutex>
#include <numeric>
#include <thread>
#include <vector>
#include "clad/Differentiator/Differentiator.h"

using VectorD = std::vector<double>;
using MatrixD = std::vector<VectorD>;

std::mutex m;

VectorD operator*(const VectorD &l, const VectorD &r) {
  VectorD v(l.size());
  for (std::size_t i = 0; i < l.size(); ++i)
    v[i] = l[i] * r[i];
  return v;
}

double dot(const VectorD &v1, const VectorD &v2) {
  VectorD v = v1 * v2;
  return std::accumulate(v.begin(), v.end(), 0.0);
}

double activation_fn(double z) { return 1 / (1 + std::exp(-z)); }

double compute_loss(double y, double y_estimate) {
  return -(y * std::log(y_estimate) + (1 - y) * std::log(1 - y_estimate));
}

void compute_and_add_loss(VectorD x, double y, const VectorD &weights, double b,
                          double &loss) {
  double z = dot(x, weights) + b;
  double y_estimate = activation_fn(z);
  std::lock_guard<std::mutex> guard(m);
  loss += compute_loss(y, y_estimate);
}

/// Compute total loss associated with a single neural neural-network.
/// y_estimate = activation_fn(dot(X[i], weights) + b)
/// Loss of a training data point = - (y_actual * std::log(y_estimate) + (1 - y_actual) * std::log(1 - y_estimate))
/// total loss: summation of loss for all the data points
double compute_total_loss(const MatrixD &X, const VectorD &Y,
                          const VectorD &weights, double b) {
  double loss = 0;
  const std::size_t num_of_threads = std::thread::hardware_concurrency();
  std::vector<std::thread> threads(num_of_threads);
  int thread_id = 0;
  for (std::size_t i = 0; i < X.size(); ++i) {
    if (threads[thread_id].joinable())
      threads[thread_id].join();
    threads[thread_id] =
        std::thread(compute_and_add_loss, std::cref(X[i]), Y[i],
                    std::cref(weights), b, std::ref(loss));
    thread_id = (thread_id + 1) % num_of_threads;
  }
  for (std::size_t i = 0; i < num_of_threads; ++i) {
    if (threads[i].joinable())
      threads[i].join();
  }

  return loss;
}

int main() {
  auto loss_grad = clad::gradient(compute_total_loss);
  // Fill the values as required!
  MatrixD X;
  VectorD Y;
  VectorD weights;
  double b;

  // derivatives
  // Zero the derivative variables and make them of the same dimension as the
  // corresponding primal values.
  MatrixD d_X;
  VectorD d_Y;
  VectorD d_weights;
  double d_b = 0;

  loss_grad.execute(X, Y, weights, b, &d_X, &d_Y, &d_weights, &d_b);

  std::cout << "dLossFn/dW[2]: " << d_weights[2] << "\n"; // Partial derivative of the loss function w.r.t weight[2]
  std::cout << "dLossFn/db: " << d_b << "\n"; // Partial derivative of the loss function w.r.t b
}
```

## Requirements

* Automatic differentiation
* Parallel programming
* Reasonable expertise in C++ programming


## Links
* [Repo](https://github.com/vgvassilev/clad)
