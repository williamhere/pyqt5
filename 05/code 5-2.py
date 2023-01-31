# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("熱門綜藝名稱:")  # Press Ctrl+F8 to toggle the breakpoint.
    art = ["嚮往的生活","歌手","中國好聲音","巧手神探","歡樂喜劇人","笑傲江湖","奔跑八","王牌對王牌","吐槽大會","奇筢說"]
    for index,item in enumerate(art) :
        if index%2 == 0:
            print(item +"\t\t",end='')
        else:
            print(item +"\n")
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
