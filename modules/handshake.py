import sys

from common import Device
from logger import log

def handshake(dev, disable_watchdog=False):
    log("Handshake")
    dev.handshake()
    if disable_watchdog:
        log("Disable watchdog")
        dev.write32(0x10007000, 0x22000000)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        dev = Device(sys.argv[1])
    else:
        dev = Device()
        dev.find_device()
    handshake(dev)
