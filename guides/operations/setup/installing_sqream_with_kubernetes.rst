.. _installing_sqream_with_kubernetes:

*********************************************
Installing SQream with Kubernetes
*********************************************
The purpose of this document is to describe how to prepare the environment and install SQream software via a Kubernetes also known as k8s  package.

Kubernetes, or k8s, is an open source platform that automates Linux container operations.

Kubernetes is a portable, extensible, open-source platform for managing containerized workloads and services, that facilitates both declarative configuration and automation.

Kubernetes is an open-source container orchestration platform that enables the operation of an elastic web server framework for cloud applications. Kubernetes can support data center outsourcing to public cloud service providers or can be used for web hosting at scale.

K8s (Kubernetes) is used in SQream as an orchestration and recovery solution.

The minimal installation when using k8s is 3 servers

A system is considered a cluster when it consists of at least 2 GPU nodes and 1 slim server to act as 

Quorum manager.

 2 servers with GPU and 1 without, From the K8s point of view all 3 servers are set as master.   

Each server should have ip in the management network, in addition, we require another ip from the same subnet to act as floating ip
