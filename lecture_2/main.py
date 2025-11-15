def generate_profile(age:int)->str:
    if age >= 0 and age <= 12:
        return "Child"
    elif age >= 13 and age <=19:
        return "Teenager"
    elif age >= 20:
        return "Adult"
    return "incorrect year of birth"
    

def get_profile_info()->dict:
    print("Hello!")
    user_name = input("Enter your full name: ")
    birth_year_str = input("Enter your birth year: ")
    birth_year = int(birth_year_str)
    current_age = 2025 - birth_year
    life_stage = generate_profile(current_age)


    hobbies = []
    while True:
        hobby = input("Enter а favorite hobby ог type 'stop' to finish: ")
        if hobby.strip().lower() == "stop":
            break
        hobbies.append(hobby)
    
    user_profile = {"name":user_name , "age":current_age, "stage":life_stage , "hobbies":hobbies}

    return user_profile 