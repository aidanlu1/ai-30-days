scores = [88, 92, 75, 60, 95]

print(scores[-2])
sum = 0
count = 0
for index, score in enumerate(scores):
    sum += score

average = sum / len(scores)




for index, score in enumerate(scores):
    if score > average:
        count += 1

print(count)
print(scores)

