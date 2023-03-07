.. _current_method_flag_types:

**************************
System Operation 
**************************

When configuring how your system operates, you may choose to configure your entire cluster; meaning how all clients operate, or you may choose to configure only how the system works for a specific session. Any configurations made to the entire cluster are persistant, meaning that any alteration will continue to be valid for the duration of the session and also after the session is terminated. Persistant configurations are valid after downtime and restart.

SQream uses three flag types, **Cluster**, **Worker**, and **Regular**. Each of these flag types is associated with one of three hierarchical configuration levels described earlier, making it easier to configure your system.

The highest level in the hierarchy is Cluster, which lets you set configurations across all workers in a given cluster. Modifying cluster values is **persistent**, meaning that any configurations you set are retained after shutting down your system. Configurations set at the Cluster level take the highest priority and override settings made on the Regular and Worker level. This is known as **cluster-based configuration**. Note that Cluster-based configuration lets you modify Cluster *and* Regular flag types. An example of a Cluster flag is **persisting your cache directory.**

The second level is Worker, which lets you configure individual workers. Modifying Worker values are also **persistent**. This is known as **worker-based configuration**. Some examples of Worker flags includes **setting total device memory usage** and **setting metadata server connection port**.

The lowest level is Regular, which means that modifying values of Regular flags affects only your current session and are not persistent. This means that they are automatically restored to their default value when the session ends. This is known as **session-based configuration**. Some examples of Regular flags includes **setting your bin size** and **setting CUDA memory**.

To see each flag's default value, see one of the following:

* The **Default Value** column in the :ref:`All Configurations<current_method_all_configurations>` section.

   ::
   
* The flag's individual description page, such as :ref:`Setting CUDA Memory<check_cuda_memory>`.