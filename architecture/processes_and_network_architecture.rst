.. _processes_and_network_architecture:

*************************************
Processes and Network Architecture
*************************************

A SQream DB installation contains several components:

* SQream DB workers (``sqreamd``)
* Metadata daemon (``metadata_server``)
* Load balancer (``server_picker``)


.. 
   processes in sqream:

   metadatad
   server picker
   sqreamd

   monit system

   pacemaker system

   vip

   ui?

   dashboard?

   mention the command line utils here?

   network

   clients connecting, the wlm redirect

   structure of a embedded metadata sqream - simple (do we need to
   mention this in the docs, or is it only for troubleshooting in
   production)

   single node with separate sqreamds - connections between the
   components, server picker, metadata

   multiple nodes

   basic network connections/routes needed

   what's also needed for the pacemaker component
   + how the vip works


