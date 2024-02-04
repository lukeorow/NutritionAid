import sqlite3


# this creates the database structure if it is not already created
def make_database():
   conn = sqlite3.connect("user_data.db")
   c = conn.cursor()


   try:
       c.execute('''
           CREATE TABLE IF NOT EXISTS UserInfo (
               username TEXT PRIMARY KEY,
               password TEXT NOT NULL,
               name TEXT NOT NULL,
               gender TEXT NOT NULL,
               age INTEGER NOT NULL,
               height INTEGER NOT NULL,
               weight REAL NOT NULL,
               goal_weight REAL NOT NULL,
               maintenance REAL NOT NULL,
               goal TEXT NOT NULL,
               calorie_goal REAL NOT NULL
           )
       ''')
   except Exception as e:
       print(f"Error creating table: {e}")
  
   conn.commit()
   conn.close()




# used for login, when the user enters their username and password, it checks the db input for that username and checks
# if the passwords match. if not, login denied.
def check_password(username, inputted_pass):
   conn = sqlite3.connect("user_data.db")
   c = conn.cursor()


   # format the inputted password to match format of correct_pass grabbed from db
   inputted_pass = "('" + inputted_pass + "',)"


   # this gets the password for the username inputted
   c.execute("SELECT password FROM UserInfo WHERE username = ?", (username,))
   correct_pass = c.fetchone()


   conn.commit()
   conn.close()


   if str(inputted_pass) == str(correct_pass):
       return True
   else:
       return False



# used when user is making a new account. this checks if the entered username is already taken in the db or not.
# returns True if exists, False if not
def check_username_exists(username):
   conn = sqlite3.connect("user_data.db")
   c = conn.cursor()


   c.execute("SELECT username FROM UserInfo WHERE username = ?", (username,))
   existing_username = c.fetchone()


   conn.commit()
   conn.close()


   if existing_username: # if this username already exists
       return True # username already taken, try something new
   else:
       return False # username available, does not exist




# after logging in, this fetches the stored data for the username that is logged in into a dictionary
# Note: could use dictionary or just straight up variables for this, dict might be easier for consistency tho
def get_user_info(username):
   conn = sqlite3.connect("user_data.db")
   c = conn.cursor()
   c.execute("SELECT * FROM UserInfo WHERE username=?", (username,))


   user_info = c.fetchone() # gets the user info for the specified username


   conn.commit()
   conn.close()


   return user_info # will return the list with the user data




# takes new user's info (list) and adds to the database
def add_new_to_db(user_info):
   conn = sqlite3.connect("user_data.db")
   c = conn.cursor()


   c.execute("INSERT INTO UserInfo VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (user_info[0], user_info[1], user_info[2],
   user_info[3], user_info[4], user_info[5], user_info[6], user_info[7], user_info[8], user_info[9], user_info[10],))
  
   conn.commit()
   conn.close()




# overrides an existing db entry with the new data in user_info list
# this will be used when there are edits in settings to the user's data
# note: username is the db key so it cannot be changed (might add ability to change in later update)
def modify_existing_user(user_info):
   conn = sqlite3.connect("user_data.db")
   cursor = conn.cursor()
   username = user_info[0]


   cursor.execute("""
       UPDATE UserInfo
       SET
           password = ?,
           name = ?,
           gender = ?,
           age = ?,
           height = ?,
           weight = ?,
           goal_weight = ?,
           maintenance = ?,
           goal = ?,
           calorie_goal = ?
       WHERE username = ?
       """, (user_info[1], user_info[2], user_info[3], user_info[4], user_info[5], user_info[6], user_info[7],
           user_info[8], user_info[9], user_info[10], username))
  
   conn.commit()
   conn.close()


# checks if password meets reqs (between 8-20 chars, and has at least 1 digit)
def check_password_eligible(password):
   if len(password) < 8 or len(password) > 20:
       return False
   if not any(char.isdigit() for char in password): # returns True if digit in password
       return False
   return True # (pass accepted) means length is between 8 and 20, and there is a digit in password




# for the login page, if they are a new user we can make a new account, put them through the quiz, and put all of their
# information into the database and use the username and a password as the key to get into the account
# for existing users, they will first have to enter their username, and then i can set a correct_password variable equal
# to the password in the database that corresponds to that username. and if they enter the correct password, then
# all other data in database for that user can be retrieved and set to the variables, and they are basically logged in
# and all their data was saved.
