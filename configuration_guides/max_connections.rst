:orphan:

.. _max_connections:

********************************
MAX CONNECTIONS
********************************

The ``maxConnections`` parameter is optional and sets the maximum number of connections allowed per Worker. Once a Worker reaches its maximum capacity, any new connections are directed to other available Workers.

* **Data type** - size_t
* **Default value** - ``1000``
* **Allowed values** - ``1-∞``

