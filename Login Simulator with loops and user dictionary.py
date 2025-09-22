#Login simulator
print ('Welcome to Login Simulator! Please log in here.')
users = {
    'admin': '12345',
    'user1': '12345',
    'user2': '12345',
    'user3': '12345',
    'user4': '12345'
}
attempts = 0 #counting attempts
while attempts < 3:
    username = input('Enter username: ')
    password = input('Enter password: ')
    if username in users and password == users[username]:
        print ('Access granted.')
        print ('Great to see you again,', username,'!')
        while True: #Start menu loop here
            print ('Here is your menu: ')
            print ('1. View profile' )
            print ('2. Change password ')
            print ('3. Log out')
            choice = input('Choose an option (1/2/3): ')
            if choice == '1':
                print (f'Displays profile of user, {username}.')
            elif choice == '2':
                change = input('Do you want to change your password? (yes/no): ')
                if change.lower() == 'yes':
                    while True:
                        new_password = input('Enter new password: ')
                        confirm_password = input('Confirm new password: ')
                        if new_password == confirm_password:
                            users[username] = new_password
                            print ('Password updated. Please log in again: ')
                            attempts = 0
                            logout = True #signal to exit menu
                            break
                        else: print ('Passwords do not match. ')
                    if logout:
                        break #exit menu loop
                elif change.lower() == 'no':
                    print ('No changes made to password.')  
                    break
                else:
                    print ('Password not changed.')
            elif choice == '3':
                print ('Logging out...' )
                break
            else:
                print ('Invalid choice. Try again. ')
    else:
        attempts += 1 #counts as failed attempt
        if attempts < 3: #As to not repeat try again after too many attempts
            print ('Access denied. Try again.')
if attempts == 3:
    print ('Access denied. Too many failed attempts.')
     