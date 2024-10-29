import pyperclip
import keyboard

def modify_clipboard():
    previous_text = ""
    while True:
        # Get the current text from the clipboard
        if keyboard.is_pressed("ctrl+c"):
            current_text = pyperclip.paste()

            # Check if the clipboard text has changed
            if current_text != previous_text:
                # Replace line breaks with spaces
                modified_text = current_text.replace('\n', ' ').replace('\r', ' ').strip()
                # Update the clipboard if the text has been modified
                pyperclip.copy(modified_text)
                print(f"Modified Clipboard Text: {modified_text}")
                previous_text = current_text

if __name__ == "__main__":
    print("Clipboard Modifier is running. Press 'Ctrl+C' to stop.")
    try:
        # Start modifying the clipboard
        modify_clipboard()
    except KeyboardInterrupt:
        print("\nClipboard Modifier stopped.")
    except Exception as e:
        print(f"An error occurred: {e}")
