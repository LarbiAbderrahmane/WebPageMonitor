import requests
from lxml import etree
import urllib.parse
from classes.Helper import Helper


class WebPageMonitor:
    def __init__(self, url, oldHTML):
        response = requests.get(url, timeout=5)
        self.url = url
        self.html = response.text
        self.oldHTML = oldHTML

    def addHttpPrefix(self, domain: str):
        if domain.startswith("/"):
            return self.url + urllib.parse.quote(domain)
        else:
            return domain

    def findText(self, html):
        dom = etree.HTML(html)
        founds = dom.xpath("/html/body//*[name()!='script' and name()!='style'][text()]")
        texts = list(map(Helper.getText, founds))
        return texts

    def findLinks(self, html):
        dom = etree.HTML(html)
        founds = dom.xpath("/html/body//@href")
        links = list(founds)
        return links

    def getTextDifference(self):
        newTexts = self.findText(self.html)
        oldTexts = self.findText(self.oldHTML)
        return Helper.getDifference(newTexts, oldTexts)

    def getLinksDifference(self):
        newLinks = self.findLinks(self.html)
        oldLinks = self.findLinks(self.oldHTML)
        difference = Helper.getDifference(newLinks, oldLinks)
        return list(map(self.addHttpPrefix, difference))

    def getNewHTML(self):
        return self.html
