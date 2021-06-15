import random




def main():
    user_input = input("press enter to generate a random password: ")
    while True:
        if user_input == "":
            password = generate_password(20)
            print (password)
            user_input = input('press enter to generate a random password: ')
        else:
            user_input = input('press enter to generate a random password: ')


#create a function to shuffle the order of the characters


def generate_password(length):

    types_of_char = int(input("how many char types? (1-4): "))      
    #character types include: uppercase and lowercase alphabets, numbers and special characters

    #validation statement
    while types_of_char > 4 or types_of_char < 1:
        types_of_char = int(input("how many char types? (1-4): "))

    #get a list of integers which correspond to number of uppercase, lowercase, number and special characters within the length of the password 
    char_type_numbers = get_char_type_numbers(length, types_of_char) 

    #empty lists to hold password strings when
    upp_case_list = []
    low_case_list = [] 
    num_char_list = []
    special_char_list = []

    #the first element corresponds to number of uppercase letters
    upp_case_char = char_type_numbers[0]
    upp_case_list = get_char("upper", upp_case_char)

    if types_of_char > 1:
        low_case_char = char_type_numbers[1]    #the second element corresponds to number of lowercase letters
        low_case_list = get_char("lower", low_case_char) 
    
    if types_of_char > 2:
        num_char = char_type_numbers[2]         #the third element corresponds to number of numbers 
        num_char_list = get_char("num", num_char) 

    if types_of_char > 3:
        special_char = char_type_numbers[3]     #the fourth element corresponds to number of special characters
        special_char_list = get_char("special", special_char)


    # combined list that is shuffled randomly
    password_list = upp_case_list + low_case_list + num_char_list + special_char_list 
    random.shuffle(password_list)
    password = turn_list_into_string(password_list)

    return password
    
def get_char(char_type, num):
    #the character type and their numbers (how many of each) are passed as arguments and to return randomised characters in the required frequency

    char_list = [] 

    if char_type == "upper":
        for i in range(num):
            char = chr(random.randint(65,90))
            char_list.append(char)
        return char_list
    # a list of required characters is returned

    elif char_type == "lower":
        for i in range(num):
            char = chr(random.randint(97, 122))
            char_list.append(char)
        return char_list

    elif char_type == "num":
        for i in range(num):
            num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8 , 9]
            char = str(random.choice(num_list))
            char_list.append(char)
        return char_list

    elif char_type == "special":
        for i in range(num):
            special_char = ['!', '?', '@', '#', '$', '%', '&']
            char = random.choice(special_char)
            char_list.append(char)
        return char_list

def  turn_list_into_string(password_list):
    password = ''
    for i in range(len(password_list)):
        password = password + str(password_list[i]) 
    return password

def get_char_type_numbers(total_length, types_of_char):
    #tried to use loop, didn't work (3)
    
    sum_of_values = 0

    #if all types of characters included, then random values are generated that all sum to the length of the password
    if types_of_char == 4:
        char_type_numbers = [1, 1, 1, 1] 
        # each character has a minimum of 1 value (number of times they appear in the password)
        # a random value for each character is generated from the remaining available values left in the length of the password
        # each time sum is updated so that the total length does not excede the length
        sum_of_values = char_type_numbers[0] + char_type_numbers[1] + char_type_numbers[2] + char_type_numbers[3] # (=4)
        char_type_numbers[0] = random.randint(1, total_length - (sum_of_values - 1))
        sum_of_values = char_type_numbers[0] + char_type_numbers[1] + char_type_numbers[2] + char_type_numbers[3]
        char_type_numbers[1] = random.randint(1, total_length - (sum_of_values - 1))
        sum_of_values = char_type_numbers[0] + char_type_numbers[1] + char_type_numbers[2] + char_type_numbers[3]
        char_type_numbers[2] = random.randint(1, total_length - (sum_of_values - 1))
        sum_of_values = char_type_numbers[0] + char_type_numbers[1] + char_type_numbers[2] + char_type_numbers[3]
        char_type_numbers[3] = total_length - sum_of_values + 1

    elif types_of_char == 3:
        char_type_numbers = [1, 1, 1]
        sum_of_values = char_type_numbers[0] + char_type_numbers[1] + char_type_numbers[2] # (=3)
        char_type_numbers[0] = random.randint(1, total_length - (sum_of_values - 1))
        sum_of_values = char_type_numbers[0] + char_type_numbers[1] + char_type_numbers[2]
        char_type_numbers[1] = random.randint(1, total_length - (sum_of_values - 1))
        sum_of_values = char_type_numbers[0] + char_type_numbers[1] + char_type_numbers[2]
        char_type_numbers[2] = total_length - sum_of_values + 1

    elif types_of_char == 2:
        char_type_numbers = [1, 1]
        sum_of_values = char_type_numbers[0] + char_type_numbers[1] # (=2)
        char_type_numbers[0] = random.randint(1, total_length - (sum_of_values - 1))
        sum_of_values = char_type_numbers[0] + char_type_numbers[1]
        char_type_numbers[1] = total_length - sum_of_values + 1

    else: 
        char_type_numbers = [1]
        char_type_numbers[0] = total_length
            

    return char_type_numbers
        
    
    
if __name__ == '__main__':
    main()