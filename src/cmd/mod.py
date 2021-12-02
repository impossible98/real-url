import sys
import constant.mod

import douyu.mod
import huya.mod


VERSION = constant.mod.VERSION

SHOW_VERSION = constant.mod.APP_NAME + "version: " + VERSION


def website():
    website = input("Enter website: ")

    if website.startswith("https://www.douyu.com/"):
        # Example: https://www.douyu.com/4044733
        show_version()
        print(len(SHOW_VERSION) * "=")
        douyu.mod.main(website)
    elif website.startswith("https://www.huya.com/"):
        # Example: https://www.huya.com/ruozhi
        show_version()
        print(len(SHOW_VERSION) * "=")
        huya.mod.main(website)
    else:
        print("Invalid website")


def show_version():
    print(SHOW_VERSION)


def main():
    if len(sys.argv) > 1:
        show_version()
    else:
        website()
