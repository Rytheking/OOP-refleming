import random
class Sort:
    def makeArr(self,seed,len):
        random.seed(seed)
        arr = [random.randint(0,999999999999999) for _ in range(len)]
        return arr
    def sort(arr):
        pass
    def template_method(self,arr):
        self.sort(arr)
        return arr
class quickSort(Sort):
    def partition(self,arr,low,high):
        i=low-1
        pivot=arr[high]
        for j in range(low, high):
            if arr[j]<=pivot:
                i=i+1
                arr[i],arr[j]=arr[j],arr[i]
        arr[i+1],arr[high]=arr[high],arr[i+1]
        return i+1
    def quickSort(self,arr,low,high):
        if len(arr)==1:
            return arr
        if low<high:
            pi=self.partition(arr,low,high)

            self.quickSort(arr,low,pi-1)
            self.quickSort(arr,pi+1,high)
    def sort(self,arr):
        self.quickSort(arr,0,len(arr)-1)
        return arr

class bubbleSort(Sort):
    def sort(self,arr):
        for i in range(len(arr)-1):
            for j in range(0, len(arr)-i-1):
                if arr[j] > arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
        return arr

class insertionSort(Sort):
    def sort(self,arr):
        for i in range(1,len(arr)):
            key = arr[i]
            j = i-1
            while(j>=0 and key<arr[j]):
                arr[j+1]=arr[j]
                j -= 1
            arr[j+1]=key
        return arr

def doit(sort_method: Sort):
    return sort_method.template_method(sort_method.makeArr(10,10))
def testit(sort_method: Sort, seed, len):
    return sort_method.template_method(sort_method.makeArr(seed,len))

doit(insertionSort())
doit(bubbleSort())
doit(quickSort())



