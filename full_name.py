first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}")

message = f"Hello, {full_name.title()}!"
print(message)

message = "{} {}".format(first_name, last_name)
print(message)

print("Python")
print("\tPython")

print("Languages:\nPython\nC\nJavascript")
print("Languages:\n\tPython\n\tC\n\tJavascript")

favorite_language = ' python '
print(favorite_language)
print(favorite_language.lstrip())