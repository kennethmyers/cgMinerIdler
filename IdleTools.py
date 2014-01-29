#!/usr/bin/python
import ctypes
import os

class XScreenSaverInfo( ctypes.Structure):
  """ typedef struct { ... } XScreenSaverInfo; """
  _fields_ = [('window',      ctypes.c_ulong), # screen saver window
              ('state',       ctypes.c_int),   # off,on,disabled
              ('kind',        ctypes.c_int),   # blanked,internal,external
              ('since',       ctypes.c_ulong), # milliseconds
              ('idle',        ctypes.c_ulong), # milliseconds
              ('event_mask',  ctypes.c_ulong)] # events


xlib = ctypes.cdll.LoadLibrary('libX11.so')
display = xlib.XOpenDisplay(os.environ['DISPLAY'])
xss = ctypes.cdll.LoadLibrary('libXss.so.1')
xss.XScreenSaverAllocInfo.restype = ctypes.POINTER(XScreenSaverInfo)

def getTimeIdleInMilliseconds():
		xssinfo = xss.XScreenSaverAllocInfo()
		xss.XScreenSaverQueryInfo(display, xlib.XDefaultRootWindow(display), xssinfo)
		return xssinfo.contents.idle