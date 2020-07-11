def RotateBinarySearch( nums , target ):
        l, r = 0, len(nums) - 1
        while(l <= r):
            mid = (l + r) // 2
            if(target == nums[mid]):
                return mid
            # nums[left to mid] is sorted 
            if(nums[l] <= nums[mid]):
                if(target > nums[mid] or target < nums[l]):
                    l = mid + 1
                else:
                    r = mid - 1
            # nums[mid to right] is sorted
            else:
                if(target < nums[mid] or target > nums[r]):
                    r = mid - 1
                else:
                    l = mid + 1
        return -1

#taking a list of rotated sorted array as a space separated input 
n=list(map(int,input().split()))
t=int(input("enter the number to find"))
print(RotateBinarySearch(n,t))
