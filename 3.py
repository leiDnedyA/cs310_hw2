
def merge(lists: list[list[int]], result=[], curr_list=0) -> list[int]:
    if len(lists) == 1:
        return lists[0]
    nums1 = lists[curr_list]
    nums2 = result
    result = []
    i, j = 0, 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            result.append(nums1[i])
            i += 1
            continue
        result.append(nums2[j])
        j += 1
    while i < len(nums1):
        result.append(nums1[i])
        i += 1
    while j < len(nums2):
        result.append(nums2[j])
        j += 1
    if curr_list == len(lists) - 1:
        return result
    return merge(lists, result, curr_list+1)

if __name__ == "__main__":
    k = 3
    lists = [[1, 4, 6], [2, 3, 5], [0, 7, 8]]
    print(merge(lists))


