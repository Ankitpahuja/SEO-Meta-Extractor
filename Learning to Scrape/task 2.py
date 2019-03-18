from processing import *
from requests_html import HTMLSession
import csv
import re
session = HTMLSession()

# Write an algorithms to find most used 10 keywords from the generated list.This is what is supposed to go in the keywords list in the excel.


# Functions relating to Task 1
def getTitle(response):
    title = response.html.find(".entry-title", first=True)
    print(title.text)
    return title.text

def getDescription(response):
    description_xpath = '/html/head/meta[5]'
    description = response.html.xpath(description_xpath, clean=True)
    return description

def getWordFrequency(response):
    pageContent = response.html.find(".entry-content", first=True)
    wordlist = pageContent.text.split()
    Words = removeStopwords(wordlist, stopwords)
    wordFreq = []
    for w in Words:
        wordFreq.append(Words.count(w))
    termFrequency = dict(zip(Words, wordFreq))
    termFrequencyOutput = sortFreqDict(termFrequency)
    return termFrequencyOutput[:15]

def getOnlyKeywords(wordFrequency):
    keywordList = []
    for keyword in wordFrequency:
        keywordList.append(keyword[1])
    return keywordList

def getKeywords(response):
    wordFrequency = getWordFrequency(response)
    Keywords = getOnlyKeywords(wordFrequency)

    return Keywords

def getDescriptionSanitized(Description):
    result = re.search(r"(?<==)'(\w+).*\.'", str(Description))
    return result.group(0)


def extractInformation(url=None):
    if url is None:
        print("You need to give a url atleast.")
        return None
    response = session.get(url)
    Title = getTitle(response)
    Description = getDescription(response)
    Keywords = getKeywords(response)
    # descSanity = getDescriptionSanitized(Description)
    return Title, Description, Keywords

# Functions relating to Task 3

def doFileOperations(Title, Description, Keywords):
    with open("output.csv", "a") as csvFile:
        row = [Title, Description, Keywords]
        writer = csv.writer(csvFile)
        writer.writerow(row)
    csvFile.close()

#Task 2
# urls = [] # List of all the urls from a sitemap tool
# with open("links.csv", "r") as links:
#         urls = links.readlines()
#         urls =[x.strip() for x in urls]
#
# print(urls)
for url in urls:
    Title, Description, Keywords = extractInformation(url)
    doFileOperations(Title, Description, Keywords)