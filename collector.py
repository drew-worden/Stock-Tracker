import pyautogui as pyauto
import time
import pandas as pd


typeOfData = eval(input("STOCKS (1)\nCRYPTO (2)\n"))
ticker = input("TICKER\n")
times = eval(input("ITERATIONS\n"))

if typeOfData == 1:
    url = "https://robinhood.com/" + "stocks" + "/" + ticker
else:
    url = "https://robinhood.com/" + "crypto" + "/" + ticker


def collectStockPrice(iterations):
    pyauto.click(210, 1070)
    pyauto.click(210, 50)
    pyauto.doubleClick()
    pyauto.press("backspace")
    pyauto.typewrite(url)
    pyauto.press("enter")
    time.sleep(2)

    for i in range(iterations):
        pyauto.moveTo(210, 200)
        pyauto.click(button="right")
        pyauto.click(215, 300)
        pyauto.keyDown("ctrl")
        pyauto.keyDown("c")
        pyauto.keyUp("ctrl")
        pyauto.keyUp("c")
        pyauto.click(700, 450)
        pyauto.click(500, 1070)
        pyauto.keyDown("ctrl")
        pyauto.keyDown("v")
        pyauto.keyUp("ctrl")
        pyauto.keyUp("v")
        pyauto.press("enter")
        time.sleep(3)
    
collectStockPrice(times)

pyauto.keyDown("ctrl")
pyauto.keyDown("s")
pyauto.keyUp("ctrl")
pyauto.keyUp("s")
pyauto.keyDown("ctrl")
pyauto.keyDown("w")
pyauto.keyUp("ctrl")
pyauto.keyUp("w")

collectedData = []

file = open("data.txt", "r")
for line in file:
    line = str(line)
    lineList = line.split(" ")
    value = lineList[2]
    numeric = value.split("$")
    numeric = numeric[1]
    collectedData.append(numeric)

print(collectedData)



