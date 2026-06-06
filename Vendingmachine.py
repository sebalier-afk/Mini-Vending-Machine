from adafruit_servokit import ServoKit
import time 
kit = ServoKit(channels=16)


kit.servo[0].angle = +30
time.sleep(1)

kit.servo[1].angle = 30
time.sleep(1)

kit.servo[2].angle = 30
time.sleep(1)

kit.servo[3].angle = 30
time.sleep(1)

kit.servo[4].angle = 30
time.sleep(1)

kit.servo[5].angle = 30
time.sleep(1)

kit.servo[6].angle = 30
time.sleep(1)
