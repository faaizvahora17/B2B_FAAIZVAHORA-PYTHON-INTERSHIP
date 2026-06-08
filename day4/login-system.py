CORRECT_USERNAME = "admin"
CORRECT_PASSWORD = "password123"

username = input("Enter username: ")
password = input("Enter password: ")

if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
  print("Login Successful")
else:
  print("Login Failed")