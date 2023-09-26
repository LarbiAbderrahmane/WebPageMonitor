from classes.WebPageMonitor import WebPageMonitor
from classes.Helper import Helper
from datetime import datetime
import time
import os.path


urls = list(map(lambda e: e.strip("\n"), open("urls.in", "r").readlines()))

output = open("result.out", "w")
while True:
    for url in urls:
        print(f"***** {url} *****")
        result = url + " : " + "recorded at " + datetime.now().isoformat().replace("T", " ") + "\n"
        oldPageName = "old_pages/" + Helper.getFileNameFrom(url)
        if os.path.isfile(oldPageName):
            with open(oldPageName, "r") as f:
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
                print(result)
                output.write(result)
                with open(oldPageName, "w") as f:
                    f.write(monitor.getNewHTML())

        if not os.path.isfile(oldPageName):
            print("creating fresh copy of the page...")
            with open(oldPageName, "w") as f:
                f.write(WebPageMonitor(url, None).getNewHTML())
    print("----- checking changes after 5 minutes... -----")
    time.sleep(5*60)
