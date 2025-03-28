def is_password_secure(password):
    special_char = [
        "!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", 
        ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~"
    ]
    is_digit = False
    is_char = False
    is_lower = False
    is_upper = False

    for i in password:
        if i in special_char:
            is_char = True

    if any(i for i in password if i.isdigit()):
        is_digit = True

    if any(i for i in password if i.isupper()):
        is_upper = True

    if any(i for i in password if i.islower()):
        is_lower = True

    if len(password) >= 8 and is_digit and is_char and is_lower and is_upper:
        return "Password is valid"
    
    return "Password is not valid. It must be at least 8 characters long and include a mix of uppercase, lowercase, digits, and special characters."
