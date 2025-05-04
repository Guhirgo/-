from random import random, randint

MIN = 0
MAX = 100
MSG_ENTER_DATA = f"Enter your number from {MIN} to {MAX}"
MSG_USER_INPUT = "You have entered {number}"
MSG_USER_WON = "CORRECT"
MSG_USER_MISSED = "Missed"
MSG_WRONG_INPUT = "Only number"

rand_int = randint(MIN , MAX + 1 )


while True:
    print("-"*80)
    user_data = input(MSG_ENTER_DATA).strip().lstrip("0")
    print(MSG_USER_INPUT.fromat(number=user_data))

    if not user_data.isdigit():
        print(MSG_USER_INPUT)
        continue
    user_data = int(user_data)
    if user_data == rand_int:
        print(MSG_USER_WON)
        break
