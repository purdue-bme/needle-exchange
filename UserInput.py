import time

users = ['1234']
i = 1

while True:
    keypad_input = input('Please enter a four-digit passcode: ')
    i += 1
    if i > 3:
        print('Access denied. Too many attempts.')
        break
    if keypad_input.isdigit() == False:
        print('Passcode must be four numerical digits.')
        time.sleep(1)
    else:
        if len(keypad_input) > 0:
            if len(keypad_input) == 4:
                if keypad_input in users:
                    print('Access granted.')
                    break
                else:
                    print('Access denied. User not recognized.')
                    time.sleep(1)
            if len(keypad_input) > 4 or len(keypad_input) < 4:
                print('Passcode must be four digits.')
                keypad_input = []
                time.sleep(1)
