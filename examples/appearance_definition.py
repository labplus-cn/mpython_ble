# The MIT License (MIT)
# Copyright (c) 2020, Tangliufeng for labplus Industries

from micropython import const

# appearance definition
# org.bluetooth.characteristic.gap.appearance.xml


class Appearance(object):
    Unknown = const(0)  # None
    GENERIC_PHONE = const(64)  # Generic category
    GENERIC_COMPUTER = const(128)  # Generic category
    GENERIC_WATCH = const(192)  # Generic category
    WATCH_SPORTS_WATCH = const(193)  # Watch subtype
    GENERIC_CLOCK = const(256)  # Generic category
    GENERIC_DISPLAY = const(320)  # Generic category
    GENERIC_REMOTE_CONTROL = const(384)  # Generic category
    GENERIC_EYE_GLASSES = const(448)  # Generic category
    GENERIC_TAG = const(512)  # Generic category
    GENERIC_KEYRING = const(576)  # Generic category
    GENERIC_MEDIA_PLAYER = const(640)  # Generic category
    GENERIC_BARCODE_SCANNER = const(704)  # Generic category
    GENERIC_THERMOMETER = const(768)  # Generic category
    THERMOMETER_EAR = const(769)  # Thermometer subtype
    GENERIC_HEART_RATE_SENSOR = const(832)  # Generic category
    HEART_RATE_SENSOR_HEART_RATE_BELT = const(833)  # Heart Rate Sensor subtype

    # Added Blood pressure support on December 09, 2011
    GENERIC_BLOOD_PRESSURE = const(896)  # Generic category
    BLOOD_PRESSURE_ARM = const(897)  # Blood Pressure subtype
    BLOOD_PRESSURE_WRIST = const(898)  # Blood Pressure subtype

    # Added HID Related appearance values on January 03, 2012 approved by BARB
    HUMAN_INTERFACE_DEVICE_HID = const(960)  # HID Generic
    KEYBOARD = const(961)  # HID subtype
    MOUSE = const(962)  # HID subtype
    JOYSTICK = const(963)  # HID subtype
    GAMEPAD = const(964)  # HID subtype
    DIGITIZER_TABLET = const(965)  # HID subtype
    CARD_READER = const(966)  # HID subtype
    DIGITAL_PEN = const(967)  # HID subtype
    BARCODE_SCANNER = const(968)  # HID subtype

    # Added Generic Glucose Meter value on May 10, 2012 approved by BARB
    GENERIC_GLUCOSE_METER = const(1024)  # Generic category

    # Added additional appearance values on June 26th, 2012 approved by BARB
    GENERIC_RUNNING_WALKING_SENSOR = const(1088)  # Generic category
    RUNNING_WALKING_SENSOR_IN_SHOE = const(1089)  # Running Walking Sensor subtype
    RUNNING_WALKING_SENSOR_ON_SHOE = const(1090)  # Running Walking Sensor subtype
    RUNNING_WALKING_SENSOR_ON_HIP = const(1091)  # Running Walking Sensor subtype
    GENERIC_CYCLING = const(1152)  # Generic category
    CYCLING_CYCLING_COMPUTER = const(1153)  # Cycling subtype
    CYCLING_SPEED_SENSOR = const(1154)  # Cycling subtype
    CYCLING_CADENCE_SENSOR = const(1155)  # Cycling subtype
    CYCLING_POWER_SENSOR = const(1156)  # Cycling subtype
    CYCLING_SPEED_AND_CADENCE_SENSOR = const(1157)  # Cycling subtype

    # Added appearance values for Pulse Oximeter on July 30th, 2013 approved by BARB
    GENERIC_PULSE_OXIMETER = const(3136)  # Pulse Oximeter Generic Category
    FINGERTIP = const(3137)  # Pulse Oximeter subtype
    WRIST_WORN = const(3138)  # Pulse Oximeter subtype

    # Added appearance values for Generic Weight Scale on May 21, 2014 approved by BARB
    GENERIC_WEIGHT_SCALE = const(3200)  # Weight Scale Generic Category

    # Added additional appearance values on October 2nd, 2016 approved by BARB
    GENERIC_PERSONAL_MOBILITY_DEVICE = const(3264)  # Personal Mobility Device
    POWERED_WHEELCHAIR = const(3265)  # Personal Mobility Device
    MOBILITY_SCOOTER = const(3266)  # Personal Mobility Device
    GENERIC_CONTINUOUS_GLUCOSE_MONITOR = const(3328)  # Continuous Glucose Monitor

    # Added additional appearance values on February 1st, 2018 approved by BARB
    GENERIC_INSULIN_PUMP = const(3392)  # Insulin Pump
    INSULIN_PUMP_DURABLE_PUMP = const(3393)  # Insulin Pump
    INSULIN_PUMP_PATCH_PUMP = const(3396)  # Insulin Pump
    INSULIN_PEN = const(3400)  # Insulin Pump
    GENERIC_MEDICATION_DELIVERY = const(3456)  # Medication Delivery

    # Added appearance values for L&N on July 30th, 2013 approved by BARB
    GENERIC_OUTDOOR_SPORTS_ACTIVITY = const(5184)  # Outdoor Sports Activity Generic Category
    LOCATION_DISPLAY_DEVICE = const(5185)  # Outdoor Sports Activity subtype
    LOCATION_AND_NAVIGATION_DISPLAY_DEVICE = const(5186)  # Outdoor Sports Activity subtype
    LOCATION_POD = const(5187)  # Outdoor Sports Activity subtype
    LOCATION_AND_NAVIGATION_POD = const(5188)  # Outdoor Sports Activity subtype
