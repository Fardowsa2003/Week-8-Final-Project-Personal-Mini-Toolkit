
import random

# Store tasks for the To-Do List tool
tasks = []

# Welcome message
print("====================================")
print("     WELCOME TO MY MINI-TOOLKIT")
print("====================================")
print("Your personal collection of useful tools!")

# Main menu loop
while True:
    print("\nPlease choose a tool:")
    print("1. Number Guessing Game")
    print("2. To-Do List")
    print("3. Simple Calculator")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    # Tool 1: Number Guessing Game
    # The user guesses a random number until they get it right.
    if choice == "1":
        secret_number = random.randint(1, 10)
        guess = 0

        print("\n--- NUMBER GUESSING GAME ---")
        print("I am thinking of a number between 1 and 10.")

        while guess != secret_number:
            try:
                guess = int(input("Enter your guess: "))

                if guess < secret_number:
                    print("Too low! Try again.")
                elif guess > secret_number:
                    print("Too high! Try again.")
                else:
                    print(f"Congratulations! You guessed {secret_number} correctly!")

            except ValueError:
                print("Please enter a valid whole number.")

    # Tool 2: To-Do List
    # The user can add, view, and remove tasks from a list.
    elif choice == "2":
        while True:
            print("\n--- TO-DO LIST ---")
            print("1. Add a task")
            print("2. View tasks")
            print("3. Remove a task")
            print("4. Back to main menu")

            todo_choice = input("Choose an option (1-4): ")

            if todo_choice == "1":
                task = input("Enter your new task: ")
                tasks.append(task)
                print(f"Task '{task}' has been added successfully!")

            elif todo_choice == "2":
                if len(tasks) == 0:
                    print("Your to-do list is empty.")
                else:
                    print("\nYour Tasks:")
                    for number, task in enumerate(tasks, start=1):
                        print(f"{number}. {task}")

            elif todo_choice == "3":
                if len(tasks) == 0:
                    print("There are no tasks to remove.")
                else:
                    for number, task in enumerate(tasks, start=1):
                        print(f"{number}. {task}")

                    try:
                        task_number = int(input("Enter the task number to remove: "))

                        if 1 <= task_number <= len(tasks):
                            removed_task = tasks.pop(task_number - 1)
                            print(f"Task '{removed_task}' removed successfully!")
                        else:
                            print("Invalid task number.")

                    except ValueError:
                        print("Please enter a valid number.")

            elif todo_choice == "4":
                print("Returning to the main menu...")
                break

            else:
                print("Invalid option. Please choose between 1 and 4.")

    # Tool 3: Simple Calculator
    # The user can perform basic mathematical operations.
    elif choice == "3":
        print("\n--- SIMPLE CALCULATOR ---")

        try:
            num1 = float(input("Enter the first number: "))
            operator = input("Enter an operation (+, -, *, /): ")
            num2 = float(input("Enter the second number: "))

            if operator == "+":
                result = num1 + num2
                print(f"The answer is: {result}")

            elif operator == "-":
                result = num1 - num2
                print(f"The answer is: {result}")

            elif operator == "*":
                result = num1 * num2
                print(f"The answer is: {result}")

            elif operator == "/":
                if num2 != 0:
                    result = num1 / num2
                    print(f"The answer is: {result}")
                else:
                    print("Error: You cannot divide by zero.")

            else:
                print("Invalid operation. Please use +, -, *, or /.")

        except ValueError:
            print("Invalid input. Please enter valid numbers.")

    # Quit option
    elif choice == "4":
        print("\nThank you for using my Mini-Toolkit!")
        print("Goodbye! Have a wonderful day.")
        break

    # Handle invalid menu choices
    else:
        print(f"Sorry, '{choice}' is not a valid choice. Please select 1, 2, 3, or 4.")
