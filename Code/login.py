import tkinter as tk
from Code.db import *
from Code.calculate import *


# for users who alredy have an account, checks the db for their username first, and if there is an existing account w/
# that username, checks if password matches. if username does not exist/password is wrong, tells them and lets
# them try again.
def existing_user_login(message):

    root = tk.Tk()
    root.title("Nutrition Pal Login")

    # displays a message at the top when either the username or login is not found or incorrect
    if message: 
        message_label = tk.Label(root, text=message, foreground="red")
        message_label.pack(pady=10)


    username_label = tk.Label(root, text="Username:")
    username_entry = tk.Entry(root)
    username_label.pack(pady=10)
    username_entry.pack(pady=10)

    password_label = tk.Label(root, text="Password:")
    password_entry = tk.Entry(root, show="*")
    password_label.pack(pady=10)
    password_entry.pack(pady=10)

    print(username_entry)
    print(password_entry)

    login_button = tk.Button(root, text="Login", command=lambda: login_attempt(username_entry.get(), password_entry.get()))
    login_button.pack(pady=10)

    root.mainloop()

def login_attempt(username_entry, password_entry):
    username_exists = check_username_exists(username_entry)
    if username_exists == False:
        message = "Account with this username not found, try again"
        existing_user_login(message)
    else:
        is_pass_correct = check_password(username_entry, password_entry)
        if is_pass_correct == True:
            user_info = get_user_info(username_entry)
            print(user_info)
            return user_info
        else:
            message = "Password is incorrect, try again"
            existing_user_login(message)




# new account creation. makes sure username does not exist and that pass is secure enough. asks user for info to
# formulate target calorie intake to reach their goals. adds it to database as a new entry
def new_account(new_account_message):

    # this checks if username is available for new account
    root = tk.Tk()
    root.title("Create New Account")

    if new_account_message:
        new_account_message_label = tk.Label(root,text=new_account_message, foreground="red")
        new_account_message_label.pack(pady=10)


    username_label = tk.Label(root, text="Username:")
    username_entry = tk.Entry(root)
    username_label.pack(pady=10)
    username_entry.pack(pady=10)

    password_label = tk.Label(root, text="Password:")
    password_entry = tk.Entry(root, show="*")
    password_label.pack(pady=10)
    password_entry.pack(pady=10)

    login_button = tk.Button(root, text="Login", command=lambda: login_attempt(username_entry.get(), password_entry.get()))
    login_button.pack(pady=10)

    username_exists = True
    while username_exists == True:
        username = input("Enter username: ")
        username_exists = check_username_exists(username) # False if nobody has that username yet


    # checks if password meets criteria of 8-20 chars and at least one digit
    password_acceptable = False
    while password_acceptable == False:
        password = input("Enter password (between 8-20 chars, at least 1 digit): ")
        password_acceptable = check_password_eligible(password) # returns True if password is good, False if not

    new_user_quiz()

def create_account_attempt(username_entry, password_entry):

    username_exists = check_username_exists(username_entry)
    if username_exists:
        message = "Account with this username already exists. Try again!"
        new_account(message)
    else:
        password_eligible = check_password_eligible(password_entry)
        if password_eligible:
            new_user_quiz(username_entry, password_entry)


def new_user_quiz(username, password):

    import tkinter as tk

def gather_info(name_entry, gender, age_entry, feet_var, inches_var, weight_var):
    name = name_entry.get()
    user_gender = "M" if gender.get() == 1 else "F"
    age = age_entry.get()
    feet = feet_var.get()
    inches = inches_var.get()
    weight = weight_var.get()
    height = (int(feet) * 12) + int(inches)
    saved_info = [name, user_gender, age, height, weight]
    print(saved_info)

    # Destroy the current frame and create the activity frame
    current_frame.destroy()
    create_activity_frame()

