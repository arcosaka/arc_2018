#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
mortor.py 定数ファイル
"""

from enum import IntEnum

# defined const

class DCROTATE(IntEnum):
    """
    DCモーター回転方向
    """
    CCW = -1
    STOP = 0
    CW = 1

# for move_dc
DC_FREQ = 20 * 1000 # DCモーター周波数[Hz]
DC_DUTY = 40 # DCモーターDuty[%]
DC_PLUS = 10 # DCモーターDuty1周期変化量[%]

# for move_servo
SERVO_FREQ = 60
SERVO_MIN = 550
SERVO_MAX = 2400

# for move_step
STEP_1PULSE = 10 # 1パルス距離[mm]
STEP_FREQ = 120 * 1000 # ステッピングモーター周波数[Hz]
STEP_DUTY = 50 # ステッピングモーターDuty[%]

# (.+)\t(.+)\t(.+) $1 = $2 # $3