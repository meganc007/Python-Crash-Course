users = ['admin', 'sara', 'dean', 'hackerman67', 'Xx_butterfly_unicorn_sparkle_rainbow_xX']
usernames = []

if usernames:
     for username in usernames:

         if username == 'admin':
            print("Hello " + username + ". Click to view stats.")
         else:
            print("Greetings " + username.title() + ". Nice to see you, again.")

else:
    print("We need to find some users!")