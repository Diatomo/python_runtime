import unittest
import os
import sys
from main import PathFinder

class TestDirPy(unittest.TestCase):
   
    def search(self, path):
        test = []
        for dirpath, dirnames, files in os.walk(os.path.abspath(path)):
            for doc in files:
                test.append(doc)
        return test

    def testPathConstructor(self):
        path = './'
        self.assertIsNotNone(PathFinder(path), "pathfinder failed to construct")

    def testPathSearchAll(self):
        path = './testDir/'
        pf = PathFinder(path)
        f = None
        s = None

        test = self.search('./testDir/')
        files = pf.search(f,s)
        self.assertEqual(len(test), len(files), "all files were not found")


    def testPathSearchFile(self):
        #pathfinder attributes
        path = './testDir/'
        pf = PathFinder(path)
        f = 'mp3'
        s = None

        test = self.search('./testDir/Media')
        files = pf.search(f,s)
        self.assertEqual(len(test), len(files), "all .mp3 files were not found")

    def testPathSearchDogFile(self):
        #pathfinder attributes
        path = './testDir/'
        pf = PathFinder(path)
        f = 'dog'
        s = None

        test = self.search('./testDir/Dogs')
        files = pf.search(f,s)
        self.assertEqual(len(test), len(files), "all dog files were not found")
    
    def testPathSearchPlantFile(self):
        #pathfinder attributes
        path = './testDir/'
        pf = PathFinder(path)
        f = 'plant'
        s = None

        test = self.search('./testDir/Plants')
        files = pf.search(f,s)
        self.assertEqual(len(test), len(files), "all plant files were not found")

    def testPathSearchSize(self):
        path = './testDir/'
        pf = PathFinder(path)
        f = None
        s = 60000

        test = self.search('./testDir/Media')
        files = pf.search(f,s)
        self.assertEqual(len(test), len(files), "all size > 6000 files were not found")

    def testPathSearchSizeOne(self):
        path = './testDir/'
        pf = PathFinder(path)
        f = None
        s = 1

        test = 9 #hardcoded if files are added for more test cases CHANGE THIS
        files = pf.search(f,s)
        self.assertEqual(test, len(files), "all size > 1 files were not found")
    
    def testPathSearchSizeZero(self):
        path = './testDir/'
        pf = PathFinder(path)
        f = None
        s = 0

        test = self.search('./testDir')
        files = pf.search(f,s)
        self.assertEqual(len(test), len(files), "all size > 0 files were not found")


    def testPathSearchSizeNegative(self):
        path = './testDir/'
        pf = PathFinder(path)
        f = None
        s = -1

        test = self.search('./testDir')
        files = pf.search(f,s)
        self.assertEqual(len(test), len(files), "all size > -1 files were not found")

if __name__ == '__main__':
    unittest.main()
