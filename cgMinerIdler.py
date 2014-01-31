import time
import subprocess
import os
import signal

from IdleTools import getTimeIdleInMilliseconds

IDLE_TIME_THRESHOLD = 10000

lowIntensityMiningCommand = './miner_command_low.sh'
highIntensityMiningCommand = './miner_command_high.sh'

# Set environment variables.
environmentVariables = dict(os.environ)
environmentVariables['GPU_MAX_ALLOC_PERCENT'] = '100'

time.sleep(10)
miningProcess = subprocess.Popen(lowIntensityMiningCommand, shell=True, env=environmentVariables, preexec_fn=os.setsid)

high_power = False
while True:
    idleTime = getTimeIdleInMilliseconds()
    if idleTime > IDLE_TIME_THRESHOLD:
        idleTime = IDLE_TIME_THRESHOLD + 1

    if idleTime > IDLE_TIME_THRESHOLD:
        if not high_power:
            os.killpg(miningProcess.pid, signal.SIGTERM)
            miningProcess = subprocess.Popen(highIntensityMiningCommand, shell=True, env=environmentVariables)
            high_power = True
    else:
        if high_power:
            os.killpg(miningProcess.pid, signal.SIGTERM)
            miningProcess = subprocess.Popen(lowIntensityMiningCommand, shell=True, env=environmentVariables)
            high_power = False