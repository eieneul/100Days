def lily():
    """
    找出100~1000之间的所有水仙花数
    三位数等于其每一位数的三次方之和

    """
    for i in range(100, 1000):
        units_digit = i % 10
        tens_digit = i % 100 // 10
        hundreds_digit = i // 100
        if units_digit ** 3 + tens_digit ** 3 + hundreds_digit ** 3 == i:
            print(i)

# lily()


def perfect_num():
    """
    find 1~9999 all the perfect numbers

    """
    for i in range(2, 10000):
        count = 0
        for j in range(1, i):
            if i % j == 0:
                count += j
        if count == i:
            print(count)


# perfect_num()

def craps():
    """
    Craps赌博游戏
    玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜
    如果摇出2点 3点 12点 庄家胜 其他情况游戏继续
    玩家再次要色子 如果摇出7点 庄家胜
    如果摇出第一次摇的点数 玩家胜
    否则游戏继续 玩家继续摇色子
    玩家进入游戏时有1000元的赌注 全部输光游戏结束

    """
    from random import randint

    money = 1000
    while money > 0:
        print('当前资产为： %d' % money)
        go_on = False
        # 下注
        while True:
            debt = int(input('请下注：'))
            if 0 < debt <= money:
                break

        first = randint(1, 6) + randint(1, 6)
        print('玩家摇出了 %d 点' % first)
        if first == 7 or first == 11:
            print('玩家胜！')
            money += debt
        elif first == 2 or first == 3 or first == 12:
            print('庄家胜!')
            money -= debt
        else:
            go_on = True

        while go_on:
            dice = randint(1, 6) + randint(1, 6)
            print('玩家摇出了 %d 点' % dice)
            if dice == 7:
                print('庄家胜！')
                money -= debt
                go_on = False
            elif dice == first:
                print('玩家胜！')
                money += debt
                go_on = False

    print('恭喜你破产了~')

craps()
