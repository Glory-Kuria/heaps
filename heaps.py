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
    
    
def find_k_closest_points(points, k):
   
    distances = [(point[0]**2 + point[1]**2)**0.5 for point in points]
    
   
    zipped_points = zip(points, distances)
    
    
    sorted_points = sorted(zipped_points, key=lambda x: x[1])
    
 
    k_closest_points = [point[0] for point in sorted_points[:k]]
    
    return k_closest_points


points = [(3, 4), (-1, -5), (2, 2), (7, 8)]
k = 2
print(find_k_closest_points(points, k))


from collections import Counter

def find_k_most_frequent_elements(nums, k):
    
    freq_counter = Counter(nums)
    
  
    most_common = freq_counter.most_common(k)
    
  
    most_frequent_elements = [element for element, _ in most_common]
    
    return most_frequent_elements


nums = [3, 1, 4, 4, 5, 2, 6, 1]
k = 2
print(find_k_most_frequent_elements(nums, k))


# def build_max_heap(arr):
#     def heapify(arr, n, i):  # Helper function to heapify subtree rooted at index i
#         largest = i  # Initialize largest as root
#         left = 2 * i + 1     # left = 2*i + 1
#         right = 2 * i + 2    # right = 2*i + 2
        
#         # Check if left child exists and is greater than root
#         if left < n and arr[i] < arr[left]:
#             largest = left
            
#         # Check if right child exists and is greater than largest so far
#         if right < n and arr[i] > arr[right]:
#             largest = i
            
def max_heapify(arr, n, i):
    largest = i    
    left = 2 * i + 1   
    right = 2 * i + 2
  
    
    if left < n and arr[i] < arr[left]:
        largest = left
  
    
    if right < n and arr[largest] < arr[right]:
        largest = right
  
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  
  
      
        max_heapify(arr, n, largest)

def build_max_heap(arr):
    n = len(arr)
    
    for i in range(n//2 - 1, -1, -1):
        max_heapify(arr, n, i)

arr = [4, 10, 3, 5, 1]
build_max_heap(arr)
print("Max heap:", arr)


def minMeetingRooms(meetings):
    if not meetings:
        return 0
    
    start_times = sorted([m[0] for m in meetings])
    end_times = sorted([m[1] for m in meetings])
    
    num_rooms = 0
    end_index = 0
    
    for i in range(len(meetings)):
        if start_times[i] < end_times[end_index]:
            num_rooms += 1
        else:
            end_index += 1
    
    return num_rooms


meetings = [(0, 30), (5, 10), (15, 20)]
print(minMeetingRooms(meetings))  


import heapq

def findKLargestElements(arr, k):
   
    if k > len(arr) or k <= 0:
        return []
    
  
    min_heap = []
    
 
    for num in arr:
      
        heapq.heappush(min_heap, num)
        
       
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    
    
    result = []
    while min_heap:
        result.append(heapq.heappop(min_heap))
    
    
    result.reverse()
    
    return result


arr = [3, 10, 4, 7, 15]
k = 3
print(findKLargestElements(arr, k))  


def findKLargestElements(arr, k):
   
    if k > len(arr) or k <= 0:
        return []
    
    sorted_arr = sorted(arr, reverse=True)
    
    
    return sorted_arr[:k]


arr = [3, 10, 4, 7, 15]
k = 3
print(findKLargestElements(arr, k))  


