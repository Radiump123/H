import keyboard

def replace_keys_with_h():
    print("Press Ctrl+H to stop.")
    
    while True:
        event = keyboard.read_event()
        
        if event.event_type == keyboard.KEY_DOWN:
            # Stop the script if Ctrl+H is pressed
            if keyboard.is_pressed('ctrl+h'):
                print("Exiting...")
                break

            # Replace any other key with 'H'
            if event.name != 'ctrl' and event.name != 'h':  # Ignore Ctrl and H
                keyboard.press_and_release('backspace')  # Remove the previous input
                keyboard.write('h')  # Output 'H'

if __name__ == "__main__":
    replace_keys_with_h()
