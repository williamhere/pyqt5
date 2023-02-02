class Geese:
    neck = "脖子很長"
    wing = "振翅頻率高"
    leg = "腿位於身體的中心點，行走自如"
    number = 0
    def __init__(self):
        Geese.number += 1
        print("\n我是第"+str(Geese.number)+"隻大雁，我屬於雁類別!我有以下特徵:")
        print(Geese.neck)
        print(Geese.wing)
        print(Geese.leg)

list1 = []
for i in range(4):
    list1.append(Geese())
print("一共有"+str(Geese.number)+"隻大雁")