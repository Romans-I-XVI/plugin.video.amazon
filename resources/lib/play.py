#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import time
import urllib
import demjson
import xbmcplugin
import xbmc
import xbmcaddon
import xbmcgui
import os
import subprocess
import resources.lib.common as common
import urllib2

from BeautifulSoup import BeautifulStoneSoup
from BeautifulSoup import BeautifulSoup
try:
    from xml.etree import ElementTree
except:
    from elementtree import ElementTree
settings = xbmcaddon.Addon( id = 'plugin.video.amazon' )
amazonscript = os.path.join( settings.getAddonInfo( 'path' ), 'amazonscript' )
osLinux = xbmc.getCondVisibility('system.platform.linux')
osOsx = xbmc.getCondVisibility('system.platform.osx')

def PLAYVIDEO():
	xbmc.Player().stop()
	dialog = xbmcgui.Dialog()
	ok = True
	kiosk='yes'
	if settings.getSetting("kiosk") == 'false':
		kiosk='no'
	url=common.args.url
	load_extension='--load-extension='+amazonscript+'" "'
	finalUrl=url.replace("http://www.amazon.com/gp/product/","http://www.amazon.com/gp/video/streaming/mini-mode.html?ie=UTF8&asin=")
	if settings.getSetting("HD") == 'true':
		try:
			req = urllib2.Request(url)
        		req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        		response = urllib2.urlopen(req)
        		link=response.read()
        		response.close()
			match=re.compile('<a href="/gp/product/(.+?)/.+?">Also available in HD</a>').findall(link)
			finalUrl='http://www.amazon.com/gp/video/streaming/mini-mode.html?ie=UTF8&asin='+match[0]
		except:pass
	xbmc.executebuiltin("RunPlugin(plugin://plugin.program.chrome.launcher/?url="+urllib.quote_plus(load_extension+finalUrl)+"&mode=showSite&kiosk="+kiosk+")")
	if osLinux:
        	try:
            		xbmc.sleep(10000)
           		subprocess.Popen('xdotool mousemove 9999 0 click 1', shell=True)
            		xbmc.sleep(5000)
            		subprocess.Popen('xdotool mousemove 9999 0 click 1', shell=True)
            		xbmc.sleep(5000)
            		subprocess.Popen('xdotool mousemove 9999 0 click 1', shell=True)
            		xbmc.sleep(5000)
            		subprocess.Popen('xdotool mousemove 9999 0 click 1', shell=True)
        	except:
            		pass
	if osOsx:
		try:
			xbmc.sleep(10000)
			subprocess.Popen('cliclick c:500,500', shell=True)
            		xbmc.sleep(5000)
            		subprocess.Popen('cliclick c:500,500', shell=True)
            		xbmc.sleep(5000)
            		subprocess.Popen('cliclick c:500,500', shell=True)
            		xbmc.sleep(5000)
            		subprocess.Popen('cliclick c:500,500', shell=True)
        	except:
            		pass
