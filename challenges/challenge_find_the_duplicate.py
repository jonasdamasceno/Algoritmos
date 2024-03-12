from collections import Counter


def find_duplicate(nums):
    if not nums or len(nums) == 1:
        return False

    if not all(isinstance(num, int) for num in nums):
        return False

    count = Counter(nums)

    number, frequency = count.most_common(1)[0]

    if frequency > 1 and number >= 0:
        return number

    return False
