n = int(input())
sum_p1 = 0
sum_p2 = 0
sum_p3 = 0
sum_p4 = 0
sum_p5 = 0

for i in range(n):
    number = int(input())
    if number < 200:
        sum_p1 += 1
    elif number < 400:
        sum_p2 += 1
    elif number < 600:
        sum_p3 += 1
    elif number < 800:
        sum_p4 += 1
    else:
        sum_p5 += 1

total_sum = sum_p1 + sum_p2 + sum_p3 + sum_p4 + sum_p5
p1 = (sum_p1 / total_sum) * 100
p2 = (sum_p2 / total_sum) * 100
p3 = (sum_p3 / total_sum) * 100
p4 = (sum_p4 / total_sum) * 100
p5 = (sum_p5 / total_sum) * 100

print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')
print(f'{p4:.2f}%')
print(f'{p5:.2f}%')