import statistics


def getnumber():
    nums = []
    xStr = input("Enter a number (<Enter> to quit)>>")
    while (xStr != ""):
        x = eval(xStr)
        nums.append(x)
        xStr = input("Enter a number (<Enter> to quit)>>")
    return nums


def mean(nums):
    # statistics.mean(list)
    sum = 0.0
    for num in nums:
        sum += num
    return sum/len(nums)


def median(nums):
    # statistics.median(list)
    nums.sort()
    size = len(nums)

    rmedian = 0
    midPos = size // 2
    if size % 2 == 0:
        rmedian = (nums[midPos] + nums[midPos-1]) / 2
    else:
        rmedian = nums[midPos]
    return rmedian

