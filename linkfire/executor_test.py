import unittest

from loaders import NetflixLoader
from gender_detector import GenderUpdater
from executor import Search

class ExecutorTestCase(unittest.TestCase):

	def setUp(self):
		self.search = Search()
		nl = NetflixLoader()
		nl.create_tables()
		nl.load_csv()
		
		# gu = GenderUpdater()		
		# gu.update_gender()

	def test_common_first_name(self):
		self.assertEqual(self.search.common_first_name('male'), 'David')
		self.assertEqual(self.search.common_first_name('female'), 'Kate')
		
	def test_longest_timespan(self):
		self.assertEqual(self.search.longest_timespan(), 
						 'Pioneers: First Women Filmmakers*')

	def test_month_most_new_releases(self):
		self.assertEqual(self.search.month_most_new_releases(), 12)
	
	def test_largest_increase(self):
		self.assertEqual(self.search.largest_increase(), 2019)

	def test_actresses_woody_harrelson(self):
		self.assertEqual(self.search.actresses_woody_harrelson(), 
						[('Thandie Newton',), ('Emilia Clarke',)])
	
if __name__ == '__main__':
	unittest.main()