arr=list(map(int,input("enter the array ").split()))
#we need define the prefix sum array 
prefix_sum=[0]*len(arr)#creates an empty structure of the same size as arr
prefix_sum[0]=arr[0]#first element of prefix sum array is same as the first element of the original array
for i in range(1,len(arr)):
    prefix_sum[i]=prefix_sum[i-1]+arr[i]
print(f"prefix sum array is {prefix_sum}")
#find the sum of elements from index i to j in O(1) time complexity
i,j=map(int,input("enter the index i and j").split())
if i==0:
    print(f"sum of elements from index {i} to {j} is {prefix_sum[j]}")
else:  
    print(f"sum of elements from index {i} to {j} is {prefix_sum[j]-prefix_sum[i-1]}")