import random
import string

users  = [1,2]
for user in users:
    userDetails = []
    print('Enter your first name:')
    first_name = input()
    userDetails.append(first_name)
    print('-----------')
    print('Enter your last name:')
    last_name = input()
    userDetails.append(last_name)
    print('-----------')
    print('Enter your email address:')
    email = input()
    userDetails.append(email)
    print('-----------')

    """Generate a random string of fixed length """
    firstChoice = first_name[:2]   
    secondChoice = last_name[-2:]
    res =  ''.join(random.choices(string.ascii_lowercase + string.digits, k = 5))
    password = firstChoice.join(secondChoice)+str(res)
    userDetails.append(password)
    print("The random password generated for you is: " + password)

    def details():
        print("|-------------------|")
        print("|   User details:   |")
        print("|-------------------|")
        print(" First name: " + userDetails[0])
        print("*" * 21)
        print(" Last name: " + userDetails[1])
        print("*" * 21)
        print(" Email: " + userDetails[2])
        print("*" * 21)
        print(" Password: " + userDetails[3])
        print("|-------------------|")
        print("|-------------------|")
        return

    response = input("are you satisfied? 'y/n'? ")
    if(response.lower() == 'y'):
        details()
    else:
        print("Choose a password yourself then")
        user_choice = input("Your chosen password ")
        if(len(user_choice) < 7):
            print("Password must be of length 7 or more. Input new password")
            newChoice = input("New password of length 7 or more ")
            userDetails[3] = newChoice
            print("Your preferred password is: " + newChoice)
            details()
        else:
            userDetails[3] = user_choice
            print("Your preferred password is: " + user_choice)
            details()
