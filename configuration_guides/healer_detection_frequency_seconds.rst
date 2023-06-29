.. _healer_detection_frequency_seconds:

**********************************
Healer Detection Frequency Seconds
**********************************

The ``healerDetectionFrequencySeconds`` flag is used for defining the threshold for creating a log recording a slow statement. The log includes information about the log memory, CPU and GPU.

* **Data type** - size_t
* **Default value** - ``60*60*24``
* **Allowed values** - 1-4000000000

For related flags, see :ref:`is_healer_on`.