import pyautogui
import pyperclip

# Function to check if clipboard content is equal to a number
def is_clipboard_same_as_number(number):
    try:
        clipboard_content = pyperclip.paste()
        return clipboard_content.strip() == str(number)
    except Exception as e:
        print("Error:", e)
        return False

pyautogui.sleep(5)

#print(pyautogui.position()) pyautogui.sleep(55)
pyautogui.moveTo(-359, 457)
pyautogui.sleep(1)
pyautogui.click()
pyautogui.sleep(1)

for i in range(10):
    for y in range(10):
        for z in range(10):
            for x in range(10):
                if found == 1:
                    break
                pyautogui.sleep(2)
                pyautogui.click()
                pyautogui.hotkey('ctrl', 'a')
                pyautogui.hotkey('Del')
                combination = f"{i}{y}{z}{x}"
                pyautogui.typewrite(combination)
                pyautogui.hotkey('ctrl', 'a')
                pyautogui.hotkey('ctrl', 'c')  # Copy to clipboard
                pyautogui.press('Enter')
                if is_clipboard_same_as_number(combination):
                   kati  = 0
                else:
                    print(f"The Correct code is : ",i,y,z,x-1)
                    found = 1
            if found == 1:
                break
        if found == 1:
            break
    if found == 1:
        break
