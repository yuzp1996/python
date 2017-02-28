import unittest, my_math

class ProductTestCase(unittest, TestCase):

    def testIntergers(self):
        for x in xrange(-10, 10):
            for y in xrange(-10, 10):
                p = my_math.product(x, y)
                self.failUnless(p == x*y, 'Integer multiplication filed')

    def testFloats(self):
        for x in xrange(-10, 10):
            for y in xrange(-10, 10):
                x = x/10.0
                y = y/10.0
                p = mymath.product(x, y)
            self.failUnless(p== x*y, 'Float multiplication failed')
if __name__ == '__main__': unittest.main()
 
