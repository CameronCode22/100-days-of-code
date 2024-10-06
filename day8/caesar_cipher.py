alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
                 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def encrypt(original_text, shift_amount):
    count = 0
    new_text = []

    for letter_orig_text in original_text:
        if letter_orig_text not in alphabet_list:
            new_text += letter_orig_text
        else:
            for index, letter_alphabet in enumerate(alphabet_list):
                if letter_orig_text.lower() == letter_alphabet.lower():
                    new_position = (index + shift_amount) % 26
                    new_text.append(alphabet_list[new_position])
                    count += 1
                    print(new_text)
    print(new_text)

def decrypt(original_text, shift_amount):
    count = 0
    new_text = []
    for letter_orig_text in original_text:
        if letter_orig_text not in alphabet_list:
            new_text += letter_orig_text
        else:
            for index, letter_alphabet in enumerate(alphabet_list):
                if letter_orig_text.lower() == letter_alphabet.lower():
                    new_position = (index - shift_amount) % 26
                    new_text.append(alphabet_list[new_position])
                    count += 1
                    print(new_text)
    print(new_text)

continue_one = True
while continue_one:
    type = input("Type 'encrypt' or 'decrypt' ")
    message = input("Input your message!: ")
    shift_num = int(input("Enter shift numbers: "))

    if type.lower() == 'encrypt':
        encrypt(message, shift_num)
    elif type.lower() == 'decrypt':
        decrypt(message, shift_num)

    retry = input("type 'yes' to go again and 'no' to stop:" )
    cap_retry = retry.lower()

    if cap_retry == 'yes':
        continue
    elif cap_retry == 'no':
        continue_one = False
        break
