---
project: CERNBOX
title: OCM WebDAV Service
author: Karthik Sundar
photo: blog_authors/KarthikSundar.jpg
date: 22.07.2022
year: 2022
layout: blog_post
logo: cernbox-logo.png
intro: |
  A OCM (Open Cloud Mesh) and WebDAV file sharing service to facilitate sharing of data across the Sciencemesh.
---

## Introduction

I am Karthik Sundar and this blog post is an account of the progress made in the
project in the first 6 weeks. I will be working with Reva team at CERNBOX. So
first of all, **what is Reva?** There are several cloud storage providers and
they have several integrations with applications. However, these applications
are written in such a way that they are specific to their platform. Reva is an
interoperability platform that connects different cloud-storage providers with
different applications, in a uniform manner.

Next, **what is my Project?** I will be working on implementing an OCM/WebDAV
file share service. OCM stands for "OpenCloudMesh" and WebDAV stands for "Web
distributed Authoring and Versioning".OpenCloudMesh provides a common file
access layer using which we can sync files across globally connected servers,
cloud storage, and internal storage. WebDAV is an extension to the HTTP protocol
that provides users the ability to edit and author web content. It makes a web
server act as a file server. It adds headers to allow for concurrent access and
editing of files.

## The Challenges

The first step in this process is the **Invitation Workflow**. The current
invitation workflow however has a security concern. So basically, we send the
user token to reva instance of the remote system. Thus, basically giving access
to all the files in the owner's system.

The next challenge is the WebDAV calls are being routed to an endpoint called
remote.php/webdav. It does not allow the full spectrum of operations provided by
the WebDAV protocol. Thus we have to have a specific webpoint for WebDAV
requests.

## The Progress towards solving the Challenges

Let's first deal with the problem in the Invitation Workflow. We decided to send
the **shareID** of the share instead of the userToken. This would result in the
shareID being stored in the share references DB. However, as of now, there is an
issue with this approach which falls outside the scope of this project. The
WebDAV calls are routed to a function named "webDAVRefStat". We send the
targetURL stored in the referenceDB as a parameter. We get the token from the
targetURL and set it as a header in the gowebdav client. However, the gowebdav
client expects the user token as the header. So that's like the crux of this
issue.

Then moving on to the second challenge, We have a WebDAV implementation provided
by OCIS. We need to have a endpoint called /ocm/webDAV which will basically
serve as a wrapper to webDAV functions. This is currently a work in progress,
which is expected to be completed by the month of August.

If you guys have reached here, it means you have to come to end of the article.
Will see you again in a month. Have a nice day.

---

Reach out to me at: karthiksundar30092002@gmail.com

---
