import pyautogui as pg
import time
import sys

def do_something():
    #click on property
    pg.moveTo(5920,1182, duration=0.5)
    pg.click()
    time.sleep(3)

    #rename
    pg.moveTo(5456,1122, duration=0.5)
    pg.click()
    time.sleep(0.5)
    pg.click()
    time.sleep(0.5)
    pg.typewrite(["backspace","5"])
    time.sleep(0.5)

    #move to estimate
    pg.moveTo(5764,828, duration=0.5)
    pg.click()
    time.sleep(4)

    #delete 6' lot
    pg.moveTo(5486,1404,duration=1)
    pg.click()
    time.sleep(1)

    pg.moveTo(7952,2130,duration=1)
    pg.click()
    pg.moveTo(8018,2282,duration=0.5)
    pg.click()
    pg.moveTo(7284,1858,duration=0.5)
    pg.click()

    pg.moveTo(7952,2044,duration=1)
    pg.click()
    pg.moveTo(8018,2172,duration=0.5)
    pg.click()
    pg.moveTo(7284,1858,duration=0.5)
    pg.click()

    pg.moveTo(7952,1946,duration=1)
    pg.click()
    pg.moveTo(8018,2086,duration=0.5)
    pg.click()
    pg.moveTo(7284,1858,duration=0.5)
    pg.click()

    pg.moveTo(7952,1878,duration=1)
    pg.click()
    pg.moveTo(8018,2018,duration=0.5)
    pg.click()
    pg.moveTo(7284,1858,duration=0.5)
    pg.click()

    pg.moveTo(7952,1812,duration=1)
    pg.click()
    pg.moveTo(8018,1950,duration=0.5)
    pg.click()
    pg.moveTo(7284,1858,duration=0.5)
    pg.click()

    time.sleep(1)

    #delete 6' sidewalk
    pg.moveTo(5484,2210,duration=1)
    pg.click()
    time.sleep(1)

    pg.scroll(-500)

    pg.moveTo(7950,2246,duration=1)
    pg.click()
    pg.moveTo(7972,2384,duration=0.5)
    pg.click()
    pg.moveTo(7280,1834,duration=0.5)
    pg.click()

    time.sleep(0.5)

    pg.moveTo(7960,2250,duration=1)
    pg.click()
    pg.moveTo(7984,2394,duration=0.5)
    pg.click()
    pg.moveTo(7264,1848,duration=0.5)
    pg.click()

    #Update Kit
    pg.moveTo(5490,2406,duration=1)
    pg.click()
    pg.moveTo(5532,2472,duration=0.5)
    pg.click()
    time.sleep(3)
    pg.moveTo(6264,2060,duration=0.5)
    pg.click()
    pg.typewrite("726")

    #update end date
    pg.moveTo(5498,838,duration=0.5)
    pg.click()
    time.sleep(3)
    pg.moveTo(7068,1608,duration=0.5)
    pg.click()
    pg.typewrite(["backspace", "5"])

    #save and exit
    time.sleep(1)
    pg.moveTo(8700,936,duration=0.5)
    pg.click()


    time.sleep(5)

    pg.moveTo(5180,1476,duration=0.5)
    pg.click()

    time.sleep(4)

while True:
        try:
            do_something()
        except KeyboardInterrupt:
            break