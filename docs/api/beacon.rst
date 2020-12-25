:py:mod:`mpython_ble.beacon`
=================================

iBeacon是苹果推出一项基于蓝牙Bluetooth BLE的精准微定位技术。iBeacon基站不断向四周发送蓝牙信号，当
智能设备进入设定区域是，就能收到信号。

正如beacon英文信标、灯塔的字面意思，这种设备以一定的时间间隔发送数据包，并且发送的数据可以被像手机这样的设备获取。
同时与信标的远近可以根据信标的信号强度大小来判断，距离越远，信标信号越弱。根据距离远近，分了4个状态。

- Immediate
- Near
- Far
- Unknown


iBeacon类
--------------


构建对象
~~~~~~~~~

.. py:class:: iBeacon(proximity_uuid, major, minor, company_id=0x004C, tx_power=0xC5)

    - `proximity_uuid` - Beacon设备机构的UUID。该参数为UUID对象。如，UUID("01122334-4556-6778-899a-abbccddeeff0")
    - `major` - 区分位置信息，major一般表示分组编号。
    - `minor` - 区分位置信息，minor一般表示组内编号。
    - `company_id` - 公司的身份标识号，默认使用0x004C，代表Apple。
    - `tx_power` - Measured Power。模块与接收器之间相距1m时的参考接收信号强度。


公共方法
~~~~~~~~~

.. py:method:: iBeacon.advertise(toggle=True, interval_us=500000)

开始Beacon设备广播设置

    - `toggle` - 翻转。True为开始广播，False为停止广播。
    - `interval_us` - 广播间隔。