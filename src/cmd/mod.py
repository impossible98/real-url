import sys

import huya.mod

def website():
    website = input("Enter website: ")

    if website.startswith("https://www.douyu.com/"):
        print("https://www.douyu.com/4044733")
    elif website.startswith("https://www.huya.com/"):
        # Example: https://www.huya.com/ruozhi
        huya.mod.main(website)
    else:
        print("Invalid website")


def main():
    if len(sys.argv) > 1:
        print("No arguments")
    else:
        website()
