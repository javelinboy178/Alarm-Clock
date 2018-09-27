import datetime
import argparse, random
from selenium import webdriver

# Main Function
def main():

    # Arg parse for hour minute second will set to 00 if none suplied
    parser = argparse.ArgumentParser(description="Simple alarm Clock")
    parser.add_argument("--hour", type=int, help="Hour in 24 hour clock")
    parser.add_argument("-m", "--minute", type=int, help="Minutes")
    parser.add_argument("-s", "--secounds", type=int, help="Secounds")
    args = parser.parse_args()

    hour = args.hour
    minute = args.minute
    secound = args.secounds

    hour = str(hour)
    minute = str(minute)
    secound = str(secound)

    if hour is None:
        hour = "00"
    if minute is None:
        minute = "00"
    if secound is None:
        minute = "00"

    if len(hour) < 2:
        hour = "0" + hour
    if len(minute) < 2:
        minute = "0" + minute
    if len(secound) < 2:
        secound = "0" + secound

    alarm_time = hour + ":" + minute + ":" + secound

    while True:
        time_now = datetime.datetime.now().time().replace(microsecond=0)
        time_now = str(time_now)

        if alarm_time == time_now:
            browser = webdriver.Chrome()
            f = open('youtube.txt', 'r')
            line_list = [i for i in f if len(i) > 1]
            browser.get(random.choice(line_list))


main()






