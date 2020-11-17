#  This is a data task. You can use this editor as a playground

with open("../../../data/2.txt") as fp:
    lines = fp.read().splitlines()

text = lines[0]
k = int(lines[1])


def count_pattern(data, pattern):
    count = 0
    patternLength = len(pattern)
    for i in range(len(data) - patternLength + 1):
        if data[i:i + patternLength] == pattern:
            count += 1
    return count


def frequent_words(data, pattern_length):
    frequentPatterns = set()
    count = []
    for i in range(len(data) - pattern_length + 1):
        pattern = data[i:i + pattern_length]
        count.append(count_pattern(data, pattern))
    maxCount = max(count)
    for i in range(len(data) - pattern_length + 1):
        if count[i] == maxCount:
            frequentPatterns.add(data[i:i + pattern_length])
    return ' '.join(map(str, [*frequentPatterns]))


print(frequent_words(text, k))
