def getnumber():
    nums = []
    xStr = input("Enter a number (<Enter> to quit)>>")
    while(xStr != ""):
        x = eval(xStr)
        nums.append(x)
        xStr = input("Enter a number (<Enter> to quit)>>")
    return nums


def mean(nums):
    sum = 0.0
    for num in nums:
        sum += num
    return sum/len(nums)


def median(nums):
    nums.sort()
    size = len(nums)

    rmedian = 0
    midPos = size // 2
    if size % 2 == 0:
        rmedian = (nums[midPos] + nums[midPos-1]) / 2
    else:
        rmedian = nums[midPos]
    return rmedian


def Main():
    lst = getnumber()
    print(lst)
    mean_outcome = mean(lst)
    print(mean_outcome)
    median_outcome = median(lst)
    print(median_outcome)


Main()
