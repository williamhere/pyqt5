def function_tips():
    '''功能:每天輸出一筆勵志文字'''
    import datetime
    mot = ["堅持下去不是因為我很堅強，而是因為我別無選擇",
           "含淚破種的人一定能笑著收穫",
           "做對的事情比把事情做對更重要",
           "命運給予我們的不是失望之酒，而是機會之杯",
           "不要等到明天，明天太遙遠，今天就行動",
           "若知若機，虛心若愚",
           "成功將屬於那些從不說不可能的人"]
    day = datetime.datetime.now().weekday()
    print(mot[day])

function_tips()