#-*- coding: utf-8 -*-
import reminders
import sys
from datetime import datetime, timedelta
message = ["頑張ってるよ", "この調子！", "休憩した方がいい", "もうやめた方がいいよ", "やりすぎだよ","はい終了"]
if len(sys.argv) >= 3:
    interval = int(sys.argv[1])
    num = int(sys.argv[2])
else:
    print("input 'python set.py 時間間隔 回数'")
    sys.exit()

for i in range(1, num + 1):
    reminders.notify(title=str(i*interval)+'分経過', message=message[(i-1) % 4], delay= interval*(i))
    print("set:" + (datetime.now() + timedelta(minutes = i * interval)).strftime("%H:%M"))
