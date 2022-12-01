# 03
import numpy as np

lines = open("input.txt", 'r').read().splitlines()
sums = np.zeros(len(lines[0]))
digits = len(sums)
num_entries = len(lines)
for line in lines:
    sums += np.array([int(i) for i in line])
most_common = np.int32(sums > num_entries/2)
# print(most_common)
gamma, epsilon = 0, 0  
for i in range(digits):
    gamma += most_common[i] * 2 ** ( i )
    epsilon += (1-most_common[i]) * 2 ** ( i )
# for i in range(digits):
#     print(most_common[digits-i-1],end="")
# print()
# print(gamma, epsilon)
# gamma = np.binary_repr(num)
# least_common = np.not_test(most_common)
# print(sums)
# print(most_common)
# print(least_common)

print(f"Part 1: gamma={gamma}, epsilon={epsilon}, solution={gamma*epsilon} ")


def most_common_at_bit(data, bit_position):
    sum = 0
    num_entries = len(data)
    for line in data:
        sum += int(line[bit_position])
    return int(sum >= num_entries/2)


def only_entries_bit_val(data, pos, val):
    out = []
    for line in data:
        if line[pos] == str(val):
            out.append(line)
    return out

# O2 score (most common)
data1 = [l for l in lines]
# print(data[:10])

for i in range(digits):
    mcv = most_common_at_bit(data1, i)
    # print(mcv)
    data1 = only_entries_bit_val(data1, i, mcv)
    # print(data[:10])
    if len(data1) <= 1:
        break
print(data1)

data2 = [l for l in lines]
for i in range(digits):
    lcv = 1 - most_common_at_bit(data2, i)
    data2 = only_entries_bit_val(data2, i, lcv)
    if len(data2) <= 1:
        break
print(data2)

o2, co2 = 0, 0  
for i in range(digits):
    o2 += int(data1[0][i]) * 2 ** ( digits - i - 1 )
    co2 += int(data2[0][i]) * 2 ** ( digits - i - 1 )


print(f"Part 2: o2={o2}, epsilon={co2}, solution={o2*co2} ")
