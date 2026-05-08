# 1. Create and display a list

numItems = int(input("How many numbers would you like to enter? "))

numbers = []

for i in range(numItems):
    value = int(input("Enter an integer: "))
    numbers.append(value)

print("\n1. Original List:")
print(numbers)


# 2. Insert 99 at position 1

numbers.insert(1, 99)

print("\n2. List after inserting 99:")
print(numbers)


# 3. Replace 99 with 100

indexValue = numbers.index(99)
numbers[indexValue] = 100

print("\n3. List after replacing 99 with 100:")
print(numbers)


# 4. Create second list and extend first list

secondList = [500, 600, 700, 800, 900]

print("\n4. Second List:")
print(secondList)

numbers.extend(secondList)

print("\n4. First List after extending:")
print(numbers)


# 5. Remove 800 from the first list

numbers.remove(800)

print("\n5. First List after removing 800:")
print(numbers)

# 6. Remove the third item from the first list

numbers.pop(2)

print("\n6. First List after removing the third item:")
print(numbers)


# 7. Create a list of grades

grades = ["A", "B", "C", "A", "A", "C"]

print("\n7. Grades List:")
print(grades)


# 8. Display the number of A grades

aCount = grades.count("A")

print("\n8. Number of A grades:")
print(aCount)


# 9. Display the index of the first B grade

bIndex = grades.index("B")

print("\n9. Index of first B grade:")
print(bIndex)


# 10. Look for grade F in the list

if "F" in grades:
    print("\n10. F is in the list.")
else:
    print("\n10. F is not in the list.")


# 11. Clear the second list

secondList.clear()

print("\n11. Second List after clearing:")
print(secondList)


# 12. Delete the second list

del secondList

print("\n12. Second List:")
print(secondList)

# 13. Create a list of players

players = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]

print("\n13. Players List:")
print(players)


# 14. Sort the list of players

players.sort()

print("\n14. Sorted Players List:")
print(players)


# 15. Make a copy of the players list

players2 = players.copy()

print("\n15. Players2 List:")
print(players2)


# 16. Reverse the order of players2

players2.reverse()

print("\n16. Players List:")
print(players)

print("\n16. Reversed Players2 List:")
print(players2)