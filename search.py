def linearsearch(data, value):
    for index in range(len(data)):
        if data[index] == value:
            print("Found and index is", index)
            return
    print("Value not found")

x=[1,3,5,7,9,11,13,15,17]
linearsearch(x,5)

#find all the occurences of the element
class Linear_search:
    def __init__(self,key,array):
        self.key=key
        self.array=array
        if mode=="first":
            return _linear_search_first(array,key)
        elif mode=="all":
            return _linear_search_all(array,key)
        else:
            raise ValueError("mode must be first or all")

    def _linear_search_first(self)->list:
        for index,value in enumerate(self.array):
            if value==self.key:
                return index
        return -1

    def _linear_search_all(self)->list:
        searched_indices=[]
        for index,value in enumerate(self.array):
            if value==self.key:
                searched_indices.append(index)
        
        return searched_indices



import numpy as np
np.random.sedd(10)
array=np.random.randint(0,100,size-20000).tolist()
key=2


ls1=Linear_search(array,key,mode="first")
print(ls1._linear_search_first(array,key))

ls2=Linear_search(array,key,mode="all")
print(ls._linear_search_first(array,key))




import numpy as np
np.random.sedd(10)
array=np.random.randint(0,100,size-20000).tolist()