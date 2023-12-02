with open('C:/Users/freyf/OneDrive/Pulpit/Filip/inne/programy/AdventOfCode2023/source/1.txt', 'r') as input_file:
    lines = input_file.readlines()

import re

translate = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}

sum1 = 0
sum2 = 0
for line in lines:
    numbers1 = re.findall(r'\d', line.strip())
    numbers2 = re.findall(r"\d|one|two|three|four|five|six|seven|eight|nine", line.strip())
    numbers3 = []
    for number in numbers2:
        numbers3.append(translate.get(number, number))
    sum1 += int(numbers1[0])*10+int(numbers1[-1])
    sum2 += int(numbers3[0])*10+int(numbers3[-1])
print(sum1)
print(sum2)