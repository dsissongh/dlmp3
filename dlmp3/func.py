import subprocess
import os

def checkconvert(executable):
	try:
		devnull = open(os.devnull)
		subprocess.Popen([executable], stdout=devnull, stderr=devnull).communicate()
		return
	except OSError as e:
		if e.errno == os.errno.ENOENT:
			print("error")
			# handle file not found error.
		else:
			# Something else went wrong while trying to run `wget`
			raise