for i in range(3):
    print("======갤러그 게임 시작======")
    print("!!==적 비행기 발생했습니다==!!")
    print("1. 총알 발사 2. 오른쪽이동 3. 왼쪽이동 ")
    number = input("숫자를 입력하세요: ")
    print("당신의 입력값: ", number)
# 1번을 누르면 총알 발사합니다.
    if number == "1":
        print("=======================")
        print("탕-------------------!!")
        print("=======================")
# 만약에 2번을 누르면 오른쪽으로 이동합니다.
    if number == "2":
        print("=======================")
        print("오른쪽으로 이동")
        print("=======================")
# 만약에 3번을 누르면 왼쪽으로 이동합니다.
    if number == "3":
        print("=======================")
        print("왼쪽으로 이동")
        print("=======================")