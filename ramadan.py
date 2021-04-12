import csv
import pyautogui as pg
import webbrowser as web
import time
with open('contacts.csv','r',encoding="utf8") as csv_file:
    flist = csv.reader(csv_file)
    next(flist)

    first = True

    for line in flist:
        messeg ="كل سنة وانت طيب يا "+ line[0].split()[0]+" ❤ ورمضان كريم عليك 😍"
        Pnumber = line[30]
        Pnumber = Pnumber.replace(" ","")
        if(len(Pnumber) == 11):
            Pnumber = "+2" + Pnumber
        print(Pnumber)
        print(messeg)
        time.sleep(4)
        web.open("https://web.whatsapp.com/send?phone=" + Pnumber + "&text=" + messeg)
        if first:
            time.sleep(6)
            first = False
        width, height = pg.size()
        pg.click(width / 2, height / 2)

        time.sleep(8)
        pg.press('enter')
        time.sleep(8)
        pg.hotkey('ctrl', 'w')





