while True:
    user_input = input("Enter a number (or type 'exit' to quit): ")
    
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
    
    if not user_input.isdigit():
        print("Please enter a valid positive number.")
        continue

    number = int(user_input)
    
    if number % 2 == 0:
        print(f"{number} is Even.")
    else:
        print(f"{number} is Odd.")