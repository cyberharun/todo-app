def condition(password):
    result = {}
    if len(password) >= 8:
        result["lenght"] = True
    else:
        result["lenght"] = False

    digit = False
    for i in password:
        if i.isdigit():
            digit = True

    result["digits"] = digit

    uppercase = False
    for i in password:
        if i.isupper():
            uppercase = True

    result["uppercase"] = uppercase

    if all(result.values()):
        return "Strong password"

    else:
        return "Weak password"


user_password = input("Enter new password: ")
print(condition(user_password))
