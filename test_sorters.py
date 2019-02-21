from unittest import TestCase
from pprint import pprint
import random

#
# Run with:
#   python -m unittest test_sorters


class SortTestCase(TestCase):
    '''Unit tests for the three sort functions'''
    LETTERS = 'abcdefghijklmnopqrstuvwxyz'

    def setUp(self):
        '''Set up the test: called before *each* test function'''
        # we generate list of tuples of random data to be used.
        self.data = []
        for i in range(10):
            self.data.append((
                ''.join((random.choice(self.LETTERS)
                         for i in range(10))),  # 10 random letters
                # an integer
                random.randint(0, 100),
                # a float
                round(random.uniform(0.0, 100.0), 1),
            ))

    def debugPrint(self):
        '''Helper method during debugging the tests'''
        pprint(self.data)
        print('')

    def iterPairs(self):
        '''
        Iterates the data list, yielding each sequential pair or rows:
            ( self.data[0], self.data[1] ),
            ( self.data[1], self.data[2] ),
            ...
        '''
        last = None
        for item in self.data:
            if last is not None:
                yield (last, item)
            last = item

    def test_bubble_sort_ascending(self):
        from sorters import bubble_sort
        idx = 1
        bubble_sort(self.data, idx)

        for a, b in self.iterPairs():
            self.assertLessEqual(a[idx], b[idx],
                                 msg='previous {} should be less than current {} at index {}'.format(a, b, idx))

    def test_bubble_sort_descending(self):
        from sorters import bubble_sort
        idx = 0
        bubble_sort(self.data, idx, True)

        for a, b in self.iterPairs():
            self.assertGreaterEqual(a[idx], b[idx],
                                    msg='previous {} should be greater than current {} at index {}'.format(a, b, idx))

    def test_bubble_sort_percentage(self):
        from sorters import bubble_sort
        idx = 2
        bubble_sort(self.data, idx, True)

        for a, b in self.iterPairs():
            self.assertGreaterEqual(a[idx], b[idx],
                                    msg='previous {} should be greater than current {} at index {}'.format(a, b, idx))

    def test_insertion_sort_asc(self):
        from sorters import insertion_sort
        idx = 1
        insertion_sort(self.data, idx)

        for a, b in self.iterPairs():
            self.assertLessEqual(a[idx], b[idx],
                                 msg='previous {} should be less than current {} at index {}'.format(a, b, idx))

    def test_insertion_sort_desc(self):
        from sorters import insertion_sort
        idx = 1
        insertion_sort(self.data, idx, True)

        for a, b in self.iterPairs():
            self.assertGreaterEqual(a[idx], b[idx],
                                    msg='previous {} should be greater than current {} at index {}'.format(a, b, idx))

    def test_selection_sort_desc(self):
        from sorters import selection_sort
        idx = 1
        selection_sort(self.data, idx, True)

        for a, b in self.iterPairs():
            self.assertGreaterEqual(a[idx], b[idx],
                                    msg='previous {} should be greater than current {} at index {}'.format(a, b, idx))

    def test_selection_sort_asc(self):
        from sorters import selection_sort
        idx = 1
        selection_sort(self.data, idx)

        for a, b in self.iterPairs():
            self.assertLessEqual(a[idx], b[idx],
                                 msg='previous {} should be less than current {} at index {}'.format(a, b, idx))
