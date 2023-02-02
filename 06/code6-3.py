class Geese:
    ''' 大雁類別'''

    def __init__(self,beak,wing,claw):
        print("我是大雁類別!我有以下特徵:")
        print(beak)
        print(wing)
        print(claw)
    def fly(self, state):
        print(state)

beak_1 = "喙的基部較高，長度和頭部的長度幾乎相等"
wing_1 = "翅膀長而尖"
claw_1 = "爪子是樸狀的"
wildGoose = Geese(beak_1,wing_1,claw_1)
wildGoose.fly("我飛行的時候，一會兒排成個人字，一會排成個一字")