:py:mod:`mpython_ble`
=======================


.. py:class:: UUID(value)

用指定的值创建一个UUID实例。与 `bluetooth.UUID` 类相同。

该值可以是:

   - 一个16位整数。例如 ``0x2908`` 。
   - 128位UUID字符串。例如 ``6E400001-B5A3-F393-E0A9-E50E24DCCA9E`` 。

   >>> from mpython_ble import UUID
   >>> UUID(0x2908)
   UUID16(0x2908)
   >>> UUID("6E400001-B5A3-F393-E0A9-E50E24DCCA9E")
   UUID128('6e400001-b5a3-f393-e0a9-e50e24dcca9e')


-----------------------------------------------------------------

**子模块目录** :

.. toctree::
   :maxdepth: 1
   
   application
   gatts
   services
   characteristics
   descriptors
   hidcode
   beacon

