import os
import string

# PART 1
with open('6_tuningTrouble\input0.txt') as f:
    chars = f.read()
    for c in range(len(chars)):
        if len(set(chars[c:c+4])) == 4:
            print(c+4)
            break

# PART 2
with open('6_tuningTrouble\input1.txt') as f:
    chars = f.read()
    for c in range(len(chars)):
        if len(set(chars[c:c+14])) == 14:
            print(c+14)
            break
