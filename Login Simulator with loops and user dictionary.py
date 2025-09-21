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
        break
    else:
        attempts += 1 #counts as failed attempt
        if attempts < 3: #As to not repeat try again after too many attempts
            print ('Access denied. Try again.')
if attempts == 3:
    print ('Access denied. Too many failed attempts.') 