import statistics

numbers_list = []

def display_list_info():
    print("Current Numbers:", numbers_list)
    print("Ascending Order:", sorted(numbers_list))
    print("Descending Order:", sorted(numbers_list, reverse=True))
    if len(numbers_list) > 1:
        print(f"Average: {statistics.mean(numbers_list):.2f}")
        print(f"Median: {statistics.median(numbers_list):.2f}")

def save_list_to_file():
    try:
        file_name = input("Enter filename to save the list: ").strip()
        with open(file_name, "w") as file:
            file.write("Numbers List: " + str(numbers_list) + "\n")
            file.write("Ascending Order: " + str(sorted(numbers_list)) + "\n")
            file.write("Descending Order: " + str(sorted(numbers_list, reverse=True)) + "\n")
            file.write(f"Average: {statistics.mean(numbers_list):.2f}\n")
            file.write(f"Median: {statistics.median(numbers_list):.2f}\n")
        print(f"List successfully saved to {file_name}.")
    except Exception as e:
        print(f"Error saving file: {e}")

while True:
    try:
        user_input = int(input("Enter a number (0 to quit): "))
        if user_input == 0:
            print("Goodbye!")
            save_option = input("Do you want to save the list to a file? (y/n): ").strip().lower()
            if save_option == "y":
                save_list_to_file()
            break
        numbers_list.append(user_input)
        display_list_info()
    except ValueError:
        print("Invalid input. Please enter a valid number.")
