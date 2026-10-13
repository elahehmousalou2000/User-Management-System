users = []

def add_user(name, email):
    users.append({"id": len(users) + 1, "name": name, "email": email})

def show_users():
    for user in users:
        print(user)

add_user("Ali", "ali@example.com")
add_user("Sara", "sara@example.com")
show_users()
