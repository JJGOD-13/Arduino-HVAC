import time
x=1234
attempts=3

while True:
    try:
        while attempts>0:
            y=int(input('please enter the vald pin: '))
            if y!=int(y) or len(str(y))!=4:
                print('invalid pin. please enter a 4 digit number')
                continue
            if y==x:
                print('pin accepted')
                break
            else:
                attempts-=1
                if attempts>0:
                    print(f'incorrect pin. you have {attempts} attempts left')

                else:
                    print('you have no attempts left. Please wait 5 seconds to try again')
                    for i in range(5,0,-1):
                        print(f'trying again in {i} seconds')
                        time.sleep(1)

                
                    attempts=3
                    continue
        if y==x:
            break
    except ValueError:
        print('invalid pin. please enter a 4 digit number')
        continue




