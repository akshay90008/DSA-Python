arr=list(map(int,input("enter the arrary ").split()))
l=0
maximum=arr[l]
for i in range(len(arr)):
    if arr[i]>maximum:
        maximum=arr[i]
print(f"maximum element in the array is {maximum}")