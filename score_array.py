scores = list(map(int, input("Enter scores: ").split()))

total = sum(scores)
average = total / len(scores)

print("Sum:", total)
print("Average:", average)