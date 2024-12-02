import csv

fileName = 'data.csv'
prices = []
clicks = []

# Read file and save prices and clicks in lists
with open(fileName, 'r') as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)
    for i in reader:
        try:
            price = float(i[11])
            click = int(i[4])
            prices.append((price, click))
        except (ValueError, IndexError):
            continue

# Build maxheap
class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self.bubbleUp(len(self.heap) - 1)

    def extractMax(self):
        if len(self.heap) == 0:
            return None
        elif len(self.heap) == 1:
            return self.heap.pop()

        maxVal = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapifyDown(0)
        return maxVal

    def bubbleUp(self, i):
        parent = (i - 1) // 2
        while i > 0 and self.heap[i][0] > self.heap[parent][0]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = (i - 1) // 2

    def heapifyDown(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i

        if left < len(self.heap) and self.heap[left][0] > self.heap[largest][0]:
            largest = left
        if right < len(self.heap) and self.heap[right][0] > self.heap[largest][0]:
            largest = right
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.heapifyDown(largest)

# Build max heap
maxHeap = MaxHeap()
for price, click in prices:
    maxHeap.insert((price, click))

# Find the most expensive purchase and its clicks
if maxHeap.heap:
    maxPrice, maxClicks = maxHeap.extractMax()
else:
    maxPrice, maxClicks = None, None

#I am storing my maxPrice and maxClicks here. Everytime the button is pushed, line 66 needs to be run again. Other than that, everything else should work. Lmk if I need to make any changes.
class MinHeap:
    def __init__(self):
        self.heap=[]

    def insert(self,val):
        self.heap.append(val)
        self.bubbleUp(len(self.heap)-1)

    def extractMin(self):
        if len(self.heap)==0:
            return None
        if len(self.heap)==1:
            return self.heap.pop()
        val=self.heap[0]
        self.heap[0]=self.heap.pop()
        self.heapifyDown(0)
        return val
    def bubbleUp(self,index):
        parent=(index-1)//2
        while index>0 and self.heap[index][0]<self.heap[parent][0]:
            self.heap[index],self.heap[parent]=self.heap[parent], self.heap[index]
            index=parent
            parent=(index-1)//2


    def heapifyDown(self,index):
        smallest=index
        left= 2*index +1
        right=2 * index +2
        if left<len(self.heap) and self.heap[left][0] <self.heap[smallest][0]:
            smallest=left
        if right<len(self.heap) and self.heap[right][0]<self.heap[smallest][0]:
            smallest=right
        if smallest!= index:
            self.heap[index],self.heap[smallest]=self.heap[smallest],self.heap[index]
            self.heapifyDown(smallest)


minHeap=MinHeap()
for price, click in prices:
    minHeap.insert((price,click))

if minHeap.size()>0:
    minPrice, minClicks= minHeap.extractMin()
else:
    minPrice, minClicks=None, None
