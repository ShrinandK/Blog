# Code 1
import time 
def findPrimeNumbers(lower,upper):
  allVal = []     
  for num in range(lower, upper + 1):        
  # all prime numbers are greater than 1        
    if num > 1:            
      for i in range(2, num):                
        if (num % i) == 0:                    
          break            
        else:                
          allVal.append(num)     
  return allVal       
                       
t0 = time.time() 
for iCount in range (1,100000):     
allVal = findPrimeNumbers(1,1000) 
t1 = time.time() 
total = t1-t0 
print(total)

# Code 2
from ctypes import * 
import time 
fun = WinDLL('libprimeNum.dll') 
fun.getPrimeNumber.argtypes = [c_int,c_int,POINTER(c_int)] 
t0 = time.time() 
for iCount in range (1,100000):     
  fun.getPrimeNumber(c_int(1000),c_int(1),pointer(c_int(0))) 
t1 = time.time() 
total = t1-t0 
print(total)

# Code 3
import time  
from cffi import FFI
ffi = FFI()  
lib = ffi.dlopen("libprimeNum.dll")  
# Describe the data type and function prototype to cffi.  
ffi.cdef('''  void getPrimeNumber(int high,int low,int* counter);  ''')  
t0 = time.time()  
for iCount in range (1,100000):      
  high = ffi.cast("int",1000)      
  low = ffi.cast("int",1)      
  counter = ffi.new("int *")      
  counter[0] = 0      
  dout = lib.getPrimeNumber(high,low,counter)  
t1 = time.time()  
total = t1-t0  
print(total) 