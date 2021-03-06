import cherrypy
import subprocess
from subprocess import call
import os

class dlmp3(object):

	@cherrypy.expose
	def index(self):
		return "Hello World!"

	@cherrypy.expose
	def get(self):
		return "get method"

def checkconvert(executable):
	path2file = os.path.dirname(__file__) + "\\" + executable
	print(path2file)
	if os.path.isfile(path2file):
		return True
	else:
		return False

def checkconvert_dep(executable):
	''' see if "executable" is installed '''
	try:
		devnull = open(os.devnull)
		subprocess.Popen([executable], stdout=devnull, stderr=devnull).communicate()
		return ""
	except OSError as e:
		if e.errno == os.errno.ENOENT:
			return "error"
		else:
			# Something else went wrong while trying to run the executable
			raise

def getmedia(executable, url):

	param1 = url
	param2 = "-x"
	param3 = "--audio-format"
	param4 = "mp3"
	param5 = "--output"
	param6 = '"../mp3/%(title)s.%(ext)s"'
	param7 = "-k"
	call([executable, param1, param2, param3, param4, param5, param6, param7])
	return