import pyautogui
import pyperclip
import time

# Function to check if clipboard content is equal to a number
def is_clipboard_same_as_number(number):
    try:
        clipboard_content = pyperclip.paste()
        return clipboard_content.strip() == str(number)
    except Exception as e:
        print("Error:", e)
        return False


def get_seconds():
    while True:
        time = input("Please select the seconds that you want the program to auto type the Passwords: ")
        if time.isdigit():
            return int(time)
        else:
            print("Invalid input. Please enter a number.")
seconds = get_seconds()

countdown = 5
while countdown > 0:
    print(f"Starting in {countdown} seconds...","\r")
    time.sleep(1)
    countdown -= 1
print("Starting now!")




found = 0
for i in range(10):
    for y in range(10):
        for z in range(10):
            for x in range(10):
                if found == 1:
                    break
                pyautogui.sleep(seconds)
                pyautogui.click()
                pyautogui.hotkey('ctrl', 'a')
                pyautogui.hotkey('Del')
                combination = f"{i}{y}{z}{x}"
                pyautogui.typewrite(combination)
                pyautogui.hotkey('ctrl', 'a')
                pyautogui.hotkey('ctrl', 'c')  # Copy to clipboard
                pyautogui.press('Enter')
                if is_clipboard_same_as_number(combination):
                   found  = 0
                else:
                    print(f"The Correct code is : ",i,y,z,x-1)
                    found = 1
            if found == 1:
                break
        if found == 1:
            break
    if found == 1:
        break
