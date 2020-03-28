cc_num = list('4556737586899855')

for i in range(len(cc_num)):
  cc_num[i] = int(cc_num[i])

check_digit = cc_num.pop()
print(check_digit)
print(cc_num)
cc_num_reversed = cc_num[::-1]
print(cc_num_reversed)

for i in range(0, len(cc_num_reversed), 2):
  cc_num_reversed[i] = cc_num_reversed[i] * 2

print(cc_num_reversed)

for i in range(0, len(cc_num_reversed)):
  if cc_num_reversed[i] > 9:
    cc_num_reversed[i] = cc_num_reversed[i] - 9

print(cc_num_reversed)

total = sum(cc_num_reversed)

print(total)

print(total % 10)

print(check_digit == (total % 10))