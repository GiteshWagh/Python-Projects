def GoodMorningSir():
    import time

    # realtime = time.strftime('%H:%M:%S')
    # print(realtime)

    CurrentHour = int(time.strftime('%H'))
    CurrentDay = int(time.strftime('%d'))
    CurrentMonth = int(time.strftime('%m'))
    CurrentYear = int(time.strftime('%Y'))
    print(CurrentDay,"/",CurrentMonth,"/",CurrentYear)
    if (CurrentDay == 27 & CurrentMonth == 8):
        print('Jay KOTW. Happy Birthday Swamiji. ')

    else:
        print('Jay Sadguru')


    if (CurrentHour>12 & CurrentHour<16):
        print("Good Afternoon Swamiji")

    elif (CurrentHour>16 & CurrentHour<20):
        print('Good Evening Swamiji')

    elif (CurrentHour>0 & CurrentHour<4):
        print("Good Night swamiji")

    else:
        print('Good Morning Swamiji')



GoodMorningSir()


