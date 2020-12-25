# The MIT License (MIT)
# Copyright (c) 2020, Tangliufeng for labplus Industrie

# iBeacon 示例
# 手机使用nRF Beacon app配合示例演示Beacon功能

from mpython_ble.application.beacon import iBeacon
from mpython_ble import UUID

# Proximity UUID 
uuid = UUID("01122334-4556-6778-899a-abbccddeeff0")

# 构建iBeacon 对象
beacon = iBeacon(proximity_uuid=uuid, major=1, minor=2)

# 开始广播
beacon.advertise(Toggle=True)
