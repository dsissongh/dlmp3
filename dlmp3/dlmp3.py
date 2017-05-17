import cherrypy

from func import dlmp3
from func import checkconvert
from func import getmedia



isinstalled = checkconvert('ffmpeg')
if "error" in isinstalled:
	print("Need to install ffmpeg")
	exit()

cherrypy.quickstart(dlmp3())

url = "https://www.youtube.com/watch?v=bamLHzEPm6U"
executable = 'youtube-dl'
#getmedia(executable, url)

