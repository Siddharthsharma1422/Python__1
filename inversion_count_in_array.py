#to count the number of inversions needed to sort an array
def merge(arr,temp_arr,left,right,mid):
    mid= len(arr)//2
    left=arr[:mid]
    right= arr[mid:]
    inv_count=0
    i=j=k=0