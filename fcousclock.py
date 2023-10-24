import time

def focus_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        minutes, secs = divmod(seconds, 60)
        timer = f'{minutes:02d}:{secs:02d}'
        print(timer, end='\r')
        time.sleep(1)
        seconds -= 1
    print("时间到！")

# 设置专注时长为25分钟（可以根据需要进行调整）
focus_timer(25)
