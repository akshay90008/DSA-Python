"""arr=list(map(int,input("enter the array").split()))
arr.reverse()"""#or by two point swapper 
arr=list(map(int,input("enter the array").split()))
l=0 
r=len(arr)-1
while l<r: 
    arr[l],arr[r]=arr[r],arr[l]
    l=l=1
    r=r-1
print(f"reversed array is {arr}")
