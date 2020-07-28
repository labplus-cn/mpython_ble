
介绍
===============

.. image:: http://oss.cyzone.cn/2014/1204/20141204040006220.jpg
    :width: 400
    :align: center


本模块是基于 `MicroPython bluetooth <http://docs.micropython.org/en/latest/library/ubluetooth.html>`_ 提供更高级抽象的BLE应用的驱动库。
为初级蓝牙BLE的初阶用户,提供友善的接口,用户可以很简易的实现BLE的应用。

本模块适用于 `MicroPython <https://github.com/micropython/micropython/>`_ 及衍生的相关项目,如掌控板 `mPython <https://github.com/labplus-cn/mpython>`_ 。

- 托管文档: https://mpython-ble.readthedocs.io/
- github: https://github.com/labplus-cn/mpython_ble

模块根据蓝牙BLE的应用和饰演的角色,设计以下几大功能点:

* `外围设备(Peripheral)` 
* `中央设备(Centeral)` 
* `串口透传(Uart)` 
* `人机交互设备HID` 

快速入门
===============


首先需要将 `mpython_ble <https://github.com/labplus-cn/mpython_ble>`_  库上传到MicroPython的文件系统中。


在实例BLE Peripheral 设备前,先要配置 GATT Profile,注册一些服务和特征。通过profile来描述设备包含什么样的应用服务。
`Bluetooth 标准协议 <https://www.bluetooth.com/specifications/gatt/>`_ 里根据常用的蓝牙设备定义了通用的服务和特性,以便BLE设备间可更好的识别、兼容。
你可以按GATT中 16 bit的UUID来配置profile,或用128bit UUID 来定义自己的服务。

下面以体温计为例,我们可以需要在profile添加以下服务:

    - `Health Thermometer` : 蓝牙标准协议里规体温服务的正式16 bit UUID识别码是0x1809;还有需要添加必选项 `Temperature Measurement` 特征(0x2A1C)。
    - `Device Information` : 用于描述设备信息。添加 `Manufacturer Name String` 特征,用于描述制造商名称。

实例 `Health Thermometer` Service 对象并添加 `Temperature Measurement` Characteristic::

    >>> from mpython_ble.services import Service
    >>> from mpython_ble.characteristics import Characteristic
    >>>
    >>> health_thermometer_service = Service(UUID(0x1809))
    >>> temperature_measurement_charact = Characteristic(UUID(0x2A1C), properties='-rn')
    >>> health_thermometer_service.add_characteristics(temperature_measurement_charact)

实例 `Device Information` Service 对象并添加 `Manufacturer Name String` Characteristic::

    >>> device_info_service = Service(UUID(0x180A))
    >>> manufacturer_name = Characteristic(UUID(0x2A29),, properties='-r')
    >>> device_info_service.add_characteristics(manufacturer_name)

完成 `health_thermometer_service` 和 `device_info_service` 服务后,将服务添加至 `profile` 中::

    >>> from mpython_ble.gatts import Profile
    >>> profile = Profile()
    >>> profile.add_services(health_thermometer_service,device_info_service)

下面我们可以通过数组索引方式很方便的读取 `profile` 的服务、特性::

    >>> profile
    <Profile: <Service UUID16(0x1809): <Characteristic UUID16(0x2a1c), '-rn'>>, <Service UUID16(0x180a): <Characteristic UUID16(0x2a29), '-r'>>>
    >>> profile[0]   # first service
    <Service UUID16(0x1809): <Characteristic UUID16(0x2a1c), '-rn'>>
    >>> profile[1]   # second service
    <Service UUID16(0x180a): <Characteristic UUID16(0x2a29), '-r'>>
    >>> 
    >>> profile[0][0]   # Read temperature_measurement Characteristic
    <Characteristic UUID16(0x2a1c), '-rn'>

现在我们看下如何通过配置好的 `profile` 来实例 `Peripheral` BLE外设。

`profile.services_uuid` 是service的UUID列表。Peripheral 里的 `adv_services` 参数为需要广播的服务。

    >>> profile.services_uuid
    [UUID16(0x1809), UUID16(0x180a)]
    >>>
    >>> from mpython_ble.application import Peripheral
    >>> ble_thermometer = Peripheral(name=b'ble_thero', profile=profile, adv_services=profile.services_uuid)
    BLE: activated!
    
BLE 功能激活后,开启广播::

    >>> ble_thermometer.advertise(True)

你可以用手机的 `nRF Connect` app 来连接蓝牙设备

往 `Temperature Measurement` `Manufacturer Name String`  特征里写值。
由于温度值是浮点型的,为了便于解读,我们将温度值*100。蓝牙协议里规定字节的储存顺序为小端在前。int 转 Bytes,要用到
`struct` 来打包数据。

写入温度值,并通知连接主机::

    >>> import struct
    >>> temperature_value = 37.36
    >>> ble_thermometer.attrubute_write(temperature_measurement_charact.value_handle, struct.pack("<H",int(temperature_value*100)),notify=True)

写入制造商名称::

    >>> ble_thermometer.attrubute_write(manufacturer_name.value_handle,b'mpython')

这时,你可以在主机端,读取到被写入的值。

.. image:: ./images/introduction_nrfconenct.png
    :width: 200
    :align: center

参考资料
===============

- `Bluetooth协议 <https://www.bluetooth.com>`_
- `HID OVER GATT <https://www.bluetooth.org/docman/handlers/downloaddoc.ashx?doc_id=245141>`_
- `HID Usage Tables <https://www.usb.org/sites/default/files/documents/hut1_12v2.pdf>`_


贡献
===============

mpython_ble 部分源码参考以下项目,感谢作者的贡献:

- `Adafruit_CircuitPython_BLE <https://github.com/adafruit/Adafruit_CircuitPython_BLE>`_
- `walkline_Micropython BLE <https://gitee.com/walkline/micropython-ble-library>`_


