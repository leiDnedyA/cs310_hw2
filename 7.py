
def bucket_sort(temps):
    buckets = [[] for _ in range(-50, 51)]
    # strategy: add 50 to all temps when figuring out
    # which bucket to put them in
    for t in temps:
        n = t + 50
        buckets[n//len(buckets)].append(t)
    for bucket in buckets:
        bucket.sort()
    result = []
    for bucket in buckets:
        result += bucket
    return result

if __name__ == "__main__":
    temperature_data = [10, 20, -5, 8, 12, 18, 5, -3, 0, 15]
    print(bucket_sort(temperature_data))


