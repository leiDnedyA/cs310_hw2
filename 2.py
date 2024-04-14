
def counting_sort(nums: list[int]) -> list[int]:
    """
    Sorts a list of numbers using
    counting sort.
    """
    max_num = 0
    min_num = 0
    for n in nums:
        max_num, min_num = max(max_num, n), min(min_num, n)
    count_arr = [0 for _ in range(max_num - min_num + 1)]
    output_arr = [0 for _ in range(len(nums))]
    for n in nums:
        m = n - min_num
        count_arr[m] += 1
    for i in range(len(count_arr) - 1):
        count_arr[i + 1] += count_arr[i]
    for n in nums[::-1]:
        m = n - min_num
        count_arr[m] -= 1
        output_arr[count_arr[m]] = n
    return output_arr

if __name__ == "__main__":
    arr = [3, 5, 1, 9, 3, 8, 1, 2]
    print(counting_sort(arr))
