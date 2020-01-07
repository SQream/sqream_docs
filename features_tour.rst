.. _features_tour:

*****************************
Tour of the SQream DB product
*****************************

Overview
=========

SQream DB is a columnar analytic SQL database management system. SQream DB uses GPUs to load and analyze large amounts of data.

SQL Features
============

Types
-----

bool
tinyint, smallint, int, bigint
real, double
varchar, nvarchar
date
timestamp


Queries
-------

select lists
from
where
tablerefs, joins
order by
limit
set operators (only union all)
distinct
aggregates, having
what are all the aggregate fns?
also show agg distinct

window functions
what are all the window fns
show aggs in windwos
partition, order



nested queries
ctes

query external table


..
  not enough interesting to say about scalar expressions here specifically
  here are some things to try to work into the other examples:

  'string literal'
  'something with ''quotes'' and stuff'
  1
  0.2
  3e-4
  null
  true
  false
  a + b
    and, or, comparisons,
    ||, like, rlike
  not true
  is null/ is not null
  a in (1,2,3)
  between
  extract
  coalesce
  nullif
  case 2 variations
  *
  function app

  cast(a as b)
  a :: b
 


    

Tables
------

create table
columns + types
schema
defaults
null, not null


alter table: add column, drop column, rename column, rename table

create table as

Inserting data
--------------

insert

external tables
select insert
copy


delete
-----------

delete from t;
truncate t;
delete from t where ...

views
-----

create and drop

saved queries
-------------

udfs
------

access control
--------------

roles as users/logins:
create, alter, drop role
rename role

permissions
grant, revoke

groups

default permissions
  
notes
=============

figure out how to put these in sections
maybe some of it should go before the sql features and some after



5TB to 500TB+

columnar
external algos
scaling
gpus

catalog

wlm

cluster/concurrency/ha system

docker

metadata system


can support 30+ concurrent users

has high availability

runs on prem or on the cloud

we see customers able to go from 3 months to 12 years data

extremely fast data loading speed

robust serializable transactions and concurrency control

wide range of client drivers

integrates with a wide range of third party components

performance
cost/ tco

highly responsive team, including new feature development

