import sys
from collections import deque

absq = deque([0])

class absh:
    def __init__(self):
        self.count = 0
    
    def insert(self, data):
        if  self.count == 0:
            absq.append(data)
            self.count += 1
        else:
            temp = data
            absq.append(temp)
            self.count += 1

            child = self.count
            parent = child // 2

            while child != 1 :
                if abs(temp) < abs(absq[parent]) or (abs(temp) == abs(absq[parent]) and temp < 0 and absq[parent] > 0):
                    absq[child] = absq[parent]
                    child = parent
                    parent = parent // 2
                else :
                    break

            absq[child] = temp
    
    def hpop(self):
        if self.count == 0:
            return 0
        
        data = absq[1]
        temp = absq[self.count]
        absq.pop()
        self.count -= 1

        if self.count == 0:
            return data

        parent = 1
        child = 2

        while child <= self.count and self.count > 1:
            if child < self.count :
                if abs(absq[child]) > abs(absq[child+1]) or (abs(absq[child] == abs(absq[child+1]) and absq[child+1] < 0 and absq[child] > 0)):
                    child += 1
            if abs(temp) < abs(absq[child]) or (abs(temp) == abs(absq[child]) and temp < 0): return data
            
            absq[parent] = absq[child]
            parent = child
            child *= 2
        
        absq[parent] = temp

        return data

            

if __name__ == '__main__':
    N = int(sys.stdin.readline())

    heap = absh()

    for i in range(N):
        a = int(sys.stdin.readline())

        if a == 0:
            print(heap.hpop())
        else:
            heap.insert(a)