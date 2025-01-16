import statistics

def display_list(user_list, descending=False):
    print("Current List:", user_list)
    sorted_list = sorted(user_list, reverse=descending)
    print("Sorted List:", sorted_list)

def calculate_statistics(user_list):
    if user_list:
        mean = statistics.mean(user_list)
        try:
            median = statistics.median(user_list)
        except statistics.StatisticsError:
            median = None 
        print(f"Mean: {mean}")
        print(f"Median: {median}")

def save_to_file(user_list):
    with open("user_list.txt", "a") as file:
        for num in user_list:
            file.write(str(num) + "\n")
    print("List saved to 'user_list.txt'.")

def load_list():
    try:
        with open("user_list.txt", "r") as file:
            loaded_list = [int(line.strip()) for line in file.readlines()]
        return loaded_list
    except FileNotFoundError:
        return []

# Initialize list
user_list = load_list()

while True:
    try:

        user_input = input("Enter a number: ")

        number = int(user_input)

        if number == 0:
            break

        user_list.append(number)

        display_list(user_list)
        
        calculate_statistics(user_list)

        descending_input = input("Do you want the list sorted in descending order? (y/n): ").lower()
        if descending_input == "y":
            display_list(user_list, descending=True)
        
        save_input = input("Do you want to save the list to a file? (y/n): ").lower()
        if save_input == "y":
            save_to_file(user_list)
        
    except ValueError:
        print("Please enter a valid number.")
