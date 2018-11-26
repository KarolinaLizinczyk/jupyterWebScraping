from urllib.request import urlopen
import re

wiki = "https://en.wikipedia.org/wiki/List_of_Presidents_of_the_United_States"

def getPresidents(url):
    res = urlopen(url).read().decode('utf-8')
    tableTag = re.findall(r'<table(.*?)</table>', res, re.M | re.I | re.S)[1]
    trTags = re.findall(r'<tr(.*?)</tr>', tableTag, re.M | re.I | re.S)

    urlList = []

    for i in range(len(trTags) - 1, 0, -1):
        bigTags = re.findall(r'<big>(.*?)</big>', trTags[i], re.M | re.I | re.S)
        for i in range(0, len(bigTags), 1):
            url = re.findall(r'<a href=\"(.*?)\" title=', bigTags[i], re.M | re.I | re.S)
            fullUrl = 'https://en.wikipedia.org' + url[0]
            if fullUrl not in urlList:
                urlList.append(fullUrl)

    return urlList

allPresidentUrls = getPresidents(wiki)

def getBirthdays(urls):
    for i in range(0, len(urls), 1):
        presidentName = (urls[i].split("/")[-1]).replace("_", " ")
        res = urlopen(urls[i]).read().decode('utf-8')
        bornTr = re.findall(r'<span class="bday">(.*?)</span>', res, re.M | re.I | re.S)
        print(presidentName)
        print(bornTr[0])

getBirthdays(allPresidentUrls)