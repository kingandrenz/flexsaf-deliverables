#!/usr/bin/python3

import json
import re

### ---- validation logics ---

def validate_age(age, min_age=1, max_age=150):
    """ checks that is is not negative or 0 and that it is not
        relatively high
    """
    try:
        age_int = int(age)
        
        if not (min_age <= age_int <= max_age):
            print(f"Age must be between {min_age} and {max_age}.")
            return False

        return True
        
    except (ValueError, TypeError):
        print("invalid input. Please enter a valid integer.")
        return False


def validate_name(name, min_len=3, max_len=20):
    """ checks if name is withinn the length range and name is alphabeth"""
    if not min_len <= len(name) <= max_len:
        print(f"Name length must be {min_len}-{max_len} characters.")
        return False

    is_valid = all(char.isalpha() or char.isspace() for char in name)
        
    if not is_valid:
        print("Name must only contain letters.")
        return False
        
    return True


def validate_email(email):
    """Checks that email follows a basic format and ends with .com"""

    regex_pattern = r'^\w+@\w+\.com$'
    
    if re.search(regex_pattern, email.strip()):
        return True
    else:
        print("Please enter a valid Email format (e.g., 'example@domain.com')")
        return False

### ---- saving and reading JSON file logic ---

def save_profile(file_path, profile):
    """ saves profile to file_path"""
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(profile, f, indent=4)
        print("Profile saved successfully!")
            
    except FileNotFoundError:
        print(f"Error: The directory for '{file_path}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")




def read_profile(file_path):
    """ read and print profile from profile.json file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            profile = json.load(f)
            return profile
    except FileNotFoundError:
        print("No Profile found at that file path")
        return None
    except json.JSONDecodeError:
        print("Error: file exists but data is corrupted")
        return None


def main():
    file_path = "profile.json"

    # Input and Validation Loop
    while True:
        name = input("Please Enter Name: ")
        if not validate_name(name):
            continue
            
        age = input("Please Enter Age: ")
        if not validate_age(age):
            continue
            
        email = input("Please Enter Email: ")
        if not validate_email(email):
            continue

        profile = {
            "name": name, 
            "age": int(age), 
            "email": email
        }
        
        # Save the profile
        save_profile(file_path, profile)
        break

    # Read and display the saved profile
    profile_data = read_profile(file_path)

    if profile_data:
        print("\n--- Saved Profile ---")
        print(f"Name: {profile_data['name']}")
        print(f"Age: {profile_data['age']}")
        print(f"Email: {profile_data['email']}")

if __name__ == "__main__":
    main()
