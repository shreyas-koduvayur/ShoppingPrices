import csv

fileName = 'e-shop clothing 2008.csv'
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
            order_id = i[0]
            country = i[1]
            page = i[2]
            prices.append((price, click, order_id, country, page))
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

#start the timer
startMax = time.time();

# Build max heap
maxHeap = MaxHeap()
for price, click, order_id, country, page in prices:
    maxHeap.insert((price, click, order_id, country, page))

#end timer
endMax = time.time();
maxTime = startMin-endMin;

# Find the most expensive purchase and its clicks
if maxHeap.heap:
    maxPrice, maxClicks, order_id, country, page = maxHeap.extractMax()
else:
    maxPrice, maxClicks = None, None, None, None, None

class MinHeap:
    def __init__(self):
        self.heap=[]

    def insert(self,val):
        self.heap.append(val)
        self.bubbleUp(len(self.heap)-1)

    def extractMin(self):
        if len(self.heap) ==0:
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
            
#start the timer
startMin = time.time();

minHeap=MinHeap()
for price, click, order_id, country, page in prices:
    minHeap.insert((price, click, order_id, country, page))

# end timer
endMin = time.time();
minTime = startMin - endMin;

if minHeap.heap:
    minPrice, minClicks, order_id, country, page = minHeap.extractMin()
else:
    minPrice, minClicks=None, None, None, None, None
