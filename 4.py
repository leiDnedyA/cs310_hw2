
def _find_mountain(nums, l, r):
    """
    Idea: binary search but check diff between values
    instead of values themselves
    """
    if r - l == 1:
        return l
    if r - l == 2:
        return l if nums[l] > nums[r - 1] else r - 1
    middle = l + (r - l) // 2
    middle_diff = nums[middle] - nums[middle - 1]
    if middle_diff > 0:
        return _find_mountain(nums, middle, r)
    if middle_diff < 0:
        return _find_mountain(nums, l, middle)
    return l if nums[l] > nums[r - 1] else r - 1

def find_mountain(nums):
    return _find_mountain(nums, 0, len(nums))

if __name__ == "__main__":
    print(find_mountain([1, 3, 5, 4, 2]))
