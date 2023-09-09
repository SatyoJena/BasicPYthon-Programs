#implemeting dynamic arrays

# Trying to implement a C like array
class Array:
    def __init__(self, len ):
        if (len >0):
            self.len = len
            self.array = [0]*len # a fixed memory allocated
        else:
            print("Length of array must be a positive integer")

    # methods defined are initiate, update, delete, traverse, insert
    
    def initiate(self, A:list):
        if (len(A) > self.len):
            choice = input("Length exceeds allocated memory. Override length? y/n..")
            if (choice == "y") :
                self.len = len(A)
                self.array = A

        else:
            for i in range(len(A)):
                self.array[i] = A[i]
        
    def update(self, index, data):
        if (index <0): 
            print("Index must be a non-negative integer")
        elif (index >self.len):
            print(f"Index must be less than {self.len}")
        elif (index == self.len):
            n = self.len
            self.len = 2*n
            self.array = self.array + [data] + [0]*n
            
        else: 
            self.array[index] = data

    def delete(self, index):
        if (index <0):
            print("Index must be a non-negative integer")
        elif (index >self.len):
            print(f"Index should be less than {self,len}")
        else:
            for i in range(index,self.len-1):
                self.array[i] = self.array[i+1]
            self.array[self.len-1] = 0

    def insert(self, index, data):
        if (0< index <self.len-1):
            self.len+=1
            self.array = self.array +[0]
            for i in range(index,self.len):
                self.array[i+1] = self.array[i]
            self.array[index] = data

        elif(index > self.len):
            print(f"Index should be less than {self.len}")
        elif (index == self.len):
            n = self.len
            self.len = 2*n
            self.array = self.array + [data] + [0]*n
        else:
            print("Invalid index")
            
    def traverse(self):
        """for i in range(self.len):
            print(f"{self.array[i]},",end='')
        print("\n")"""
        """print(self.array)"""
        
        print("[",end="",sep="")
        for i in range(self.len):
            if (i>0): print(",",end="",sep="")
            print(f"{self.array[i]}",end="",sep="")
        print("]\n",end="",sep="")
                

# main

l = Array(10)
l.traverse()

l.initiate([2,44,6,33,87,7,23,1])
l.traverse()

l.update(index=5, data=98)
l.traverse()

l.delete(index=3)
l.traverse()

l.insert(index=10, data=69)
l.traverse()
