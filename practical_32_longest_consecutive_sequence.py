# Practical 32: Find longest consecutive sequence of numbers

nums = [100, 4, 200, 1, 3, 2]
print("Numbers:", nums)

num_set = set(nums)
longest_streak = 0
best_seq = []

for num in num_set:
    # Check if it's the start of a sequence
    if num - 1 not in num_set:
        current_num = num
        current_seq = [current_num]

        while current_num + 1 in num_set:
            current_num += 1
            current_seq.append(current_num)

        if len(current_seq) > longest_streak:
            longest_streak = len(current_seq)
            best_seq = current_seq

print("Longest consecutive sequence length:", longest_streak)
print("Sequence:", best_seq)
