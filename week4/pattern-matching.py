def check_password():
    """ Iterate through each Character in a string and check if it belongs to 
        specific categories (Uppercase, digits, symbols).
    """
    password = input("Please Enter Password: ")

    score = 0
    tips = []

    if len(password) >= 8:
        score += 1
    else:
        tips.append("Increase password length to at least 8 characters")

    if any(c.isupper() for c in password):
        score += 1
    else:
        tips.append("Add an uppercase letter")

    if any(c.islower() for c in password):
        score += 1
    else:
        tips.append("Add a lowercase letter")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        tips.append("Add at least 1 number")

    if any(c in "@!#$%^&*()-_=+[]{};:,.<>?" for c in password):
        score += 1
    else:
        tips.append("Add a special character")

    labels = {
        0: "Very Weak",
        1: "Weak",
        2: "Fair",
        3: "Medium",
        4: "Strong",
        5: "Very Strong"
    }

    return score, labels[score], tips
