#!/bin/python
import unittest
import what_time
from what_time import gauss

class TestOutputs(unittest.TestCase):

    def test_graph(self):
        for i in range(-43200, 43200, 10):
            (r,g,b)=gauss(i)
            print ("%i %i %i %i" % (i,r,g,b) )

    def test_midpoint(self):
        i=0
        (r,g,b)=gauss(i)
        print ("RGB at midpoint: %i %i %i %i" % (i,r,g,b) )
        self.assertGreater(r,150)
        self.assertGreater(g,150)
        self.assertGreater(b,150)

if __name__ == '__main__':
    unittest.main()
