import random
import time
import timeit
import unittest

from ch2.InsertionSort import InsertionSort
from ch2.SelectionSort import SelectionSort

class TestSort(unittest.TestCase):
	def testInsertionSort(self):
		self._testSort(InsertionSort)

	def testSelectionSort(self):
		self._testSort(SelectionSort)

	def genRandomList(self, length):
		return [ random.randint(1, 100) for _ in xrange(length)]

	def _testSort(self, sorterClass):
		print '====================================================================================================='
		for length in (1000, 2000, 4000, 8000, 10000, 100000, 1000000):
			if length >= 5000 and sorterClass in (InsertionSort, SelectionSort):
				continue

			list = self.genRandomList(length)
			t0 = time.time()
			sorterClass(list).sort()
			dt = time.time() - t0
			self.checkSorted(list)
			print '%s sort on %d nums => %fus' % (sorterClass.__name__, length, dt * 10000000)

	def checkSorted(self, list):
		lastVal = None
		for v in list:
			if lastVal is not None:
				assert v >= lastVal

			lastVal = v


if __name__ == '__main__':
	unittest.main()
