from xml.dom import UserDataHandler
name = ''
      

def user_details():
    """
    Prompt user input
    """
    while True:
        first_name =input("Insert your first name\n").lower()

        if first_name.isalpha():
            break

        else:
            print("Invalid first name")
    
    
    while True:
        last_name =input("Insert your last name\n").lower()

        if last_name.isalpha():
            break

        else:
            print("Invalid last name")

    while True:
        cohort = input("Insert your cohort\n")
        if cohort.isdigit() != True or cohort == "":
            continue
        elif int(cohort) < 2023:
            print("Invalid cohort\n")
            continue
        else:
            break
    
    while True:
        Campus = ["johannesburg","durban","phokeng","cape town"]
        final_campus = input("Insert the campus you will be attending in\n").lower()

        if final_campus in Campus:
            break
        else:
            print("Invalid campus")
    return create_user_name(first_name, last_name, cohort, final_campus)
            
def create_user_name(first_name, last_name, cohort, final_campus):
    """
    Create and return a valid username
    """
    first_3 = last_name[:3].lower()
    last_3 = ''
    uppercase_campus = ''
    for char in first_name:
        last_3 = last_3[-2:] + char
    
   
    uppercase_campus = user_campus(final_campus)

    username = last_3 + first_3 + uppercase_campus + str(cohort)
    return username

def user_campus(campus):
    """
    Return valid campus abbreviations
    """
    uppercase_campus = ''
    if campus == "Durban":
        uppercase_campus = "DBN"
    elif campus == "Johannesburg":
        uppercase_campus = "JHB"
    elif campus == "Cape Town":
        uppercase_campus = "CPT"
    elif campus == "Phokeng":
        uppercase_campus = "NW"
    
    return uppercase_campus

if __name__ == '__main__':
    first_name, last_name, cohort, final_campus = user_details()
    create_user_name(first_name, last_name, cohort, final_campus)
    