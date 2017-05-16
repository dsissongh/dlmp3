import unittest

from dlmp3 import func

class func_testcase(unittest.TestCase):
	""" Tests for `func.py` """

	def test_checkconvert_returns_true(self):
		"""Is five successfully determined to be prime?"""
		self.assertTrue(checkconvert('youtube-dl'))

if __name__ == '__main__':
	unittest.main()