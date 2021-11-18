from typing import Counter
import cv2
import urllib.request
import requests
import json
from copy import deepcopy
import os
import shutil
from bs4 import BeautifulSoup
import re
import cli
import time


# TODO input integrity check
# TODO error handling
# TODO filename dublication check, if true: filename(counter).jpg


def download_json(url):
    urllib.request.urlretrieve(url, "temp-files/json/data.json")


def open_json():
    file = open('temp-files/json/data.json',)
    return json.load(file)


def get_json_from_url(url):
    default_v1 = "https://vangoghmuseum-assetserver.appspot.com/tiles?id=5667465501605888"
    default_v2 = "https://vangoghmuseum-assetserver.appspot.com/tiles?id=5649007678324736"

    if url == "1":
        url = default_v1
    elif url == "2":
        url = default_v2
    else:
        url = find_json_on_page(url)

    download_json(url)
    return open_json()



def find_json_on_page(url):
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        for div in soup.find_all('div'):    
            if div.has_attr( "data-base-path" ):
                db = div['data-base-path']
            if div.has_attr( "data-id" ):
                id = div['data-id']
    except:
        notify_user("Error opening the URL")
    return db + id


def download_all_images(data, resolution):
    notify_user("Downloading image assets...")
    if resolution == "":
        resolution = 0
    else:
        resolution = int(resolution)

    cols = []
    rows = []
    last_row = 0
    for i in data["levels"][resolution]["tiles"]:
        img, row = download_single_image(i)
        if last_row < row:
            rows.append(deepcopy(cols))
            cols.clear()
            last_row = row
        cols.append(img)
    rows.append(cols)
    return rows


def download_single_image(i):
    row = i["y"]
    x = str(i["x"])
    y = str(row)
    url = i["url"]
    urllib.request.urlretrieve(url, "temp-files/tiles/" + x + "-" + y + ".jpg")
    return cv2.imread("temp-files/tiles/" + x + "-" + y + ".jpg"), row


def concatinate_matrix(matrix, filename):
    directory = "./"
    stack = []

    for i in matrix:
        stack.append(cv2.hconcat(i))

    final = cv2.vconcat(stack)
    cv2.imwrite(f"{directory}{filename}.jpg", final)
    notify_user(f"\n{filename}.jpg is saved in the app's folder\n")


def get_filename():
    filename = cli.user_prompt_name(False, "")
    if filename == "":
        filename = "downloaded_image"
    return filename


def create_temp_folders():
    path = os.getcwd() + "/temp-files"
    try:
        os.mkdir(path)
        os.mkdir(path + "/tiles")
        os.mkdir(path + "/json")
    except OSError:
        notify_user("Creation of the directory %s failed" % path)
    else:
        notify_user("Successfully created the directory %s " % path)
    return path


def delete_temp_folders(path):
    try:
        shutil.rmtree(path)
    except OSError:
        notify_user("Deletion of the directory %s failed" % path)
    else:
        notify_user("Successfully deleted the directory %s" % path)


def notify_user(msg):
    cli.notify_user(msg)


def run():
    path = create_temp_folders()
    url = cli.user_prompt_url()
    data = get_json_from_url(url)
    resolution = cli.user_prompt_resolution(data)
    matrix = download_all_images(data, resolution)
    filename = get_filename()
    concatinate_matrix(matrix, filename)
    delete_temp_folders(path)


if __name__ == '__main__':
    run()
