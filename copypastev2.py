import pyperclip
import time

def modify_clipboard():
    previous_text = ""
    print("Clipboard Modifier is running.")
    while True:
        try:
            # Get clipboard content
            current_text = pyperclip.paste()
            
            # Check if clipboard content is valid text and has changed
            if current_text and current_text != previous_text:
                # Replace line breaks with spaces and strip whitespace
                modified_text = current_text.replace('\n', ' ').replace('\r', ' ').strip()
                
                # Update clipboard only if modification occurs
                if modified_text != current_text:
                    pyperclip.copy(modified_text)
                    print(f"Clipboard updated: {modified_text}")
                
                # Update the previous text tracker
                previous_text = current_text
        
        except pyperclip.PyperclipException as e:
            print(f"Clipboard error: {e}")
        
        except Exception as e:
            print(f"Unexpected error: {e}")
        
        # Sleep to prevent CPU overload
        time.sleep(0.5)

if __name__ == "__main__":
    try:
        modify_clipboard()
    except KeyboardInterrupt:
        print("Clipboard Modifier stopped.")
