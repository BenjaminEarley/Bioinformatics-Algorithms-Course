#  You can experiment here, it won’t be checked

text = "ACTGACTCCCACCCC"
k = 3


def count_pattern(data, pattern):
    count = 0
    patternLength = len(pattern)
    for i in range(len(data) - patternLength + 1):
        if data[i:i + patternLength] == pattern:
            count += 1
    return count


def frequent_words(data, k):
    frequentPatterns = set()
    count = []
    for i in range(len(data) - k + 1):
        pattern = data[i:i + k]
        count.append(count_pattern(data, pattern))
    maxCount = max(count)
    for i in range(len(data) - k + 1):
        if count[i] == maxCount:
            frequentPatterns.add(data[i:i + k])
    return ' '.join(map(str, [*frequentPatterns]))


print(frequent_words(text, k))



