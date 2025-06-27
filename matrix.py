# Program: To get the addition of row elements and column elements in a matrix
# Collect matrix dimensions from the user
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

lst = []

# Input: total number of elements based on matrix size
num = rows * cols
print(f"\nYou need to enter {num} elements.")

# Collect the elements from the user
for i in range(num):
    element = int(input(f"Enter element {i + 1}: "))
    lst.append(element)

# Print the updated list
print(f"\nUpdated list: {lst}\n")

# Initialize row sums, column sums, and total sum
row_sums = [0] * rows     # To store sums of rows
col_sums = [0] * cols     # To store sums of columns
total_sum = 0             # To store the total sum of all elements

# Print elements in a matrix and calculate row and column sums
print("Matrix with Row Sums:")
j = 0  # index for accessing list elements
for m in range(rows):
    row_sum = 0  # Initialize sum for the current row
    for n in range(cols):
        value = lst[j]
        print(f"{value:<4}", end='')  # Adjust spacing for alignment
        row_sum += value              # Add to the current row sum
        col_sums[n] += value          # Add to the respective column sum
        total_sum += value            # Add to the total sum
        j += 1
    row_sums[m] = row_sum             # Store the current row sum
    print(f"| {row_sum:<4}")          # Print only the row sum

# Print column sums below the matrix with alignment
print("-" * (cols * 4))               # Adjust separator length based on number of columns
for col_sum in col_sums:
    print(f"{col_sum:<4}", end='')    # Align sums directly under their columns

# Calculate and print the combined total of row sums and column sums
combined_total = sum(row_sums) + sum(col_sums)
print(f"  {combined_total}\n")        # Print combined total at the bottom right

# Print total sum of all rows and columns
print(f"Total Sum of all elements: {total_sum}")