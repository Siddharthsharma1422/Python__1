#-------Search in Rotated Array-----------#
#----simple brute force approach will be to iterate through all the elements of the array and if it is equal to target it will give us the index number__________#
#________or the second approach could be to use binary search but i find brute force equally simple and efficient--------------#

#----CODE----#
nums = [4,5,6,7,0,1,2] 
target = 0
for i in range(len(nums)):
    if (nums[i]==target):
        return i
return -1

