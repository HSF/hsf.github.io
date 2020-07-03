---
title: Differentiable Computing
author: Nathan Simpson
layout: plain
---

## Why make things differentiable?

When we write a program to do some physics, that program will likely have some free parameters. These could be as simple as the position of a cut, or as complicated as the parameters of a neural network. In either case, we want these parameters to be optimized such that we get the best possible result, whatever that may be. In the case of a HEP analysis, for instance, this could correspond to having the highest sensitivity to new phenomena. 

So, how exactly do we get there?

It turns out that we can do exactly what we do when we train a neural network -- update the parameters using gradient descent. This is where the _differentiable_ part
comes in: we can only optimize with respect to an objective that has a tractable gradient, since that's how we tell our parameters which direction to go in order to improve. Since there are usually many steps between the use of the parameters and the program output, it follows that every operation in-between them must also be differentiable. This lets us track exactly how changing the parameters affects the final result, and allows us to optimize our physics calculations _end-to-end_.

## How do we do it?
We can make this possible if we keep track of the derivatives of each step (i.e. line of code) of the program with respect to its inputs. While that may sound like a harsh requirement, this is made pretty simple thanks to the magic of automatic differentiation. Of course, this is not without its caveats, as not all lines of code are necessarily differentiable. In particular, common operations in HEP like binning a set of data or making a cut do not vary smoothly with respect to their inputs. That’s why there’s an ongoing effort within this activity to provide drop-in differentiable replacements for common operations, as well as more sophisticated differentiable ‘blocks’, such as statistical model building using [pyhf](https://github.com/scikit-hep/pyhf), or inference using the profile likelihood as a test statistic.

## How do I get involved?

Efforts in this direction are currently pivoting around the [gradHEP](https://gradhep.github.io) organisation on GitHub. 

To express general interest:
- [Say hi on Gitter](https://gitter.im/gradhep/community?source=orgpage)
- For big-picture thoughts or specific questions, [comment on existing issues, or raise a new issue on our ‘center’ repo](https://github.com/gradhep/center/issues) 

For those that have CERN accounts (or those that can make a lightweight account) and want to be more involved, we have a [Mattermost](https://mattermost.web.cern.ch/signup_user_complete/?id=zf7w5rb1miy85xsfjqm68q9hwr), which is the main way we communicate amongst ourselves.

We're also going to start having monthly update meetings, which you can find the agendas for on the [differentiable computing Indico category](https://indico.cern.ch/category/12615/) (time slot TBD).

This is a new & emerging effort — everyone is very much welcome to join! :)

### Contact information

For any further queries, please contact the activity organisers (Lukas Heinrich & Nathan Simpson):

<lukas.heinrich@cern.ch>, <n.s@cern.ch>
