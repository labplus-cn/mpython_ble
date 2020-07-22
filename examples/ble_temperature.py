
from mpython_ble.gatts import Profile
from mpython_ble import UUID
from mpython_ble.services import Service
from mpython_ble.characteristics import Characteristic
from mpython_ble.application import Peripheral
import time
import struct
import random

# 实例profile
profile = Profile()
# 实例Service 环境传感器服务(0x181A)  
# org.bluetooth.service.environmental_sensing
env_sense_service = Service(UUID(0x181A))
# 实例 Characteristic 温度特征(0x2A6E),权限为可读,通知  
# org.bluetooth.characteristic.temperature
temp_char = Characteristic(UUID(0x2A6E), properties='rn')
# 环境传感器服务添加温度特征
env_sense_service.add_characteristics(temp_char)

# 将服务添加到profile
profile.add_services(env_sense_service)

# 实例BLE外设
perip_temp = Peripheral(name=b'mpy_temp', profile=profile, adv_services=profile.services_uuid)
# 开始广播
perip_temp.advertise(True)

t = 25
i = 0
while True:
    # Write every second, notify every 10 seconds.
    time.sleep(1)
    i = (i + 1) % 10
    # Data is sint16 in degrees Celsius with a resolution of 0.01 degrees Celsius.
    # Write the local value, ready for a central to read.
    perip_temp.attrubute_write(temp_char.value_handle, struct.pack('<h', int(t * 100)), notify=i == 0)
    # Random walk the temperature.
    t += random.uniform(-0.5, 0.5)
