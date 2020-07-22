# The MIT License (MIT)
# Copyright (c) 2020, Tangliufeng for labplus Industrie

# Nordic UART 服务的外围设备的示例
# 中央设备端可用手机APP,"nRF Conenct" 或 "nRF Toolbox",配合使用

from mpython_ble.application import BLEUART
import time

uart = BLEUART(name=b'ble_uart')


def rx_irq():
    """串口接收中断函数定义"""
    print('Receive: ', uart.read().decode().strip())


uart.irq(handler=rx_irq)    # 串口中断

# 发送数据
nums = [4, 8, 15, 16, 23, 42]
i = 0

try:
    while True:
        uart.write(str(nums[i]) + '\n')
        i = (i + 1) % len(nums)
        time.sleep_ms(1000)
except KeyboardInterrupt:
    pass

uart.close()
