#!/usr/bin/env python
"""PythonRss 0.0.1

Usage:
    feed <rss-url>


"""
import sys
import urllib.request as urlRequest
import feedparser
import webbrowser


def checkInternetConnection():
    try:
        urlRequest.urlopen('https://www.google.ca')
        return True
    except:
        return False

def programIntroduction():
    print("""pythonRss - a simple RSS feed reader
Welcome thanks for using this software and hope you like it
You can quit at any moment by typing ctrl+c.\n
    """)
    return

def getURL():
    while( True ):
        url = input("Enter the RSS fedd url: ")
        try:
            urlRequest.urlopen(url)
            return url
        except:
            userChoice = input("The url is no valid, do you whant to enter another one?")
            if userChoice.startwith('y'):
                continue
            else:
                print("You choose not to continue, the progam will close shortly.")
                exit()

def validateUrl(url):
    try:
        response = urlRequest.urlopen(url)
        return url
    except:
        print("The url you gave isn't valid.")
        exit()


def getTerminalParameter():
    if sys.argv == 2:
        return  sys.argv[2]
    else:
        return False


def parseRssUrl(url):
    feed = feedparser.parse(url)
    post = feed.entries
    for i in range(10):
        print(f"[{i}] {post[i]['author']}: {post[i]['title']}\n")
    return

# starting to get tired of this codebas :
def dealwithhRssUrl(url):
    feed = feedparser.parse(url)
    post = feed.entries
    for i in range(len(feed['entries'])):
        print(f"[{i + 1}] {post[i]['author']}: {post[i]['title']} \n")

    userChoice = input("What post do you whant to see >> ")

    if userChoice not in range(len(feed['entries'])):
        webbrowser.open_new(post[int(userChoice)]['link'])
    else:
        print("An error occure the program will shutdown")
        exit()

    return


def main():
    if checkInternetConnection():

        if len(sys.argv) == 2:
            url = validateUrl(sys.argv[1])
            dealwithhRssUrl(url)
        else:
            programIntroduction()

    else:
        print("Sorry, we couldn't find a internet connection.")
    return 0


main()
