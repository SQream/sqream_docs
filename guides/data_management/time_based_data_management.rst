.. _time_based_data_management:

**************************
Time based data management
**************************

you have data with a timestamp column

the time stamp matches more or less with when the data is inserted
into sqream/ and when the event that generated that data happened
(e.g. you are inserting new event data every hour or every day)

you want to keep x months or years of data in sqream to query. so
e.g. you delete the oldest month of data every month, by this
timestamp column

you often query over a range on this timestamp, e.g. a specific hour,
day or month.

the sqream chunk/extent system, the insert implementation, and the
free cheap metadata system will all support this kind of process
extremely effectively


