import pyperclip
import keyboard

def modify_clipboard():
    previous_text = ""
    current_text = ""
    while True:
        # Get the current text from the clipboard
        if keyboard.is_pressed("ctrl+c") and current_text != previous_text:
            current_text = pyperclip.paste()
            # Replace line breaks with spaces
            modified_text = current_text.replace('\n', ' ').replace('\r', ' ').strip()
            # Update the clipboard if the text has been modified
            pyperclip.copy(modified_text)
            previous_text = current_text

if __name__ == "__main__":
    print("Clipboard Modifier is running.")
    try:
        modify_clipboard()
    except Exception as e:
        print(f"An error occurred: {e}")
