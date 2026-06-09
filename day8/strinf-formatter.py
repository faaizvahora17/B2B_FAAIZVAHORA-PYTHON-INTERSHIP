name = input("Enter your name: ")
city = input("Enter your city: ")

formatted_name = name.strip().title()
formatted_city = city.strip().title()
message = f"My name is {formatted_name} and I live in {formatted_city}"
print(message)