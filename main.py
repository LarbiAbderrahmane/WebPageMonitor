from classes.MyTelegramBot import MyTelegramBot
from classes.WebPageMonitor import WebPageMonitor
from classes.Helper import Helper
from datetime import datetime
import time

telegram = MyTelegramBot()
telegram.sendMessage("server is on!")

urls = [
    "http://www.usthb.dz",
    "http://fmi.univ-tiaret.dz/",
    "https://en.univ-blida.dz/",
    "https://www.univ-constantine2.dz/facntic/"
]

while True:
    for url in urls:
        print(f"***** {url} *****")
        result = url + " : " + "recorded in " + datetime.now().isoformat().replace("T", " ") + "\n"
        oldPageName = Helper.getFileNameFrom(url)
        with open("old_pages/" + oldPageName, "r") as f:
            oldPage = f.read()

        try:
            monitor = WebPageMonitor(url, oldPage)
        except Exception as e:
            print(url + " site is down!\n" + "error: " + str(e))
            continue

        textDifferences = monitor.getTextDifference()
        linksDifferences = monitor.getLinksDifference()
        if len(textDifferences) > 0:
            result += "\t\n**text differences:\n\n" + "\n".join(textDifferences) + "\n"
        if len(linksDifferences) > 0:
            result += "\t\n**links differences:\n\n" + "\n".join(linksDifferences) + "\n"

        if len(textDifferences) > 0 or len(linksDifferences) > 0:
            telegram.sendMessage(result)
            with open("old_pages/" + oldPageName, "w") as f:
                f.write(monitor.getNewHTML())

    time.sleep(5*60)
