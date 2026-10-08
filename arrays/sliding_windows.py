arr= list(map(int,input("enter the array ").split()))#this scanner the input without for loop using list 
k=3 
window_sum=0
for i in range(k):
    window_sum+=arr[i]
print(f"window sum of 1 slide ={window_sum}")
max_sum=window_sum

for i in range(k,len(arr)):
    window_sum=window_sum-arr[i-k]+arr[i] # i-k means remove the first element for the window then adding the next element 
    print(f"window sum of {i+1} slide={window_sum}")
    if window_sum>max_sum:
        max_sum=window_sum
print(f"max number in the sliding window {max_sum}")    

    