.. _use_legacy_string_literals:

*************************
Interpreting VARCHAR as TEXT
*************************
The ``useLegacyStringLiterals`` flag interprets ASCII-only strings as **VARCHAR** instead of **TEXT**. This flag is used to preserve legacy behavior in existing customers.

The following describes the ``useLegacyStringLiterals`` flag:

* **Data type** - boolean
* **Default value** - ``FALSE``
* **Allowed values** - ``true``, ``false``