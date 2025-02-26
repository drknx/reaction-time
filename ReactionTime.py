import pyautogui
import time
import webbrowser
import random

cpuSaver = 0.05 # delay to prevent extra load on the cpu
reactionTime = random.uniform(0,1) # reaction time (lowest, highest)

webbrowser.open('https://www.humanbenchmark.com/tests/reactiontime', new=2)
time.sleep(3) # change to how much time it takes to open up the site

width, height = pyautogui.size()
width, height = width // 7, height // 7

pyautogui.FAILSAFE = True

def is_mostly_green(rgb):
    r, g, b = rgb
    return g > r and g > b  # detects green

# if green is detected, then clicks
while True:
    try:
        color = pyautogui.pixel(width, height)

        if is_mostly_green(color):
            time.sleep(reactionTime) # clicked
            pyautogui.click()
            print("click")

            # b
            while is_mostly_green(pyautogui.pixel(width, height)):
                time.sleep(cpuSaver)

        time.sleep(cpuSaver)

    except Exception as e:
        print(f"Error: {e}")
        time.sleep(cpuSaver)

