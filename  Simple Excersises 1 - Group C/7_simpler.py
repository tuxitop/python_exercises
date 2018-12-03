numbers = []
for i in range(4):
    numbers.append(float(input()))

sum = sum(numbers)
avg = sum / len(numbers)
prod = 1
for i in numbers:
    prod *= i
max_num = max(numbers)
min_num = min(numbers)
print('Sum : {:0.6f}'.format(sum),
      'Average : {:0.6f}'.format(avg),
      'Product : {:0.6f}'.format(prod),
      'MAX : {:0.6f}'.format(max_num),
      'MIN : {:0.6f}'.format(min_num), sep='\n')
