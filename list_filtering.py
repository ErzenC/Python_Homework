# 5. List Filtering
# numbers = [4, 8, 12, 16, 20, 24]
# Using lambda + filter:
# •	Return values divisible by 4 and strictly greater than 10
numbers = [4, 8, 12, 16, 20, 24]
filtered_numbers = list(filter(lambda x: x % 4 == 0 and x > 10, numbers))
print("Numrat e filtruar:", filtered_numbers)
#OUTPUT: Numrat e filtruar: [12, 16, 20, 24]
