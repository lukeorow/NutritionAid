from Code.db import *


my_list = ("lukeorow", "lukeyy123", 'Luke Orow', 'M', 20, 76, 232.3, 200, 3000, '1', 2500)
my_list2 = ("jakeybear", "jakeronii", "jake fisher", "M", 15, 68, 150.4, 170, 2400, '2', 2900)
username = my_list[0]
username2 = my_list2[0]


updated_user = ("lukeorow", "lukeyy123", 'Luke Orow', 'M', 20, 76, 232.3, 200, 3000, '1', 2500)
modify_existing_user(updated_user)


#make_database()
#add_new_to_db(my_list2)
user_info = get_user_info(username)
user_info2 = get_user_info(username2)
print(user_info)
print(user_info2)
