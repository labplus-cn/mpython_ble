:py:mod:`mpython_ble.application`
=================================

基于蓝牙BLE的应用,本模块中定义了Peripheral(外围设备) 和Centeral(中央设备)两大类。

    - 外围设备：这一般就是非常小或者简单的低功耗设备，用来提供数据，并连接到一个更加相对强大的中心设备。例如蓝牙心率计。
    - 中心设备：中心设备相对比较强大，用来连接其他外围设备。例如手机、电脑等。

在蓝牙应用中外围设备最为广泛,涵盖的设备多种多样。本模块中基于 `Peripheral` 类,又再封装了 `UART` 和 `HID` ,用于串口收发和人机交互设备的应用。

Peripheral类
--------------

BLE 外围设备

构建对象
~~~~~~~~~

.. py:class:: Peripheral(profile, name=b'mpy_ble', appearance=0, adv_services=None, resp_services=None, interval_us=500000, connectable=True)

    - `profile` - GATT :class:`Profile` 实例对象。用于描述BLE设备具备哪些服务信息。有关Profile的用法,请查阅 :class:`Profile` 类。
    - `name` -  蓝牙设备名称。类型为字节类型。
    - `appearance` -  16-bit 数字编码。定义蓝牙设备的外观,像电脑或手机会根据该外观标识,给定外观图标。默认为Unknown(0)。
    - `adv_services` - 广播负载服务。外围设备会向广播通达发送设备的广播数据,告诉主机,设备具有哪些服务。
    - `resp_services` - 扫描应答负载服务。当主机主动扫描广播设备,发起Scan Request,外围设备会应答resp_services服务。
    - `interval_us` - 以指定的时间间隔（以微秒为单位）广播
    - `connectable` - 设置外围设备是否为可连接,默认为 `True` , `False` 则设备为单纯的广播者,不可连接。

实例完成且BLE蓝牙开启,完成蓝牙服务注册后。会将 `profile` 里的属性的句柄赋值到相应的 `value_handle`。以便后面对属性进行读写操作。

.. Hint:: 

    - 考虑到esp32的内存有限,所以并没有在类中没有定义appearance常量, 用户可根据 `appearance_definition <../../../../examples/appearance_definition.py>`_ 按需自定义。
    - 由于广播报文有长度限制37 Bytes。在配置 adv_services,resp_services 参数时,需注意广播的服务不能太多,应合理分配。

方法
--------

.. py:method:: Peripheral.advertise(toggle=True)

外围设备广播开关。 `toggle` 为 `True` 则,开始广播; `False` 则停止广播。

.. py:method:: Peripheral.attrubute_read(value_handle)

读取BLE设备的属性值,返回类型为 `Bytes` 类型。

    - `value_handle` - Characteristic或Descriptor属性的值柄

.. py:method:: Peripheral.attrubute_write(value_handle, data, notify=False)

写BLE设备的属性值。

    - `value_handle` - Characteristic或Descriptor属性的值柄
    - `data` - 写入的字节数据。类型为 `Bytes` 。

.. py:method:: Peripheral.connection_callback(callback)

外围设备与中央设备建立连接的回调函数。回调函数的参数定义 callback_function(conn_handle, addr_type, addr)。`conn_handle` 参数为连接的句柄, `addr_type` 为地址类型 , `addr` 为发起连接
的中央设备的MAC地址,类型为 `Bytes` 。


.. py:method:: Peripheral.write_callback(callback)

当BLE设备的属性值被写操作的回调函数。callback_function(conn_handle, attr_handle, data)。`conn_handle` 参数为连接的句柄, `attr_handle` 为被写得属性值柄 , `data` 为写入的数据,类型为 `Bytes` 。

.. py:method:: Peripheral.disconnect()

外围设备断开与中央设备的连接。

.. py:attribute:: Peripheral.mac

返回外围设备的MAC地址,类型为 `Bytes` 。

Centeral类
--------------

中央设备

构建对象
~~~~~~~~~

.. py:class:: Centeral(name=b'mpy_centeral')

    - `name` - BLE设备的名称

方法
~~~~~~~~~

.. py:method:: Centeral.connect(name=b'', addr=None)

中央设备发起连接。`name` 和 `addr` 参数,二选一。可通过BLE广播的设备名称来连接。或者你已知要连接的外围设备的 `MAC` 地址,可通过 `addr` 参数发起连接。

如连接成功后,则返回 被连接设备的 GATT :class:`Profile` 对象。如,连接不成功或扫描不到设备则返回 `None` 。

.. py:method:: Centeral.is_connected()

返回中央设备与外围设备是否连接。`True` 为连接, `False` 为未连接。

.. py:method:: Centeral.characteristic_read(value_handle)

读取被连接的外围设备的属性值

    - `value_handle` - Characteristic的值柄。

.. py:method:: Centeral.characteristic_write(value_handle, data)

写被连接的外围设备的属性值

    - `value_handle` - Characteristic的值柄。
    - `data` - 写入的字节数据。类型为 `Bytes` 。

.. py:method:: Centeral.notify_callback(callback)

当被连接的外围设备,发起notify通知事件,告知特征属性被改写。
回调函数的参数定义 callback_function(value_handle, notify_data) `value_handle` 参数为属性的值柄, `notify_data` 参数为通知的属性值。


.. py:attribute:: Centeral.connected_info

连接成功后, `connected_info` 有被连接的外围设备的设备信息元组。
格式: (addr_type, addr, name, adv_type, rssi) 


