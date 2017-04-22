import subprocess
from subprocess import call
import os

def checkconvert(executable):
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
	param6 = '"./mp3/%(title)s.%(ext)s"'
	param7 = "-k"
	call([executable, param1, param2, param3, param4, param5, param6, param7])
	return