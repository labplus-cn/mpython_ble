:py:mod:`mpython_ble.descriptors`
=================================

Descriptor类
-----------------

Descriptor用来描述characteristic变量的属性。例如，一个descriptor可以规定一个可读的描述，或者一个characteristic变量可接受的范围，或者一个characteristic变量特定的测量单位。

构建对象
~~~~~~~~~

.. py:class:: Descriptor(uuid, properties='-r')

    - `uuid` - 为Descriptor的UUID实例对象。
    - `properties` -  特征的权限设置,定义了Descriptor的Value如何被使用。类型为字符串。

        - 可读 - 'r'
        - 可写 - 'w'
        - 通知 - 'n'

方法
~~~~~~~~~

.. py:attribute:: Descriptor.uuid

返回Characteristic服务的 :class:`UUID` 对象。

.. py:attribute:: Descriptor.value_handle

返回 Descriptor 的值柄,在 `gatts_register_services()` 服务注册前。默认为 `None` 。


