def caesar_encrypt(text, shift):
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main():
 while True:    
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))

    encrypted_message = caesar_encrypt(message, shift)
    print("Encrypted message:", encrypted_message)
    

    User_input = input("\n For Decryption Type : d   ")
    if User_input.lower() == 'd':
        decrypted_message = caesar_decrypt(encrypted_message, shift)
        print("Decrypted message:", decrypted_message)

    break_code = input("To quit the program press q or any key to continue the program : ")
    if  break_code == 'q':
       break

main()
