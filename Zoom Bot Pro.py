#import pyautogui
import win10toast
from time import sleep
import datetime
import webbrowser
toaster = win10toast.ToastNotifier()
classes = int(input("How many classes do you have? (MAX 7): "))      
if classes > 7:
    print("You picked a number higher than 7, reverting number to 7...") 
    classes = 7

zoom1 = False # Defines for the statement function later on 
zoom2 = False
zoom3 = False
zoom4 = False
zoom5 = False
zoom6 = False
zoom7 = False

zoomTimeList = []
zoomLinkList = []

# TODO Refactor into one loop

if classes >= 1:
    zoom1 = True
    zoomTime1 = input("What time is your first zoom? Format:(Hour.Minute): ")
    late1 = input("Is your zoom in the AM or PM? Format:(AM OR PM): ")
    link1 = input("Your zoom class link: ")
    time = zoomTime1.split(".")
    zoomHour1 = int(time[0])
    PM = "pm" or "PM"
    if late1 == PM:
        zoomHour1 = zoomHour1 + 12
    zoomTime1 = str(zoomHour1) + "." + time[1]
    zoomTimeList.append(zoomTime1)
    zoomLinkList.append(link1)
    if classes >= 2:
        zoom2 = True
        zoomTime2 = input("What time is your second zoom? Format:(Hour.Minute): ")
        late2 = input("Is your zoom in the AM or PM? Format:(AM OR PM): ")
        link2 = input("Your zoom class link: ")
        pm2 = "PM" or "pm"
        time = zoomTime2.split(".")
        zoomHour2 = int(time[0])
        PM = "pm" or "PM"
        if late2 == PM:
            zoomHour2 = zoomHour2 + 12
        zoomTime2 = str(zoomHour2) + "." + time[1]
        zoomTimeList.append(zoomTime2)
        zoomLinkList.append(link2)
        if classes >= 3:
            zoom3 = True
            zoomTime3 = input("What time is your third zoom? Format:(Hour.Minute): ")
            late3 = input("Is your zoom in the AM or PM? Format:(AM OR PM): ")
            link3 = input("Your zoom class link: ")
            pm3 = "PM" or "pm"
            time = zoomTime3.split(".")
            zoomHour3 = int(time[0])
            PM = "pm" or "PM"
            if late3 == PM:
                zoomHour3 = zoomHour3 + 12
            zoomTime3 = str(zoomHour3) + "." + time[1]
            zoomTimeList.append(zoomTime3)
            zoomLinkList.append(link3)
            if classes >= 4:
                zoom4 = True
                zoomTime4 = input("What time is your fourth zoom? Format:(Hour.Minute): ")
                late4 = input("Is your zoom in the AM or PM? Format:(AM OR PM): ")
                link4 = input("Your zoom class link: ")
                pm4 = "PM" or "pm"
                time = zoomTime4.split(".")
                zoomHour4 = int(time[0])
                PM = "pm" or "PM"
                if late4 == PM:
                    zoomHour4 = zoomHour4 + 12
                zoomTime4 = str(zoomHour4) + "." + time[1]
                zoomLinkList.append(link4)
                zoomTimeList.append(zoomTime4)
                if classes >= 5:
                    zoom5 = True
                    zoomTime5 = input("What time is your fifth zoom? Format:(Hour.Minute): ")
                    late5 = input("Is your zoom in the AM or PM? Format:(AM OR PM): ")
                    link5 = input("Your zoom class link: ")
                    pm5 = "PM" or "pm"
                    time = zoomTime5.split(".")
                    zoomHour5 = int(time[0])
                    PM = "pm" or "PM"
                    if late5 == PM:
                        zoomHour5 = zoomHour5 + 12
                    zoomTime5 = str(zoomHour5) + "." + time[1]
                    zoomTimeList.append(zoomTime5)
                    zoomLinkList.append(link5)
                    if classes >= 6:
                        zoom6 = True
                        zoomTime6 = input("What time is your sixth zoom? Format:(Hour.Minute): ")
                        late6 = input("Is your zoom in the AM or PM? Format:(AM OR PM): ")
                        link6 = input("Your zoom class link: ")
                        pm6 = "PM" or "pm"
                        time = zoomTime6.split(".")
                        zoomHour6 = int(time[0])
                        PM = "pm" or "PM"
                        if late6 == PM:
                            zoomHour6 = zoomHour6 + 12
                        zoomTime6 = str(zoomHour6) + "." + time[1]
                        zoomLinkList.append(link6)
                        zoomTimeList.append(zoomTime6)
                        if classes >= 7:
                            zoom7 = True
                            zoomTime7 = input("What time is your seventh zoom? Format:(Hour.Minute): ")
                            late7 = input("Is your zoom in the AM or PM? Format:(AM OR PM): ")
                            link7 = input("Your zoom class link: ")
                            pm7 = "PM" or "pm"
                            time = zoomTime7.split(".")
                            zoomHour7 = int(time[0])
                            PM = "pm" or "PM"
                            if late7 == PM:
                                zoomHour7 = zoomHour7 + 12
                            zoomTime7 = str(zoomHour7) + "." + time[1]
                            zoomLinkList.append(link7)
                            zoomTimeList.append(zoomTime7)

def Statement(): #Code written a while ago, can be edited for a switch method 
    if zoom1 == True:
        print ("-=Launching your first zoom at " + zoomTime1 + " " + late1 + "=-")
    else:
        print("N/A")
    if zoom2 == True:
        print ("-=Launching your second zoom at " + zoomTime2 + " " + late2 + "=-") 
    else:
        print("N/A")
    if zoom3 == True:
        print ("-=Launching your third zoom at " + zoomTime3 + " " + late3 + "=-")
    else:
        print("N/A")
    if zoom4 == True:
        print ("-=Launching your fourth zoom at " + zoomTime4 + " " + late4 + "=-")
    else:
        print("N/A")
    if zoom5 == True:
        print ("-=Launching your fifth zoom at " + zoomTime5 + " " + late5 + "=-")
    else:
        print("N/A")        
    if zoom6 == True:
        print ("-=Launching your sixth zoom at " + zoomTime6 + " " + late6 + "=-")
    else:
        print("N/A")
    if zoom7 == True:
        print ("-=Launching your seventh zoom at " + zoomTime7 + " " + late7 + "=-")
    else:
        print("N/A")

Statement()


x = 0

while x < len(zoomTimeList): #loops through and will get the proper zoom based off of the time
    now = datetime.datetime.now()
    nowHour = now.hour
    nowMinute = now.minute
    zoomTime = zoomTimeList[x]
    args = zoomTime.split(".")
    zoomHour = int(args[0])
    zoomMinute = int(args[1])
    if zoomHour == nowHour:
        if zoomMinute == nowMinute:
            webbrowser.open(zoomLinkList[x])
            toaster.show_toast("Zoom Bot", "Your zoom is launching!")         
            x = x + 1       
    sleep(10)

        