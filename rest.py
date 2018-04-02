#-*- coding: utf-8 -*-
import reminders
import sys 

message = ["休憩終了！", "終了だって．", "終わりでーす"] 
if len(sys.argv) >= 3:
    interval = int(sys.argv[1]) #時間間隔
    num = int(sys.argv[2]) #回数
else:
    print("input'python rest.py  時間間隔 回数'")
    sys.exit()

for i in range(1, num + 1):
    reminders.notify(title=str(i*interval)+'分経過', message=message[(i-1) % 3], delay= interval*i)

