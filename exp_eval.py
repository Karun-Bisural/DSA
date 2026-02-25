class Arithmetic:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        '''
       adds two number
       parameter a  = int
       parameter b  = int
        '''
        return self.a + self.b

#test execution   
if __name__=="__main__":
    arim =Arithmetic(3,5)
    print(arim.add())

arim =Arithmetic(3,4)
print(arim.add())