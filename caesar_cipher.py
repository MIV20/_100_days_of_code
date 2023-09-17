from day_8_art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, amount_shift, cipher_direction):

        end_text = ""
    # if direction == "encode" or "decode":
        if cipher_direction == "decode":
            amount_shift *= -1
        for char in start_text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position + amount_shift
                end_text += alphabet[new_position]
            else:
                end_text += char
        print(f"Here's the {direction}d result: {end_text}")
        # else:
        #     print("Not a valid selection, please try again.")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(start_text=text, amount_shift=shift, cipher_direction=direction)

    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == "no":
        should_continue = False
        print("Thanks for using the Caesar Cipher!")