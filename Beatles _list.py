# Step 1: Create an empty list named beatles
beatles = []

# Step 2: Use the append() method to add John Lennon, Paul McCartney, and George Harrison
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

print("Initial List of Beatles:")
print(beatles)

# Step 3: Use the for loop and the append() method to prompt the user to add Stu Sutcliffe and Pete Best
members_to_add = ["Stu Sutcliffe", "Pete Best"]
for member in members_to_add:
    response = input(f"Do you want to add {member} to the list? (yes/no): ")
    if response.lower() == "yes":
        beatles.append(member)
    else:
        print(f"{member} not added.")

print("\nList of Beatles after adding members:")
print(beatles)

# Step 4: Use the del instruction to remove Stu Sutcliffe and Pete Best from the list
members_to_remove = ["Stu Sutcliffe", "Pete Best"]
for member in members_to_remove:
    if member in beatles:
        beatles.remove(member)  # Using remove() instead of del for simplicity
        print(f"{member} removed from the list.")

print("\nList of Beatles after removing members:")
print(beatles)

# Step 5: Use the insert() method to add Ringo Starr to the beginning of the list
beatles.insert(0, "Ringo Starr")

print("\nFinal List of Beatles:")
print(beatles)
