input()
orig = input()
recieved = input()
mistakes = 0
for i, letter in enumerate(recieved):
    if orig[i] != letter:
        mistakes += 1

print(mistakes)
