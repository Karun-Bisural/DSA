class Linear_search:
    def __init__(self, array, key, mode):
        self.key = key
        self.array = array
        self.mode = mode

    def _linear_search_first(self):
        for index, value in enumerate(self.array):
            if value == self.key:
                return index
        return -1

    def _linear_search_all(self):
        searched_indices = []
        for index, value in enumerate(self.array):
            if value == self.key:
                searched_indices.append(index)
        return searched_indices


import numpy as np
np.random.seed(10)
array=np.random.randint(0,100,size=20000).tolist()
key=2

ls1 = Linear_search(array, key, mode="first")
print(ls1._linear_search_first())

ls2 = Linear_search(array, key, mode="all")
print(ls2._linear_search_all())
