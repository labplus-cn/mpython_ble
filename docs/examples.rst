简单的温度外设
----------------

.. literalinclude:: ../examples/ble_temperature.py
    :caption: ble 环境温度设备: examples/ble_temperature.py
    :linenos:

中央设备连接温度外设
----------------


.. literalinclude:: ../examples/ble_temperature_central.py
    :caption: 中央设备ble连接上面示例的温度设备: examples/ble_temperature_central.py
    :linenos:


Nordic UART
----------------

通过 Nordic UART 服务的应用,实现与上位机位端(手机或电脑)的串口通信。

.. literalinclude:: ../examples/uart_peripheral.py
    :caption: examples/uart_peripheral.py
    :linenos:

使用 "nRF Connect" 、"nRF Toolbox"等上位机软件或app inventor自己制作APP,来收发BLE UART的数据。

.. figure:: /images/uart_nrfconenct.gif
    :align: center
    :width: 300

    nRF Connect 查看UART gatt


.. figure:: /images/uart_nrftoolbox.gif
    :align: center
    :width: 300

    nRF Toolbox 演示与UART与上位机的通讯应用




人机交互设备-翻页笔
----------------

.. literalinclude:: ../examples/ble_ppt_remote.py
    :caption: ppt翻页笔: examples/ble_ppt_remote.py
    :linenos:
