#  This is a data task. You can use this editor as a playground

with open("../../../data/1.txt") as fp:
    lines = fp.read().splitlines()


def count_pattern(data, pattern):
    count = 0
    patternLength = len(pattern)
    for i in range(len(data) - patternLength + 1):
        if data[i:i + patternLength] == pattern:
            count += 1
    return count


print(count_pattern(lines[0], lines[1]))
