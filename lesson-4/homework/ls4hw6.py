pas = input()

if len(pas) < 8:
    print("Password is too short.")
if pas.lower() == pas:
    print("Password must contain an uppercase letter")
else:
    print("Password is strong")
