.. _connecting_to_blue:

******************************
Connectivity and Third-Parties
******************************

Users who wish to use the BLUE :ref:`Jobs<performing_basic_blue_operations>` workflow management tool or establish connections to BLUE from their personal applications or tools are required to employ connectors and obtain authentication access tokens, thereby necessitating the creation of dedicated BLUE **Clients** and the generation of these access tokens to enable the use of Jobs, connectors, applications, and tools in question.

Access tokens are essential for establishing secure links to connectors and external platforms. These tokens serve to authenticate, enhancing security by permitting only authorized entities to access the BLUE cluster. Their importance lies in facilitating smooth machine-to-machine communication, enabling thorough auditing and logging, and aligning with modern integration practices.

Before You Begin
----------------

It is essential that you create a BLUE client and associate it with an :ref:`access token<access_tokens>`.


Connectors, Drivers, and Third-Parties
--------------------------------------

BLUE offers seamless integration with third-party tools, BI tools, and analysis tools, ensuring efficient data flow for advanced utilization. Verified compatibility exists with the following tools: 

.. tab:: Connectors and Drivers

    :ref:`JDBC<java_jdbc>`
	
	:ref:`ODBC<odbc>`

    :ref:`Python<pysqream>`

.. tab:: Integration Tools

    :ref:`Apache Airflow<apache_airflow>`
	
    :ref:`DBeaver<dbeaver>`
	
.. tab:: Cloud Natives

    :ref:`Snowflake<snowflake>`



