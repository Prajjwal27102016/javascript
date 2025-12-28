# Get user input
amount = int(input("Enter the total amount in Rupees: "))

print(f"\nBreakdown for ₹{amount}:")

# Calculate 1000 rupee notes
notes_1000 = amount // 1000
amount = amount % 1000

# Calculate 500 rupee notes
notes_500 = amount // 500
amount = amount % 500

# Calculate 100 rupee notes
notes_100 = amount // 100
amount = amount % 100

# Display Results
print(f"1000 Rupee notes: {notes_1000}")
print(f"500 Rupee notes: {notes_500}")
print(f"100 Rupee notes: {notes_100}")
print(f"Remaining balance: ₹{amount}")