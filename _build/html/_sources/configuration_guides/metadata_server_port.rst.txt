.. _metadata_server_port:

*************************
Setting Port Used for Metadata Server Connection
*************************
The ``metadataServerPort`` flag sets the port used to connect to the metadata server. SQream recommends using port ranges above 1024 because ports below 1024 are usually reserved, although there are no strict limitations. You can use any positive number (1 - 65535) while setting this flag.

The following describes the ``metadataServerPort`` flag:

* **Data type** - uint
* **Default value** - ``3105``