def create_input_frame():
    input_frame = tk.Frame(root, width=300, height=200)

    name_var = tk.StringVar()
    gender = tk.IntVar()
    age_var = tk.StringVar()
    feet_var = tk.StringVar()
    inches_var = tk.StringVar()
    weight_var = tk.StringVar()

    name_entry = create_label_entry("Name:", name_var, 0, input_frame)
    create_label_entry("Gender:", None, 1, input_frame)
    age_entry = create_label_entry("Age:", age_var, 2, input_frame)
    create_label_entry("Height:", None, 3, input_frame)
    create_label_entry("Weight (lbs):", weight_var, 4, input_frame)

    male_button = tk.Radiobutton(input_frame, text="Male", variable=gender, value=1)
    female_button = tk.Radiobutton(input_frame, text="Female", variable=gender, value=2)
    male_button.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)
    female_button.grid(row=1, column=1, padx=10, pady=10, sticky=tk.E)

    feet_label = tk.Label(input_frame, text="feet:")
    feet_entry = tk.Entry(input_frame, textvariable=feet_var)
    inches_label = tk.Label(input_frame, text="inches:")
    inches_entry = tk.Entry(input_frame, textvariable=inches_var)

    feet_label.grid(row=3, column=0, sticky=tk.E)
    feet_entry.grid(row=3, column=1, padx=10, pady=10)
    inches_label.grid(row=3, column=2, sticky=tk.E)
    inches_entry.grid(row=3, column=3, padx=10, pady=10)

    weight_entry = create_label_entry("Weight (lbs):", weight_var, 4, input_frame)

    submit_button = tk.Button(input_frame, text="Submit", command=lambda: gather_info(name_entry, gender, age_entry, feet_entry, inches_entry, weight_entry))
    submit_button.grid(row=5, column=0, columnspan=2, pady=20)

    input_frame.pack(fill=tk.BOTH, expand=True)

def create_activity_frame():
    activity_frame = tk.Frame(root, width=300, height=200)

    select_activity_label = tk.Label(activity_frame, text="Select Your Activity Level")

    option1 = tk.Radiobutton(activity_frame, text="Sedentary: little or no exercise, inactive job", value=1)
    option2 = tk.Radiobutton(activity_frame, text="Lightly Active: light exercise 1-3 days/week", value=2)
    option3 = tk.Radiobutton(activity_frame, text="Moderately Active: moderate exercise 3-5 days/week", value=3)
    option4 = tk.Radiobutton(activity_frame, text="Very Active: heavy exercise 6-7 days/week", value=4)
    option5 = tk.Radiobutton(activity_frame, text="Extremely Active: strenuous training 2x/day", value=5)

    select_activity_label.grid(row=0, column=0)
    option1.grid(row=1, pady=5)
    option2.grid(row=2, pady=5)
    option3.grid(row=3, pady=5)
    option4.grid(row=4, pady=5)
    option5.grid(row=5, pady=5)

    activity_frame.pack(fill=tk.BOTH, expand=True)

def create_label_entry(label_text, entry_var, row, frame):
    label = tk.Label(frame, text=label_text)
    entry = tk.Entry(frame, textvariable=entry_var)
    label.grid(row=row, column=0, stick=tk.E)
    entry.grid(row=row, column=1, padx=10, pady=10)
    return entry

root = tk.Tk()
root.title("Getting Started")
root.geometry("375x667")  # iOS-like dimensions

# Create the initial input frame
current_frame = tk.Frame(root)
create_input_frame()

root.mainloop()



"""
    if not (1 <= activity_choice <= 5):
        activity_choice = input("Please enter valid answer: ")
    if activity_choice == 1:
        activity_level = 1.2
    elif activity_choice == 2:
        activity_level = 1.375
    elif activity_choice == 3:
        activity_level = 1.55
    elif activity_choice == 4:
        activity_level = 1.725
    elif activity_choice == 5:
        activity_level = 1.9
    else:
        print("Error")
    
    maintenance = round(calculate_maintenance(gender, age, height, weight, activity_level))


    goal_weight = float(input("Goal weight: "))
    calorie_goal = 0
    
    if goal_weight < weight:
        goal = "loss"
        print("Choose a goal:")
        print("2. Extreme Weight Loss (2 lbs/week)")
        print("1.5. Rapid Weight Loss (1.5 lbs/week")
        print("1. Moderate Weight Loss (1 lb/week) *RECCOMENDED*")
        print("0.5. Gradual Weight Loss (0.5 lbs/week")
        weight_loss_speed = float(input("--> "))
        calorie_goal = find_calorie_goal(goal, weight_loss_speed, maintenance)
    elif goal_weight > weight:
        goal = "gain"
        print("Choose a goal:")
        print("2. Gain 2 lbs/week")
        print("1.5. Gain 1.5 lbs/week")
        print("1. Gain 1 lb/week")
        print("0.5. Gain 0.5 lbs/week")
        weight_gain_speed = float(input("--> "))
        calorie_goal = find_calorie_goal(goal, weight_gain_speed, maintenance)


    # 10 total items
    user_info = [username, password, name, gender, age, height, weight, goal_weight, maintenance, goal, calorie_goal]


    add_new_to_db(user_info)
    """




new_user_quiz("luke", "orow")