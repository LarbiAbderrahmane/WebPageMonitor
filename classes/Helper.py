import urllib.parse
import re


class Helper:
    def getText(e):
        if e.text != None:
            return e.text.strip()
        else:
            return ""

    def getDifference(new, old):
        return [t for t in new if not (t in old)]

    def getFileNameFrom(url):
        return "".join(re.findall("\w+", urllib.parse.urlparse(url).netloc)) + ".html"
