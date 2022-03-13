.. _use_legacy_string_literals:

*************************
Using Legacy String Literals
*************************
The ``useLegacyStringLiterals`` flag interprets ASCII-only strings as **VARCHAR** instead of **TEXT**. This flag is used to preserve legacy behavior in existing customers.

The following describes the ``useLegacyStringLiterals`` flag:

* **Data type** - boolean
* **Default value** - ``false``
* **Allowed values** - ``true``, ``false``