while True:
    print('What is your name?')
    name = input()
    if name != 'Istiaq':
        print('You are not authorized! Try again.')
        continue
    print('Hi, Istiaq! Type your password, please.')
    pw = input()
    if pw =='istiaq123':
        print('Welcome, Istiaq!')
        break
    else:
        print('Wrong! Try again.')
        continue
