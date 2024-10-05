def calculate_love_score(name_one, name_two):
    #how many times does the letter in word 'TRUE' occure
    
    word_true_one = {'T': 0,'R': 0,'U': 0,'E': 0}
    word_true_two = {'T': 0,'R': 0,'U': 0,'E': 0}

    #Find matches for 'True' in name one
    for letter in name_one:
        for let_True in "TRUE":
            if let_True.lower() == letter.lower():
                word_true_one[let_True] += 1

    #Find matches for 'True' in name two
    for letter in name_two:
        for let_True in "TRUE":
            if let_True.lower() == letter.lower():
                word_true_two[let_True] += 1

    combined_values_true = {key: word_true_one[key] + word_true_two[key] for key in word_true_one}
    print(combined_values_true)

    total_true = 0
    for i in combined_values_true:
        total_true += combined_values_true[i]


    #same for 'LOVE'

    word_love_one = {'L': 0, 'O': 0, 'V': 0, 'E': 0}
    word_love_two = {'L': 0, 'O': 0, 'V': 0, 'E': 0}

        #Find matches for 'True' in name one
    for letter in name_one:
        for let_True in "LOVE":
            if let_True.lower() == letter.lower():
                word_love_one[let_True] += 1

    #Find matches for 'True' in name two
    for letter in name_two:
        for let_True in "LOVE":
            if let_True.lower() == letter.lower():
                word_love_two[let_True] += 1

    combined_values_love = {key: word_love_one[key] + word_love_two[key] for key in word_love_one}
    print(combined_values_love)

    total_love = 0
    for i in combined_values_love:
        total_love += combined_values_love[i]

    #combine the scores

    love_score = str(total_true) + str(total_love)
    print(love_score)

# name_one = input("Enter their first name")
# name_two = input("Enter their second name")

calculate_love_score("Kanye West", "Kim Kardashian")

