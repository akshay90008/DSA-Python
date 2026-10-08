arr=list(map(int,input("enter the number of elements in the array").split()))
#first we will find the prefix sum of array then we will store the prefix sum in a new array and then 
prefix_sum=arr[0]
arr1=[prefix_sum]#new array to store the prefix sum of the array
for i in range(1,len(arr)):
    prefix_sum+=arr[i]
    arr1.append(prefix_sum)
    
print(f"prefix sum array is {arr1}")
# if suppose we have to find the sum of elements from index i to j then we can use the prefix sum array to find the sum in O(1) time complexity
i,j=map(int,input("enter the index i and j").split())
if i==0:
    print(f"sum of elements from index {i} to {j} is {arr1[j]}")
else:  
    print(f"sum of elements from index {i} to {j} is {arr1[j]-arr1[i-1]}")
