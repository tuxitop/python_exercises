import re


def compress(word):
    output = word[0]
    count = 1
    for i, char in enumerate(word[:-1]):
        if char == word[i+1]:
            count += 1
        else:
            if count != 1:
                output += str(count)
            output += word[i+1]
            count = 1
    if count != 1:
        output += str(count)
    return output


def decompress(word):
    return re.sub('(.)([0-9]+)', lambda m: m.group(1) * int(m.group(2)), word)


outputs = []
for i in range(int(input())):
    if input() == '1':
        outputs.append(compress(input()))
    else:
        outputs.append(decompress(input()))
print(*outputs, sep='\n')
