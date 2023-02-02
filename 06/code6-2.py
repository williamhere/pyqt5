def fun_bmi(person,height,weight):
    print(person + "的身高:" + str(height) + "公尺\t 體重:" + str(weight) + "公斤")
    bmi = weight/(height*height)
    print(person + "的bmi指數為:" + str(bmi))

    if bmi < 18.5:
        print("您的體重過輕~@_@~\n")
    if bmi >= 18.5 and bmi < 24.9 :
        print("正常範圍，注意保持(-_-)\n")
    if bmi >= 24.9 and bmi <29.9:
        print("您的體重過重~@_@~\n")
    if bmi >= 29.9 :
        print("肥胖^@_@^\n")

fun_bmi("路人甲",1.83, 60)
fun_bmi("路人乙",1.60, 50)