BLEUART类
--------------

UART服务是在连接的设备之间发送和接收数据的标准方法，它模拟了熟悉的两线UART接口（一根线用于传输数据，另一线用于接收数据）。

该服务模拟通过两条线路TXD和RXD的基本串口连接。
它基于Nordic Semiconductors专有的UART服务规范。可以使用Nordic Semiconductors用于Android和iOS的nRFUART应用查看与该服务之间收发的数据。

Nordic的UART UUID("6E400001-B5A3-F393-E0A9-E50E24DCCA9E") 服务包括以下特征：

================ ======================= ==================
Name              UUID                    权限
TX                0x0002                  write                  
RX                0x0003                  read/notify                 
================ ======================= ==================

- TX : 此特性用于将数据发送回传感器节点，并且可以由连接的中央设备（移动电话，平板电脑等）写入。
- RX : 此特性用于将数据发送到连接的中央设备。可以通过连接的设备启用通知，以便每次更新TX通道时发出警报


构建对象
~~~~~~~~~

.. py:class:: BLEUART(name=b'ble_uart', appearance=0, rxbuf=100)

UART服务的外围设备, 可用于模拟串口数据收发。对于初级BLE用户,可不用关注BLE协议,即可达到两设备之间的通讯。

    - `name` -  蓝牙设备名称。类型为字节类型。
    - `appearance` -  16-bit 数字编码。定义蓝牙设备的外观,像电脑或手机会根据该外观标识,给定外观图标。默认为Unknown(0)。
    - `rxbuf` - UART的接收缓存大小设置,单位为 Byte。

方法
~~~~~~~~~~

.. py:method:: BLEUART.any()

返回可读字节数量

.. py:method:: BLEUART.irq()

当串口接收的数据的中断函数。

.. py:method:: BLEUART.read(size=Nones)

读取串口缓存字节。

    - `size` - 读取字节数

.. py:method:: BLEUART.write(data)

往串口TX写字节。

    - `data` - 为写入的数据,类型为 `Bytes` 。 

.. py:method:: BLEUART.close()

关闭串口。

HID类
--------------

HID设备(Human Interface Devices)，即人机交互设备，常见的有鼠标，键盘，游戏手柄，遥控器等等。一般有线方式都是通过USB连线连接到机器设备，作为用户输入设备。
在蓝牙BLE技术中,通过GATT配置HID Service实现无线的HID设备应用。

HID类实现以下的BLE HID设备:

    - 键盘设备
    - 鼠标设备
    - 消费类设备(例如遥控器)

构建对象
~~~~~~~~~

.. py:class:: HID(name=b'mpy_hid', battery_level=100)

    - `name` - HID设备名称,类型为 `Bytes` 。
    - `battery_level` - 设置HID设备的电池电量


公共方法
~~~~~~~~~

.. py:method:: HID.advertise(toggle=True)

HID设备广播开关。 `toggle` 为 `True` 则,开始广播; `False` 则停止广播。

.. py:method:: HID.disconnect()

HID设备断开与中央设备的连接

.. py:attribute:: HID.battery_level

返回或配置HID设备的电池电量

鼠标设备
''''''''

HID鼠标设备的函数方法

.. py:method:: HID.mouse_click(buttons)

点击鼠标按键。`buttons` 为鼠标按键。你可以使用 ``|`` 或逻辑运算实现多个按键同时按下操作。

鼠标按键常量见, :mod:`hidcode.Mouse` 。

    >>> from mpython_ble.application import HID
    >>> from mpython_ble.hidcode import Mouse
    >>> mouse = HID()
    >>> mouse.mouse_click(Mouse.LEFT)  # left button

.. py:method:: HID.mouse_press(buttons)

按住鼠标按键。使用同上述。

.. py:method:: HID.mouse_release(buttons)

释放鼠标按键。使用同上述。

.. py:method:: HID.mouse_release_all()

释放所有鼠标按键。

.. py:method:: HID.mouse_move( x=0, y=0, wheel=0)

鼠标光标移动、滚轮。

    - `x`, `y` - 光标移动量,范围 ±127 。
    - `wheel` - 滚轮,范围 ±127 。

键盘设备
''''''''

HID键盘设备的函数方法

.. Hint::

    按键键值常量见, :mod:`hidcode.KeyboardCode` 。如果你的可用内存不多,不建议你使用 hidcode 模块。你可按需,自行定义常量,减少不必要
    的内存浪费。




.. py:method:: HID.keyboard_send(*keycodes)

点击键盘按键,支持单个或多个按键按下。`keycodes` 为键盘的键值。一次不能超过6个按键。

    >>> from mpython_ble.application import HID
    >>> form mpython_ble.hidcode import KeyboardCode
    >>> hid = HID()
    >>> hid.keyboard_send(KeyboardCode.CONTROL,KeyboardCode.D)     # ctrl-d

.. py:method:: HID.keyboard_press(*keycodes)

按住键盘按键。使用同上述。

.. py:method:: HID.keyboard_release(*keycodes)

释放键盘按键。使用同上述。

.. py:method:: HID.keyboard_release_all()

释放所有按键。使用同上述。

消费类设备
''''''''

.. Hint::

    按键键值常量见, :mod:`hidcode.ConsumerCode` 。如果你的可用内存不多,不建议你使用 hidcode 模块。你可按需,自行定义常量,减少不必要
    的内存浪费。

.. py:method:: HID.consumer_send(consumer_code)

消费类设备单个按键点击。

