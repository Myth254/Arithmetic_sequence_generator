# Arithmetic sequence generator
# Starting value (first term)
a1 = 5
# Common difference
d = 3
# Number of terms
n = 8

print("Arithmetic Sequence Generator")
print("=" * 30)
print(f"First term (a1): {a1}")
print(f"Common difference (d): {d}")
print(f"Number of terms (n): {n}")
print()

# Using a loop to get the numbers in sequence
sequence = []
for i in range(n):
    term = a1 + i * d
    sequence.append(term)
    print(f"Term {i+1}: {term}")

print(f"\nComplete sequence: {sequence}")
print()

# Additional calculations
print("Sequence Analysis:")
print("-" * 20)
print(f"Sum of all terms: {sum(sequence)}")
print(f"Average of terms: {sum(sequence)/len(sequence):.2f}")
print(f"Last term: {sequence[-1]}")
print(f"Difference between first and last term: {sequence[-1] - sequence[0]}")

# Verify it's an arithmetic sequence
differences = [sequence[i+1] - sequence[i] for i in range(len(sequence)-1)]
print(f"Differences between consecutive terms: {differences}")
print(f"Is arithmetic sequence? {all(diff == d for diff in differences)}")