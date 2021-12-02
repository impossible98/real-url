import sys


def website():
    website = input("Enter website: ")

    if website.startswith("https://www.douyu.com/"):
        print("https://www.douyu.com/4044733")
    elif website.startswith("https://www.huya.com/"):
        print("https://www.huya.com/ruozhi")
    else:
        print("Invalid website")


def main():
    if len(sys.argv) > 1:
        print("No arguments")
    else:
        website()
