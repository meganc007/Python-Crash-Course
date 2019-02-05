current_users = ['sam', 'dean', 'castiel', 'crowley', 'meg']
new_users = ['rowena', 'kevin', 'azazel', 'sam', 'castiel']

if current_users and new_users:
    for new_user in new_users:
        if new_user.lower() in current_users:
            print("That username is already taken.")
        else:
            current_users.append(new_user)
            print(new_user.title() + " was added to the site.")
    print(current_users)
else:
    print("There aren't any users!")