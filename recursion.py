import time


def counter_down(i):
    print(i)
    if i <= 0:
        return
    else:
        counter_down(i-1)
        f = i * i
        print(f)
        print('else')
        time.sleep(0.10)

counter_down(900)
