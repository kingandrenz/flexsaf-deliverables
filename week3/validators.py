def is_adult(age):
    return age >= 18

def is_authenticated(username, password, database):
    for user in database:
        if user["username"] == username and user["password"] == password:
            return True
    return False
