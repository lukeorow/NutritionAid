def find_calorie_goal(goal, speed, maintenance): 
    if goal == "loss":
        calorie_goal = maintenance - (speed * 500)
    if goal == "gain":
        calorie_goal = maintenance + (speed * 500)
    return calorie_goal

# calculates calorie maintenence based on information from user
def calculate_maintenance(gender, age, height, weight, activity_level):
    if gender == "M":
        bmr = float(10 * (weight * 0.453592) + (6.25 * (height * 2.54)) - (5 * age) + 5)
    if gender == "F":
        bmr = float(10 * (weight * 0.453592) + (6.25 * (height * 2.54)) - (5 * age) - 161)

    maintenance = bmr * activity_level
    return maintenance