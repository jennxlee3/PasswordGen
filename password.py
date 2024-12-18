import random

upp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
low = "abcdefghijklmnopqrstubwxyz"
sym = "!@#$%^&*()_+-=[]{}|;:,.<>?/~`"
digits = "0123456789"


user_input = input("Would you like a weak or strong password? ")

def generate_password():
    global password
    if user_input.lower() == "strong":
        password = list(''.join([random.choice(set) for set in [upp, low, sym, digits] for _ in range(2)]))
        random.shuffle(password)
    elif user_input.lower() == "weak":
        password = [
            random.choice(random.choice([upp, low, sym, digits])) for _ in range(4)
        ]
        random.shuffle(password)
    else:
        print("Invalid input. Type either weak or strong.")

    return ''.join(password)

if __name__ == "__main__":
    passwrd = generate_password()
    print("Your new password is:", passwrd)
    print("Store it somewhere safe!")






