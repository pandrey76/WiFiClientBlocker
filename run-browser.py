
import pyautogui as pg
import time
from auth import password

# pg.moveTo(200, 200, 0.5)
# pg.drag(50, 50, 0.5, button='left')
# print(pg.position())
# pg.click(350, 350)

#pg.typewrite("Hello, world!")
#pg.typewrite(["enter"])

# pg.rightClick(250, 259)


# 
#pg.hotkey("winleft")
# Run browser
# ################
# pg.moveTo(20, 180, 0.5)
# pg.moveTo(250, 180, 0.5)
# pg.leftClick()

# i = 0
# while i<5:
#     pg.press("down")
#     i+=1
# pg.press("right")
# pg.press("enter")
# ################

time.sleep(5)

# pg.typewrite("www.youtube.com", 0.3)
# pg.typewrite(["enter"])

#pg.typewrite("http://192.168.1.254/index.htm", 0.1) # 0.3)
#pg.press("enter")
#time.sleep(10)
pg.typewrite("admin", 0.1)
# x, y = pg.position()
#pg.moveTo(x, y + 30)
#pg.leftClick()1
pg.press("tab")
pg.typewrite(password, 0.1)
pg.press("enter")
time.sleep(20)
i = 0
while i < 15:
    pg.press("tab")
    i += 1

pg.press("enter")
time.sleep(1)
pg.press("enter")
time.sleep(5)
pg.hotkey("alt", "f4")


