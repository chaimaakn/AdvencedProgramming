numbers = [1, 2, 3, 4, 5]

def display_menu():
    print("\nMenu:")
    print("1. Append")
    print("2. Insert")
    print("3. Pop")
    print("4. Remove")
    print("5. Sort")
    print("6. Reverse")
    print("7. Search")
    print("8. Quit")

def append_value():
    value = int(input("Enter value: "))
    numbers.append(value)

def insert_value():
    value = int(input("Enter value: "))
    index = int(input("Enter index: "))
    if 0 <= index <= len(numbers):
        numbers.insert(index, value)
    else:
        print("Invalid index.")

def pop_value():
    if numbers:
        index = int(input("Enter index to pop (-1 for last element): "))
        if index == -1:
            numbers.pop()
        elif 0 <= index < len(numbers):
            numbers.pop(index)
        else:
            print("Invalid index.")
    else:
        print("List is empty.")

def remove_value():
    value = int(input("Enter value to remove: "))
    if value in numbers:
        numbers.remove(value)
    else:
        print("Value not found in list.")

while True:
    print("\nCurrent List:", numbers)
    display_menu()
    try:
        option = int(input("Choose an option: (for example if you want to choose Append option enter 1) "))
        if option == 1:
            append_value()
        elif option == 2:
            insert_value()
        elif option == 3:
            pop_value()
        elif option == 4:
            remove_value()
        elif option == 5:
            numbers.sort()
        elif option == 6:
            numbers.reverse()
        elif option == 7:
            value = int(input("Enter value to search: "))
            if value in numbers:
                print(f"Value {value} found at index {numbers.index(value)}.")
            else:
                print("Value not found in list.")
        elif option == 8:
            break
        else:
            print("Invalid option. Please choose from the menu.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
