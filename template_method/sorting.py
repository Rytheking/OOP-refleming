class Sort:
    def template_method(self):
        print(self.__class__)
        arr = [10,20,1,25,44,68,0,89,74,4,2,3,3,3,3,3,420,69,73,49,452,2542,1,34,8,6,52]
        print(arr)
        self.sort(arr)
        print(arr)
    def sort(arr):
        pass
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

class bubbleSort(Sort):
    def sort(self,arr):
        for i in range(len(arr)-1):
            for j in range(0, len(arr)-i-1):
                if arr[j] > arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
class insertionSort(Sort):
    def sort(self,arr):
        for i in range(1,len(arr)):
            key = arr[i]
            j = i-1
            while(j>=0 and key<arr[j]):
                arr[j+1]=arr[j]
                j -= 1
            arr[j+1]=key
def doit(sort_method: Sort) -> None:
    sort_method.template_method()

doit(insertionSort())
doit(bubbleSort())
doit(quickSort())

