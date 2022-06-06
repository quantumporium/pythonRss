#!/usr/bin/env python
"""PythonRss 0.0.1

Usage:
    python pythonRss.py <rss-url>
    python pythonRss.py

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
            userChoice = input("The url is no valid, do you whant to enter another one? (yes/no) ")
            if userChoice.startswith('y'):
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

# starting to get tired of this codebase :
def dealwithhRssUrl(url):
    quit = False

    feed = feedparser.parse(url)
    post = feed.entries
    for i in range(len(feed['entries'])):
        print(f"[{i}] {post[i]['author']}: {post[i]['title']} \n")


    while not quit:
        userChoice = input("What post do you whant to see >> ")
    # print(f"[ debug ] {userChoice} {len(feed.entries)} {int(userChoice) in range(len(feed['entries']))}")
        if int(userChoice) in range(len(feed['entries'])):
            webbrowser.open_new(post[int(userChoice)]['link'])
        else:
            print("An error occure the program will shutdown")
            exit()

        userOption = input("Do you whant to quit? (yes/no):  ")
        if userOption.lower().startswith("y"):
            continue
            #print("[ debug ] this part is working ")
        else:
            quit = True
            #print("[ debug ] this part should not be working ")

    return


def main():
    if checkInternetConnection():

        if len(sys.argv) == 2:
            url = validateUrl(sys.argv[1])
            dealwithhRssUrl(url)
            print("Thanks for using PythonRss")
        else:
            programIntroduction()
            url = getURL()
            # print(f"[ debug ] {url}")
            dealwithhRssUrl(url)
            print("Thanks for using pythonRss")
    else:
        print("Sorry, we couldn't find a internet connection.")
    return 0


main()
