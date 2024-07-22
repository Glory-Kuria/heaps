# def heapify(arr, N, i):
#     largest = i 
#     l = 2 * i + 1   
#     r = 2 * i + 2     
#     if l < N and arr[largest] < arr[l]:
#         largest = l

#     if r < N and arr[largest] < arr[r]:
#         largest = r

#     if largest != i:
#         arr[i], arr[largest] = arr[largest], arr[i] 

#         heapify(arr, N, largest)


# def heapSort(arr):
#     N = len(arr)

#     for i in range(N//2 - 1, -1, -1):
#         heapify(arr, N, i)

#     for i in range(N-1, 0, -1):
#         arr[i], arr[0] = arr[0], arr[i]  
#         heapify(arr, i, 0)



# if __name__ == '__main__':
#     arr = [12, 11, 13, 5, 6, 7]


#     heapSort(arr)
#     N = len(arr)

#     print("Sorted array is")
#     for i in range(N):
#         print("%d" % arr[i], end=" ")



def partition(array, low, high):
    last_element = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= last_element:
            i = i + 1

            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

def quicksort(array, low, high):
    if low < high:

        pi = partition(array, low, high)
        quicksort(array, low, pi - 1)
        quicksort(array, pi + 1, high)

if __name__ == '__main__':
    array = [1, 5, 7, 11, 12, 13]
    N = len(array)
    
    quicksort(array, 0, N - 1)
    print('Sorted array:')
    for x in array:
        print(x, end=" ")
        
        
        
class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2
    
    def left_child(self, i):
        return 2 * i + 1
    
    def right_child(self, i):
        return 2 * i + 2
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)
    
    def heapify_up(self, i):
        while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
            self.swap(i, self.parent(i))
            i = self.parent(i)
    
    def heapify_down(self, i):
        smallest = i
        left = self.left_child(i)
        right = self.right_child(i)
        
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
            
        if smallest != i:
            self.swap(i, smallest)
            self.heapify_down(smallest)
    
    def extract_min(self):
        if len(self.heap) == 0:
            return None
        
        min_element = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify_down(0)
        
        return min_element
    
    def get_min(self):
        if len(self.heap) > 0:
            return self.heap[0]
        return None


heap = MinHeap()
heap.insert(3)
heap.insert(2)
heap.insert(1)
heap.insert(5)
heap.insert(4)

print("Min heap elements:")
while len(heap.heap) > 0:
    print(heap.extract_min())
