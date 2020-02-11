import random
import time

if __name__ == '__main__':
    fullness = random.randrange(5,90)
    print(fullness)
    while(True):
        opened = random.choice([True, False])
        if opened:
            if(fullness < 75):
                fullness += random.randrange(5,25)
            else:
                fullness = 0
        message = "{} : {}"
        print(message.format(opened,fullness))
        time.sleep(2)