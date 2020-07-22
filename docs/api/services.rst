:py:mod:`mpython_ble.services`
=================================

Service类
--------------

服务可以具有一个或多个特征，并且每个服务都通过称为UUID的唯一数字ID与其他服务区分开，
UUID可以是16位（蓝牙协议定义的正式的BLE服务）或128位（自定义服务）。

可以在Bluetooth 标准协议的 `org.bluetooth.servic <https://www.bluetooth.com/specifications/gatt/services/>`_ 上查看已定义的正式的BLE服务。
例如，如果您查看“ 心率服务”，我们可以看到此正式采用的服务具有16位UUID 0x180D，并包含多达3个特征，尽管只有第一个是必选的：心率测量，人体传感器位置和心率控制点。

构建对象
~~~~~~~~~

.. py:class:: Service(uuid)


`Service` 是 :class:`Characteristic` 特征对象的集合。

    - `uuid` 为Service的UUID实例对象。


例如, 心率服务 Heart Rate ( `org.bluetooth.service.heart_rate <https://www.bluetooth.com/xml-viewer/?src=https://www.bluetooth.com/wp-content/uploads/Sitecore-Media-Library/Gatt/Xml/Services/org.bluetooth.service.heart_rate.xml>`_)
的16位UUID为 `0x180D` :

    >>> from mpython_ble.services import Service
    >>> from mpython_ble import UUID
    >>> heart_rate_service = Service(UUID(0x180D))
    >>> heart_rate_service
    <Service UUID16(0x180D)>


方法
~~~~~~~~~

.. py:method:: Service.add_characteristics(*characteristics)

在服务中添加characteristics特征。返回添加后的Service自身。

    - `characteristics` 参数为 :class:`Characteristic` 对象。



在Heart Rate Service(`org.bluetooth.service.heart_rate <https://www.bluetooth.com/xml-viewer/?src=https://www.bluetooth.com/wp-content/uploads/Sitecore-Media-Library/Gatt/Xml/Services/org.bluetooth.service.heart_rate.xml>`_) 添加 Heart Rate Measurement 心率测量特征,UUID为0x2A37:

    >>> from mpython_ble.characteristics import Characteristic
    >>> heart_rate_measurement_chara = Characteristic(UUID(0x2A37),properties ='-r')
    >>> heart_rate_service.add_characteristics(heart_rate_measurement_chara)

.. py:attribute:: Service.uuid

返回Service服务的 :class:`UUID` 对象。

    >>> heart_rate_service.uuid
    UUID16(0x180D)

.. py:attribute:: Service.handles


返回Service包含的属性值柄元组。服务元组是服务内定义的顺序特征和描述符句柄展平。


.. Hint:: 

    该函数用于 `BLE.gatts_register_services()` 服务注册后, 返回属性值柄映射到 GATT Profile内的对应属性 :class:`Characteristic` 对象, :class:`Descriptor` 对象的 `value_handle` 值柄。

.. py:attribute:: Service.definition

返回服务定义services_definition中的Service元组。服务包含 `UUID` 和特征的两元组。
每个特征是包含UUID、flags值(属性权限)、可选的描述符列表的两或三元组。
每个描述符包含UUID和 flags值的两元组。


.. Hint:: 

    该函数用于 `BLE.gatts_register_services()` 服务注册函数,依照 `services_definition` 要求组建服务元组。
