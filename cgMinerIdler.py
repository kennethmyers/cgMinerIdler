import time
import subprocess
import os

from IdleTools import getTimeIdleInMilliseconds

IDLE_TIME_THRESHOLD = 10000

d = dict(os.environ)   # Make a copy of the current environment
d['GPU_MAX_ALLOC_PERCENT'] = '100'

lowIntensityMiningCommand = './miner_command_low.sh'
highIntensityMiningCommand = './miner_command_high.sh'
time.sleep(10)
miningProcess = subprocess.Popen("./miner_command_high.sh", shell=True, env=d)



high_power = False
while True:
    idleTime = getTimeIdleInMilliseconds()
    if idleTime > IDLE_TIME_THRESHOLD:
        idleTime = IDLE_TIME_THRESHOLD + 1

    if idleTime > IDLE_TIME_THRESHOLD:
        if not high_power:
            miningProcess.kill()
            miningProcess = subprocess.Popen(highIntensityMiningCommand, shell=True, env=d)
            high_power = True
    else:
        if high_power:
            miningProcess.kill()
            miningProcess = subprocess.Popen(lowIntensityMiningCommand, shell=True, env=d)
            high_power = False