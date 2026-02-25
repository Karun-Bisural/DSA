class LinearProbingTable:
    def __init__(self,size):
        self.size=size
        self.table=[None]*size
        
    def insert(self,key):
        index=key%self.size
        for i in range(self.size):
            prob_idx=(index + i) % self.size
            if self.table[prob_idx] is None:
                self.table[prob_idx] = key
                return True
        return False

    def search(self,key):
        index = key % self.size
        for i in range(self.size):
            prob_idx=(index+i)%self.size
            if self.table[prob_idx] == key:
                return prob_idx
            if self.table[prob_idx] is None:
                break
        return -1

if __name__ == "__main__":
    lp_table=LinearProbingTable(10)
    lp_table.insert(12)
    lp_table.insert(22)
    print(f"Linear Probing: 22 found at index{lp_table.search(22)}")

#quadratic probing
class QuadraticProbingTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        def insert(self, key):
        hash_val = key % self.size
        for i in range(self.size):
            idx = (hash_val + i * i) % self.size
            if self.table[idx] is None:
                self.table[idx] = key
                return True
        return False

    def search(self, key):
        hash_val = key % self.size
        for i in range(self.size):
            idx = (hash_val + i * i) % self.size
            if self.table[idx] == key:
                return idx
            if self.table[idx] is None:
                break
        return -1
             
# Example Usage:
if __name__ == "__main__":
    qp_table = QuadraticProbingTable(10)
    qp_table.insert(15)
    qp_table.insert(25) # Collision
    print(f"Quadratic Probing: 25 found at index {qp_table.search(25)})


#double hashing
class DoubleHashingTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
    def _hash2(self, key):
    # Secondary hash must never return 0 and should be
        return 7 - (key % 7)
        def _hash2(self, key):
        # Secondary hash must never return 0 and should be
        return 7 - (key % 7)
    
    def insert(self, key):
        h1 = key % self.size
        step = self._hash2(key)
        for i in range(self.size):
            idx = (h1 + i * step) % self.size
            if self.table[idx] is None:
                self.table[idx] = key
                return True
        return False
    
    def search(self, key):
        h1 = key % self.size
        step = self._hash2(key)
        for i in range(self.size):
            idx = (h1 + i * step) % self.size
            if self.table[idx] == key:
                return idx
            if self.table[idx] is None:
                break
        return -1
# Example Usage:
if __name__ == "__main__":
    dh_table = DoubleHashingTable(10)
    dh_table.insert(10)
    dh_table.insert(20) # Collision
    print(f"Double hashing table:index found at {dh_table.search(20)}")


#seperate chaining
class SeparateChainingTable:
    def __init__(self, size):
        self.size = size
        self.table =[None]*size
        def insert(self, key):
        index = key % self.size
        if key not in self.table[index]:
            self.table[index].append(key)
    
    def search(self, key):
        index = key % self.size
        return key in self.table[index]
# Example Usage:
if __name__ == "__main__":
    sc_table = SeparateChainingTable(5)
    sc_table.insert(10)
    sc_table.insert(15) # Both hash to index 0
    print(f"Separate Chaining: 15 found? {sc_table.search(1)}")