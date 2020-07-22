# The MIT License (MIT)
# Copyright (c) 2020, Tangliufeng for labplus Industrie

# 蓝牙PPT翻页笔
# 下一页: A键  / 上一页: B键

from mpython_ble.application import HID
from mpython_ble.hidcode import KeyboardCode
from mpython import oled, button_a, button_b
import time
import music

ppt_remote = HID(name=b'ble_ppt')  # 实例 BLE HID设备

oled.DispChar("蓝牙ppt翻页笔", 20, 10)
oled.DispChar("说明:下页A键 下页B键", 0, 30)
oled.show()

# 初始化button_before标记变量
btn_a_stat_before = button_a.value()
btn_b_stat_before = button_b.value()

while True:
    # 读取button_a,button_b状态
    btn_a_stat_current = button_a.value()
    btn_b_stat_current = button_b.value()
    time.sleep_ms(20)

    # 检测A键按下时,发送键盘按键码,"PgUp"
    if button_a.value() == btn_a_stat_current:
        if btn_a_stat_before ^ btn_a_stat_current:
            if btn_a_stat_before == 1:
                ppt_remote.keyboard_send(KeyboardCode.PAGE_UP)
                music.pitch(2000, 50, wait=False)
                print("pressed Page Up!")
            btn_a_stat_before = btn_a_stat_current

    # 检测B键按下时,发送键盘按键码,"PgDown"
    if button_b.value() == btn_b_stat_current:
        if btn_b_stat_before ^ btn_b_stat_current:
            if btn_b_stat_before == 1:
                ppt_remote.keyboard_send(KeyboardCode.PAGE_DOWN)
                music.pitch(2000, 50, wait=False)
                print("pressed Page Down!")
            btn_b_stat_before = btn_b_stat_current
