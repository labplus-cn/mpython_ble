:py:mod:`mpython_ble.gatts`
=================================


GATT(Generic Attribute Profile)通用属性配置文件,描述了一种使用ATT的服务框架
该框架定义了服务(Server)和服务属性(characteristic)。


Profile类
--------------

GATT Profile是Services和Characteristics的高级嵌套。Profile包含一个或多个的 `Service` 服务; 一个 `Service` 服务包含一个或多个 `Characteristic` 特征；
`Characteristic` 特征可包含 `Descriptors` 描述符(也可以没有)。用于设备应用服务描述,比如心率计要有哪些服务、哪些特性、哪些描述符等。

.. image:: https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWFnZXMwLmNuYmxvZ3MuY29tL2Jsb2cvNDE3ODg3LzIwMTQxMi8xMTE5NDUxNjQ5MzIzMjgucG5n?x-oss-process=image/format,png
    :width: 450
    :align: center


.. py:class:: Profile()

`Profile` 是 :class:`Service` 服务对象的集合。

方法
~~~~~~~~~

.. py:method:: Profile.add_services(*services)

添加 `Service` 服务。`services` 参数为 :class:`Service` 类的实例对象。

.. py:attribute:: Profile.services_uuid

返回 `Profile` 内的 Service 服务的 :class:`UUID` 对象元组。


.. py:attribute:: Profile.definition

返回服务定义services_definition。services_definition是服务元组，其中每个服务包含 `UUID` 和特征的两元组。
每个特征是包含UUID、flags值(属性权限)、可选的描述符列表的两或三元组。
每个描述符包含UUID和 flags值的两元组。

.. Hint:: 

    该函数用于 `BLE.gatts_register_services()` 服务注册函数services_definition参数组建。


.. py:attribute:: Profile.handles


返回值Profile 的 `Characteristic` 特征 和 `Descriptors` 描述符的 `value_handle` 值柄的元组的列表。
每个服务一个元组, 每个服务元组是服务内定义的顺序特征和描述符句柄展平。

.. Hint:: 

    用于 `BLE.gatts_register_services()` 服务注册后, 返回属性值柄映射到 GATT Profile内的对应属性 :class:`Characteristic` 对象, :class:`Descriptor` 对象的 `value_handle` 值柄。



