import tkinter as tk
from Code.login import *
from Code.db import *


def main(): # determines if new user or existing user

    make_database() # makes database if it does not exist yet

    def existing_user():
        user_info = existing_user_login(None)
        #main_menu(user_info)

    root = tk.Tk()
    root.title("Nutrition Buddy")
   
    welcome_label = tk.Label(root, text="Welcome to Nutrition Pal!", font=("Georgia", 25))
    welcome_label.pack(pady=30)

    new_user_button = tk.Button(root, text="New User", command = new_user)
    new_user_button.pack(pady=10)

    existing_user_button = tk.Button(root, text="Existing User", command = existing_user)
    existing_user_button.pack(pady=10)

    root.mainloop()


        
  
def new_user():
    new_account()
    main_menu()



def main_menu(user_info):


   # UI: make these boxes to click on
   print("Main Menu:")
   print("1. View Diary") # add food, view remaining calories, view macros (optional)
   print("2. Goal Progress") # input weight, see pace, view progress, add progress pics
   print("3. Exercises") # create exercise plans that match goals, learn about workouts
   print("4. Calendar") # view daily calorie eating and exercises
   print("0. Settings") # change personal information (heighr, weight, age, goals, etc)
   main_menu_choice = input("--> ")


   if main_menu_choice == "1":
       # view_diary()
       None
   elif main_menu_choice == "2":
       # goal_progress()
       None
   elif main_menu_choice == "3":
       # exercises()
       None
   elif main_menu_choice == "4":
       # calendar()
       None
   else:
       print("Error")
   return None

main()