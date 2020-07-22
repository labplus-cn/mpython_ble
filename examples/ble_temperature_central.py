
from mpython_ble.application import Centeral
from mpython_ble import UUID
import time
import struct


def convert_temperature(bytes_):
    """温度值还原"""
    # 对bytes拆包,转为整形数据。字节的储存顺序为little-endian,无符号整形,2字节。
    # 除100,还原浮点型
    temperature = struct.unpack("<H", bytes_)[0]/100
    return temperature


# 实例BLE中央设备
temp_centeral = Centeral()

# 扫描 temperature device 并连接
while True:
    temp_profile = temp_centeral.connect(name=b'mpy_temp')
    if temp_centeral:
        break
    time.sleep(2)

print("Connected temperature device. gatt profile:")
# print service
for service in temp_profile:
    print(service)


def temperature_notify_callback(value_handle, notify_data):
    """温度特征值的通知事件的回调函数"""
    global temp_characteristic
    # 判断是否为温度特征句柄值
    if value_handle == temp_characteristic.value_handle:
        temperature = convert_temperature(notify_data)
        print("temperature notify: {}" .format(temperature))


for service in temp_profile:
    # 查询 environmental_sensing 服务
    if service.uuid == UUID(0x181A):
        print("find environmental_sensing service (0x181a)")
        for characteristics in service:
            print("find temperature characteristic (0x2a6e)")
            if characteristics.uuid == UUID(0x2A6E):
                temp_characteristic = characteristics
                temperature_bytes = temp_centeral.characteristic_read(temp_characteristic.value_handle)
                print("temperature value is: {}" .format(convert_temperature(temperature_bytes)))
                # 设置温度特征值的回调函数
                temp_centeral.notify_callback(temperature_notify_callback)
