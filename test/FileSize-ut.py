"""
unit test for class: FileSize
"""


import unittest
import random
import sys

sys.path.append('../')

import FileSize

class TestSequence(unittest.TestCase):

        def setUp(self):
                self.FileSize1 = FileSize.FileSize('B')
                self.FileSize2 = FileSize.FileSize('B')
                self.assertEqual(0, self.FileSize1.value)
                self.assertEqual(0, self.FileSize2.value)

        def tearDown(self):
                del self.FileSize1
                del self.FileSize2

        def test_checkFunctionSet(self):
                self.FileSize1.set(200)
                self.assertEqual(200, self.FileSize1.get())

        def test_checkFunctionEqual(self):
                self.FileSize1.set(200)
                self.assertFalse(self.FileSize1 == self.FileSize2)
                self.FileSize2.set(200)
                self.assertTrue(self.FileSize1 == self.FileSize2)
                self.assertTrue(self.FileSize1 == 200)
                self.assertFalse(self.FileSize1 == 201)         

        def test_checkFunctionLessThan(self):
                self.FileSize1.set(200)
                self.FileSize2.set(201)
                self.assertTrue(self.FileSize1 < 201)
                self.assertFalse(self.FileSize1 < 200)
                self.assertTrue(self.FileSize1 < self.FileSize2)
                self.assertFalse(self.FileSize2 < self.FileSize1)

        def test_checkFunctionGreaterThan(self):
                self.FileSize1.set(200)
                self.FileSize2.set(201)
                self.assertTrue(self.FileSize1 > 199)
                self.assertFalse(self.FileSize1 > 200)
                self.assertTrue(self.FileSize2 > self.FileSize1)
                self.assertFalse(self.FileSize1 > self.FileSize2)

        def test_checkOperatorAddEqual(self):
                self.FileSize1.set(200)
                self.FileSize2.set(21)
                self.assertEqual(200, self.FileSize1.get())
                self.assertEqual(21, self.FileSize2.get())
                
                self.FileSize1.add(20)
                self.assertEqual(220, self.FileSize1.get())
                self.FileSize1.add(self.FileSize2)
                self.assertEqual(241, self.FileSize1.get())

        def test_clearContent(self):
                self.FileSize1.set(200)
                self.assertEqual(200, self.FileSize1.get())

                self.FileSize1.clear()
                self.assertEqual(0, self.FileSize1.get())


if __name__ == "__main__":
    unittest.main()
