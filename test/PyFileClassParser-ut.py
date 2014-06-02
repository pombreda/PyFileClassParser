import unittest
import random
import sys

sys.path.append('../')

from PyFileClassParser import CodeAnalysis
from FileWalker import FileWalker
import os

class TestSequence(unittest.TestCase):

        def setUp(self):
                self.name = 'Kinder'
                self.analysis = CodeAnalysis(self.name)
                self.exportDir = 'exportCsv'
                self.exportFile = 'export.csv'

        def tearDown(self):
                del self.analysis
                if os.path.exists(self.exportDir):
                        os.rmdir(self.exportDir)
                if os.path.exists(self.exportFile):
                        os.remove(self.exportFile)

        def test_definedNameMatches(self):
                self.assertEqual(self.name, self.analysis.name)

        def test_FileCLassOtherNotSupported(self):
                # self.assertRaises(TypeError, self.analysis.extAdd('other', ['.tar.gz', '.zip']))
                pass

        def test_nonExistingDirIsCreated(self):
                self.analysis.extAdd('source', ['.c', '.C', '.cc', '.h', '.CC', '.py'])
                self.folder = FileWalker(name='Broadcom SDK', pathToFolder='./')
                self.analysis.folderAdd(self.folder)
                self.assertTrue(self.analysis.export2File(mode='csv', name=self.exportFile, dirname=self.exportDir))
                self.assertTrue(os.path.exists(self.exportDir))
                pass

        def test_folderAdd(self):

                # declare own file classes, everything else will be counted as OTHER
                self.analysis.extAdd('source', ['.c', '.C', '.cc', '.h', '.CC', '.py'])
                self.analysis.extAdd('make', ['.in', '.am', '.mk'])
                self.analysis.extAdd('script', ['.sh'])
                self.analysis.extAdd('doc', ['.pdf', '.txt', '.doc'])
                self.analysis.extAdd('container', ['.tar.gz', '.zip'])
                self.analysis.extAdd('fpga-code', ['.vhdl', '.v'])
                self.analysis.extAdd('images', ['.iso', '.bin'])

                self.folder = FileWalker(name='Broadcom SDK', pathToFolder='./')

                self.analysis.folderAdd(self.folder)

                print self.analysis


if __name__ == "__main__":
    unittest.main()
