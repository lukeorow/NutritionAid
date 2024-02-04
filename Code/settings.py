from Code.fitness import *


def settings():
   settings_choice = input("--> ")
   if settings_choice == 1: # change user information (heigh, weight, etc from original signup quiz)
       change_user_info()
   elif settings_choice == 2: # change the user's goals (weight loss/weight gain and speeds)
       change_goals()
   elif settings_choice == 3: # delete account
       delete_account()


def change_user_info():
   None
def change_goals():
   None
def delete_account():
   None
