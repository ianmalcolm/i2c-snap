#!/usr/bin/env python

import corr
import i2cSnap
import time

HOST = '10.1.0.23'
LED0_ADDR = 0x21
LED1_ADDR = 0x20

r = corr.katcp_wrapper.FpgaClient(HOST)
time.sleep(0.1)

i2c = i2cSnap.I2C(r, 'i2c_ant1')
i2c.clockSpeed(200)

i2c.writeSlave(LED1_ADDR, 1)
