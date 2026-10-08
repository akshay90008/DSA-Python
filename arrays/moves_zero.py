#suppose array is given and we have to move all the zeros to the end of the array without changing the order of non-zero elements
arr=[0,0,1,2,2,330,33,00,23,1,3,0,11]
arr1=[]
for i in range(len(arr)):
    if arr[i]!=0:
        arr1.append(arr[i])
while len(arr1)<len(arr):
    arr1.append(0)
print(f"array after moving all the zeros to the end is {arr1}")