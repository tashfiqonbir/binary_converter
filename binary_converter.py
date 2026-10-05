"""
User-Friendly Binary Converter CLI Tool
Author: Tashfiq Onbir 
GitHub: https://github.com/tashfiqonbir
Description: A clean and easy-to-use Binary Encoder & Decoder.
"""

import sys
import os

def clear_screen():
    """Clears the terminal screen for a clean user interface."""
    os.system('cls' if os.name == 'nt' else 'clear')

def text_to_binary(text):
    """Convert text to an 8-bit space-separated binary string."""
    try:
        return ' '.join(format(ord(char), '08b') for char in text)
    except Exception as e:
        return f"Error: {e}"

def binary_to_text(binary_string):
    """Convert a binary string back to human-readable text."""
    try:
        # Strip spaces and split by chunks
        binary_values = binary_string.strip().split(' ')
        
        # If input is continuous without spaces, try splitting every 8 bits
        if len(binary_values) == 1 and len(binary_values[0]) >= 8:
            binary_values = [binary_values[0][i:i+8] for i in range(0, len(binary_values[0]), 8)]
            
        text = "".join([chr(int(b, 2)) for b in binary_values if b])
        return text
    except ValueError:
        return "⚠️ Invalid Binary Code! Please use only 0s, 1s, and spaces."
    except Exception as e:
        return f"Error: {e}"

def main():
    while True:
        clear_screen()
        print("╭───────────────────────────────────────────────╮")
        print("│        ✨ BINARY CONVERTER TOOL BY ONBIR ✨            │")
        print("╰───────────────────────────────────────────────╯")
        print("  [1] 📝 Encode: Text ➔ Binary")
        print("  [2] 🔓 Decode: Binary ➔ Text")
        print("  [3] ❌ Exit")
        print("─────────────────────────────────────────────────")
        
        choice = input("👉 Select an option (1/2/3): ").strip()
        
        if choice == '1':
            clear_screen()
            print("📝 [TEXT ➔ BINARY ENCODER]")
            print("───────────────────────────")
            text_input = input("Enter the text you want to convert:\n> ")
            
            if text_input:
                binary_result = text_to_binary(text_input)
                print("\n📊 [Resulting Binary Code]:")
                print(binary_result)
            else:
                print("\n⚠️ Input cannot be empty!")
                
            input("\nPress Enter to return to Menu...")
            
        elif choice == '2':
            clear_screen()
            print("🔓 [BINARY ➔ TEXT DECODER]")
            print("───────────────────────────")
            binary_input = input("Enter the binary code (spaces allowed):\n> ")
            
            if binary_input:
                text_result = binary_to_text(binary_input)
                print("\n📄 [Decoded Plain Text]:")
                print(text_result)
            else:
                print("\n⚠️ Input cannot be empty!")
                
            input("\nPress Enter to return to Menu...")
            
        elif choice == '3':
            clear_screen()
            print("\n👋 Thank you for using this tool! Goodbye.\n")
            sys.exit()
            
        else:
            print("\n❌ Invalid choice! Please select 1, 2, or 3.")
            input("Press Enter to try again...")

if __name__ == "__main__":
    main()
