arr=[5,4,3,2,1,0]
n= len(arr)
l= 0
r= n-1
while l<=r:
    arr[l],arr[r]=arr[r],arr[l]
    l+=1
    r-=1
print(arr)
