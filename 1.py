
def counting_sort(chars: list[str]) -> list[str]:
    """
    Sorts a list of chars [strings of len=1] using
    counting sort.
    """
    count_arr = [0 for _ in range(27)]
    output_arr = [0 for _ in range(len(chars))]
    for c in chars:
        n = ord(c) - ord('a')
        count_arr[n] += 1
    for i in range(len(count_arr) - 1):
        count_arr[i + 1] += count_arr[i]
    for c in chars[::-1]:
        n = ord(c) - ord('a')
        count_arr[n] -= 1
        output_arr[count_arr[n]] = c
    return output_arr

if __name__ == "__main__":
    arr = ['b', 'd', 'a', 'c', 'f', 'e']
    print(counting_sort(arr))
