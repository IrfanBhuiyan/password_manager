from tkinter import *
from tkinter import messagebox
import random
import csv


root = Tk()

root.title("password manager")
root.geometry("700x600")

user_website_label = Label(root, text="Website: ").grid(row=0, column=0, pady = (50,0), padx= (50,30))
username_label = Label(root, text="Username: ").grid(row=1, column=0, pady = 30, padx= (50,30))
password_label = Label(root, text="Password: ").grid(row=2, column=0, padx= (50,30))


user_website = StringVar()
username = StringVar()
user_pass = StringVar()
user_website_entry = Entry(root, textvariable = user_website, width= 32 )
user_website_entry.grid(row=0, column=1, pady = (50,0))
username_entry = Entry(root, textvariable = username, width= 32 )
username_entry.grid(row=1, column=1)
password_entry = Entry(root, textvariable = user_pass, width= 32 )
password_entry.grid(row=2, column=1)

user_data_frame = Frame(root)
user_data_frame.grid(row=4, column=0, columnspan=3, pady= 20)

user_data_scrollbar = Scrollbar(user_data_frame, orient= VERTICAL)
user_data_scrollbar.pack(side=RIGHT, fill=Y)
user_data_listbox = Listbox(user_data_frame, width= 40, height = 12, bd=0, bg="lightgrey", yscrollcommand= user_data_scrollbar.set)
user_data_listbox.pack()

user_data_scrollbar.config(command=user_data_listbox.yview)

password = ''

with open('user_data.csv','a+') as f:
    f.seek(0)
    first_line = str(f.readline())
    if first_line != "website,username,password\n":
        writer = csv.writer(f)
        writer.writerow(["website","username","password"])
    else: 
        pass



def save_and_update():
    user_data_listbox.delete(0, END)
    with open('user_data.csv','a') as f:
        writer = csv.writer(f)
        writer.writerow([user_website.get(),username.get(),user_pass.get()])

    password_entry.delete(0,"end")
    username_entry.delete(0,"end")
    user_website_entry.delete(0,"end")

    info_box = messagebox.showinfo("Success", "Succesfully saved")


    with open('user_data.csv') as f:
        reader = csv.DictReader(f)
        for line in reader:
            username_datum= line['username']
            website_datum = line['website']
            user_data_listbox.insert(END,website_datum + " -> " + username_datum)
            #use a listbox instead of labels

    #for each line in csv file, create labels to show website, username and a button to update or view password
password_show = []



def show_password():
    index = user_data_listbox.curselection()[0]
    with open('user_data.csv') as f:
        reader = csv.reader(f)
        data_list = list(reader)
        password_message = messagebox.showinfo("Password", "Password: " + (data_list[index+1][2])) #get the password from the index+1 line and 3rd column
      

def open_new_window():
    new_window = Toplevel()
    spc_char = IntVar()
    special_char = Checkbutton(new_window, offvalue=3, onvalue=4, variable= spc_char, text= "Include Special Characters (!, ?, @, #, $, %, &)").grid(row=5,column=0, pady=20, padx=10)

    randomise_button = Button(new_window, text= "Generate random password", command = lambda: generate_password(length_slider.get(), spc_char.get() ) )
    randomise_button.grid(row=1, column=0, pady= 20, padx= 20)

    length = Label(new_window, text="Choose the length of Password: ").grid(row=2, column=0, padx=20)
    length_slider = Scale(new_window, from_= 8, to= 32, length= 144, orient=HORIZONTAL)
    length_slider.grid(row=3, column=0, padx= 20, rowspan=2)

generate_password_button = Button(root, command=open_new_window, text="Generate Password", padx=20).grid(row=2, column=2, padx=10)
save_button = Button(root, text="Save", command=save_and_update).grid(row=3, column=2, ipadx=30, pady= (10,0))

show_pass_button = Button(root,text="Show Password", command=show_password).grid (row=5, column=1)


def generate_password(length, types_of_char):
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
    
    #print (password)

    password_entry.delete(0,"end")
    password_entry.insert(0, password)

    #return password
    
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

#to ensure the data loads up each time the app is run
with open('user_data.csv') as f:
    reader = csv.DictReader(f)
    for line in reader:
        username_datum= line['username']
        website_datum = line['website']
        user_data_listbox.insert(END,website_datum + " -> " + username_datum)

root.mainloop()