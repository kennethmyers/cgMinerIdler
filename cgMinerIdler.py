import time

import pexpect

from IdleTools import getTimeIdleInMilliseconds

IDLE_TIME_THRESHOLD = 10000

lowIntensityMiningCommand = 'mate-terminal -e "/home/kenneth/Desktop/cgminer-3.7.0-x86_64-built/cgminer -o stratum+tcp://stratum2.wemineltc.com:3335 -u kennyguy.cool -p beans -o stratum+tcp://stratum.hashfaster.com:3333 -u kennyguy.cool -p beans --scrypt -I 13 --auto-fan --temp-target 78 --temp-overheat 85 --temp-cutoff 90"'
highIntensityMiningCommand = 'mate-terminal -e "/home/kenneth/Desktop/cgminer-3.7.0-x86_64-built/cgminer -o stratum+tcp://stratum2.wemineltc.com:3335 -u kennyguy.cool -p beans -o stratum+tcp://stratum.hashfaster.com:3333 -u kennyguy.cool -p beans --scrypt -I 20 --auto-fan --temp-target 78 --temp-overheat 85 --temp-cutoff 90"'

child = pexpect.spawn(lowIntensityMiningCommand)
time.sleep(10)


high_power = False
while True:
    idleTime = getTimeIdleInMilliseconds()
    if idleTime > IDLE_TIME_THRESHOLD:
        idleTime = IDLE_TIME_THRESHOLD + 1

    if idleTime > IDLE_TIME_THRESHOLD:
        if not high_power:
            child.terminate(force=True)
            child = pexpect.spawn(highIntensityMiningCommand)
            high_power = True
    else:
        if high_power:
            child.terminate(force=True)
            child = pexpect.spawn(lowIntensityMiningCommand)
            high_power = False