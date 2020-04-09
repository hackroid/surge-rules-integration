import requests
import sys
import os

TMP_DIR = "./tmp"
SUB_URL_FILE = "./tmp/sub_url.txt"
SUB_CONF = "./tmp/sub.conf"


def file_dl(url, write_dir):
    file = requests.get(url)
    open(write_dir, 'wb').write(file.content)


def sub_dl(url):
    file_dl(url, SUB_CONF)


def sub_url_reader():
    if not os.path.exists(TMP_DIR):
        print("TMP dir not found, creating...")
        os.makedirs(TMP_DIR)
    else:
        print("TMP dir found")
    if not os.path.exists(SUB_URL_FILE):
        print("SUB_FILE not found, creating...")
        file = open(SUB_URL_FILE, 'w')
        file.close()
        print("SUB_FILE created at \"{}\"".format(SUB_URL_FILE))
        print("Pls add your sub link to the first line of SUB_FILE, then restart this script.")
        print("Exiting...")
        sys.exit()
    else:
        print("SUB_FILE found, reading...")
    f = open(SUB_URL_FILE, "r")
    url = f.readline()
    print("SUB_FILE url is: {}".format(url))
    return url


def main():
    sub_url = sub_url_reader()
    sub_dl(sub_url)


if __name__ == '__main__':
    main()
