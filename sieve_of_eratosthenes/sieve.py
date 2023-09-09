import time
start= time.process_time()
n= 1000000
root_n = 1000

a= [True]*n
for i in range(2,root_n):
    if a[i]==True:
        for j in range(i*i,n,i):
            a[i] = False
end = time.process_time()
print(f"done in {end-start} seconds")