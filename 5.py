def _get_digit(n: float, i):
    return ((n * 10**i) % 10) // 1

def _bubble_sort(nums, key):
    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            if key(nums[j]) > key(nums[j+1]):
                nums[j], nums[j+1] = nums[j+1], nums[j]

def _least_significant_digit(n: float) -> int:
    s = str(n)
    return len(s.split('.')[1])

def radix_sort(nums: list[float]):
    result = [n for n in nums] # Clone nums
    max_digits = 0
    for n in nums:
        max_digits = max(max_digits, _least_significant_digit(n))
    for i in range(max_digits, 0, -1):
        _bubble_sort(result, lambda n: _get_digit(n, i))
    return result

if __name__ == "__main__":
    print(radix_sort([0.170, 0.45, 0.75, 0.90, 0.802, 0.24, 0.2, 0.66]))
