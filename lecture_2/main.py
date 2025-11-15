def generate_profile(age:int)->str:
    if age >= 0 and age <= 12:
        return "Child"
    elif age >= 13 and age <=19:
        return "Teenager"
    elif age >= 20:
        return "Adult"