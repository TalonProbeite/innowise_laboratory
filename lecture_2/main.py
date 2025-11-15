def generate_profile(age:int)->str:
    """Returns the life stage (Child, Teenager, Adult) based on age."""
    if age >= 0 and age <= 12:
        return "Child"
    elif age >= 13 and age <=19:
        return "Teenager"
    elif age >= 20:
        return "Adult"
    return "incorrect year of birth"
    

def get_profile_info()->dict:
    """Collects user information (name, birth year, hobbies) and calculates age and life stage."""
    print("Hello!")
    user_name = input("Enter your full name: ")
    birth_year_str = input("Enter your birth year: ")
    birth_year = int(birth_year_str)
    current_age = 2025 - birth_year
    life_stage = generate_profile(current_age)


    hobbies = []
    while True:
        hobby = input("Enter a favorite hobby оr type 'stop' to finish: ")
        if hobby.strip().lower() == "stop":
            break
        hobbies.append(hobby)
    
    user_profile = {"name":user_name , "age":current_age, "stage":life_stage , "hobbies":hobbies}

    return user_profile 


def show_profile(user_profile:dict)->None:
    """Prints a summary of the user's collected profile data."""
    num_hobbies = len(user_profile["hobbies"])
    if num_hobbies == 0:
        hobbies_summary = "\nYоu didn't mention аnу hobbies.\n"
    else:
        hobbies_summary = f"\nFavorite Hobbies ({num_hobbies}):\n"
        for h in user_profile["hobbies"]:
            hobbies_summary += f"- {h}\n"
        
    
    summery_profile = f"""---
Profil Summary
Name: {user_profile["name"]}
Age: {user_profile["age"]}
Life Stage: {user_profile["stage"]}"""
    summery_profile += hobbies_summary + "---"

    print(summery_profile)


def main():
    """Main function to run the profile generation and display process."""
    show_profile(get_profile_info())


if __name__ == "__main__":
    main()