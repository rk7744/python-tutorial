# 12. Sum and average of positive and negative numbers
nums = [int(input("Enter number: ")) for _ in range(4)]
pos = [x for x in nums if x > 0]
neg = [x for x in nums if x < 0]
print("Sum of positive numbers:", sum(pos), "Average:", sum(pos)/len(pos) if pos else 0)
print("Sum of negative numbers:", sum(neg), "Average:", sum(neg)/len(neg) if neg else 0)
