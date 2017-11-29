import math
import sys


class Slover(object):
    def demo(self, a, b, c):
        print(str(sys.argv),len(sys.argv))
        d = b ** 2 - 4 * a * c
        if d > 0:
            disc = math.sqrt(d)
            root1 = (-b + disc) / (2 * a)
            root2 = (-b - disc) / (2 * a)
            print(root1, root2)
            print(disc)
            return root1, root2
        else:
            raise Exception

def my_print(args):
    print args

def move(n, a, b, c):
       my_print ((a, '-->', c)) if n==1 else (move(n-1,a,c,b) or move(1,a,b,c) or move(n-1,b,a,c))
#    if n == 1
#        my_print((a, '-->', c))
 #   else
 #       (move(n - 1, a, c, b) or move(1, a, b, c) or move(n - 1, b, a, c))

move (3, 'a', 'b', 'c')
Slover().demo(3, 6, -5)
