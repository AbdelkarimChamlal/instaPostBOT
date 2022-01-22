from instagrapi import Client
import configs
import os
import time
from PIL import Image


# log in into your insta account
cl = Client()
cl.login(configs.username, configs.password)

# keep the account running for ever until it is forced to close
while True:
    try:
        # load all the files in the pictures folder
        files = os.listdir(configs.picsFolderPath)
        imageTitle = ""
        for file in files:
            imageTitleTemp = file.title()
            imagePath = configs.picsFolderPath + imageTitleTemp
            # get the image size
            im = Image.open(imagePath)
            width, height = im.size
            im.close()
            ratio = height / width
            # look for the first picture to respect instagram's pictures aspect ratio
            if ratio in configs.allowedAspectRatios:
                # save image title
                imageTitle = imageTitleTemp
                # break
                break
        files.clear()
        # check if there is a picture that respects instagram's pictures aspect ratio
        if imageTitle != "":
            # post it
            imagePath = configs.picsFolderPath + imageTitle
            media = cl.photo_upload(
                imagePath,
                "description here"
            )
            print(imageTitle)

            # delete it from the folder so next time it will not be posted
            os.remove(configs.picsFolderPath + imageTitle)
    # exception to make sure the bot will keep working if the network is down
    except:
        print("error while trying to post")

    time.sleep(configs.sleepDuration)
