import os
import time
import pyautogui

def clear():
    """Clear the terminal screen based on OS."""
    os.system('clear' if os.name == 'posix' else 'cls')

def spambotgui():
    """Displays the spambot GUI header."""
    print("""
███████╗██████╗  █████╗ ███╗   ███╗██████╗  ██████╗ █████████
██╔════╝██╔══██╗██╔══██╗████╗ ████║██╔══██╗██╔═══██╗╚══██╔══╝
███████╗██████╔╝███████║██╔████╔██║██████╔╝██║   ██║   ██║
╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██╔══██╗██║   ██║   ██║
███████║██║     ██║  ██║██║ ╚═╝ ██║██████╔╝╚██████╔╝   ██║
╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═════╝  ╚═════╝    ╚═╝
               [+]  Made By Exploits  [+]                            
""")

def get_message():
    """Get the spam message from user input."""
    return input('Enter your message to spam: ')

def get_count():
    """Get the number of times to spam from user input."""
    while True:
        try:
            count = int(input('How many times would you like to spam? '))
            if count > 0:
                return count
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def confirm_action(message):
    """Confirm action with the user."""
    confirmation = input(f"Are you sure you want to spam '{message}'? (y/n): ").lower()
    return confirmation == 'y'

def spam_message(message, count):
    """Perform the actual spamming of the message."""
    print(f"Spamming {message} {count} times...")
    for _ in range(count):
        pyautogui.typewrite(message)
        pyautogui.press('enter')
    print(f"Successfully spammed '{message}' {count} times!")

def spam_from_file(filename='filespam.txt'):
    """Spam messages from a file."""
    if not os.path.exists(filename):
        print(f"File '{filename}' not found!")
        return
    
    with open(filename, 'r') as file:
        lines = file.readlines()

    print(f"Spamming {len(lines)} lines from '{filename}'...")
    for line in lines:
        pyautogui.typewrite(line.strip()) 
        pyautogui.press('enter')
    print(f"Successfully spammed {len(lines)} lines from '{filename}'.")

def main():
    clear()
    spambotgui()
    print("[1] Spam a custom message")
    print("[2] Spam from a file")
    print("[0] Exit")
    choice = input('Choose an option: ')

    if choice == '0':
        print("Exiting the program...")
        quit()

    elif choice == '1':
        clear()
        spambotgui()
        message = get_message()

        if not confirm_action(message):
            main() 

        count = get_count()
        time.sleep(2) 
        spam_message(message, count)
        
    elif choice == '2':
        clear()
        spambotgui()
        print("Ensure the file 'filespam.txt' exists and contains the lines you want to spam.")
        input("Press Enter to continue...")

        if not confirm_action("spamming from the file"):
            main() 

        spam_from_file()

    else:
        print("Invalid input. Please choose a valid option.")
        time.sleep(1)
        main()

if __name__ == "__main__":
    main()
