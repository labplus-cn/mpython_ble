:py:mod:`mpython_ble.characteristics`
=======================================

Characteristic类
-----------------

GATT事务中最底层的概念是特性，与服务类似，每个特征都通过预定义的16位或128位UUID进行区分，您可以自由使用Bluetooth SIG定义的标准特征（这可以确保跨BLE和启用BLE的硬件/软件的互操作性）或定义自己的自定义特征，只有外围设备和软件才能理解。

例如，心率测量特性对于心率服务是必填项，并且使用0x2A37的UUID。它从描述HRM数据格式的单个8位值开始（无论数据是UINT8还是UINT16等），然后继续包含与该配置字节匹配的心率测量数据。
特性是您将与BLE外设进行交互的重点，因此理解这一概念很重要。它们还用于将数据发送回BLE外设，因为您也可以写入特征。

构建对象
~~~~~~~~~

.. py:class:: Characteristic(uuid,properties='-r')

`Characteristic` 由Properties、值柄, 一个或者多个Descriptor组成(可选项)。 是GATT profile中最基本的数据单位。

    - `uuid` - 为Service的UUID实例对象。
    - `properties` -  特征的权限设置,定义了characteristic的Value如何被使用。类型为字符串。

        - 可读 - 'r'
        - 可写 - 'w'
        - 通知 - 'n'

心率测量特征点:

    >>> from mpython_ble.characteristics import Characteristic
    >>> heart_rate_measurement_chara = Characteristic(UUID(0x2A37),properties ='-r')


方法
~~~~~~~~~

.. py:method:: Characteristic.add_descriptors(*descriptors)

在特征中添加descriptors描述符。返回添加后的Characteristic自身。

    - `descriptors` 参数为 :class:`Descriptors` 对象。

descriptors用于描述Characteristic Value相关的信息,作为非必须选项。（例如value记录距离长度，那么Descriptor可以是长度单位m/km）。


.. py:attribute:: Characteristic.value_handle

返回 Characteristic 的值柄,在 `gatts_register_services()` 服务注册前。默认为 `None` 。

.. py:attribute:: Characteristic.uuid

返回Characteristic服务的 :class:`UUID` 对象。

.. py:attribute:: Characteristic.handles

返回Characteristic包含的属性值柄元组。

.. Hint:: 

    该函数用于 `BLE.gatts_register_services()` 服务注册后, 返回属性值柄映射到 GATT Profile内的对应属性 :class:`Characteristic` 对象, :class:`Descriptor` 对象的 `value_handle` 值柄。


.. py:attribute:: Characteristic.definition


返回服务定义services_definition中的Characteristic元组。特征元组是包含UUID、flags值(属性权限)、可选的描述符列表的两或三元组。


.. Hint:: 

    该函数用于 `BLE.gatts_register_services()` 服务注册函数,依照 `services_definition` 要求组建服务元组。
