import time
from datetime import datetime as dt
import os

# Enter the site name which you want to block
sites_to_block = [
    "www.facebook.com",
    "facebook.com",
    "www.youtube.com",
    "youtube.com",
    "www.gmail.com",
    "gmail.com",
]

# different hosts for different os
Linux_host = "/etc/hosts"
Window_host = r"C:\Windows\System32\drivers\etc\hosts"
default_hoster = Linux_host # if you are on windows then change it to Window_host
redirect = "127.0.0.1"


if os.name == 'posix':
    default_hoster = Linux_host

elif os.name == 'nt':
    default_hoster = Window_host
else:
    print("OS Unknown")
    exit()


def block_websites(start_hour, end_hour):
    #TODO Need to finish this code


if __name__ == "__main__":
    block_websites(9, 21)
