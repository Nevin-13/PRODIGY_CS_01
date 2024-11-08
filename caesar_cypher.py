def caesar_cipher(text, shift, mode):
    result = ""
    
    # Adjust the shift if the mode is decryption
    if mode == "decrypt":
        shift = -shift
    
    for char in text:
        if char.isalpha():
            # Shift for uppercase letters
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            # Shift for lowercase letters
            elif char.islower():
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            # Non-alphabetic characters remain unchanged
            result += char
    
    return result

def main():
    print("Welcome to Caesar Cipher Encryption/Decryption!")
    print("===============================================")

    # Get the mode: encryption or decryption
    while True:
        mode = input("Would you like to (E)ncrypt or (D)ecrypt? ").lower()
        if mode in ['e', 'd']:
            break
        else:
            print("Invalid choice. Please select 'E' for Encryption or 'D' for Decryption.")

    mode = "encrypt" if mode == 'e' else "decrypt"

    # Get the shift value
    while True:
        try:
            shift = int(input("Enter the shift value (an integer): "))
            break
        except ValueError:
            print("Invalid input! Please enter an integer value for the shift.")

    # Get the text to encrypt or decrypt
    text = input("Enter the text: ")

    # Perform the cipher operation
    result = caesar_cipher(text, shift, mode)

    # Display the result
    if mode == "encrypt":
        print(f"Encrypted Text: {result}")
    else:
        print(f"Decrypted Text: {result}")

if __name__ == "__main__":
    main()
