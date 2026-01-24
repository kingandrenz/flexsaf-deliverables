# Profile Manager (Python Script)

## 📌 Overview
This program is a simple **Profile Manager** written in Python.  
It allows users to:
- Enter their **Name**, **Age**, and **Email**.
- Validate the inputs to ensure they meet specific rules.
- Save the profile data into a JSON file (`profile.json`).
- Read and display the saved profile back to the user.

It demonstrates **input validation**, **file handling**, and **JSON serialization** in Python.

---

## ⚙️ Features
- **Name Validation**: Must be 3–20 characters long and contain only letters/spaces.
- **Age Validation**: Must be an integer between 1 and 150.
- **Email Validation**: Must follow the format `example@domain.com` and end with `.com`.
- **Save Profile**: Stores the profile in a JSON file.
- **Read Profile**: Loads and displays the saved profile.

---

## 🚀 How to Run
1. Ensure you have **Python 3** installed on your system.
   ```bash
   python3 --version


2. Save the script as intro_to_json.py / profile_manager.py (or any name you prefer).

3. Run the script in your terminal:

   ```bash
   python3 profile_manager.py

4. Follow the prompts to enter your Name, Age, and Email.

5. The program will validate your inputs, save them to profile.json, and display the saved profile.


### 📂 File Structure


   ```bash
   project-folder/
   │── profile_manager.py   # Main program
   │── profile.json         # Generated JSON file with saved profile
   │── README.md            # Documentation


### 📦 Required Libraries
This program uses only Python Standard Libraries, so no external installations are needed:

json -> For saving and reading profile data.

re -> For validating email format.


### 📝 Example Run

   ```bash
   Please Enter Name: John Doe
Please Enter Age: 25
Please Enter Email: johndoe@example.com
Profile saved successfully!

--- Saved Profile ---
Name: Anthony Kanu
Age: 25
Email: kanu@example.com

    
