import unittest

from sorting import *

class SortTest(unittest.TestCase):
    def testQuickSort(self):
        seed=112
        length=20
        random.seed(seed)
        arr = [random.randint(0,999999999999999) for _ in range(length)]
        arr.sort()
        self.assertEqual(arr,testit(quickSort(),seed,length))
    def testInsertionSort(self):
        seed=112
        length=20
        random.seed(seed)
        arr = [random.randint(0,999999999999999) for _ in range(length)]
        arr.sort()
        self.assertEqual(arr,testit(insertionSort(),seed,length))
    def testBubbleSort(self):
        seed=112
        length=20
        random.seed(seed)
        arr = [random.randint(0,999999999999999) for _ in range(length)]
        arr.sort()
        self.assertEqual(arr,testit(bubbleSort(),seed,length))


if __name__ == '__main__':
    unittest.main()


