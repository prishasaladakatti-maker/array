import sys

if len(sys.argv) > 1:
    scores = list(map(int, sys.argv[1:]))
else:
    scores = list(map(int, input("Enter scores: ").split()))

total = sum(scores)
average = total / len(scores)

print("Scores:", scores)
print("Sum:", total)
print("Average:", average)