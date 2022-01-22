
# instaPostBOT

**this is a bot coded using python, all it does is post a picture from a specified folder to Instagram.**

## Use case?
going on a holiday ? have a meme profile?...etc.  all you have to do is save what you want to post to a folder and the bot will take sure to post them later one by one.

## Installation

please note this bot is using a non official Instagram API [instagrapi](https://adw0rd.github.io/instagrapi/)
you can install it by running the command 

    pip install instagrapi

## Configuration
to configure the bot first thing is to open:

    configs.py

make sure to change the username and password to yours

    username = "username" 
    password = "password"
also make sure to change the picsFolderPath to yours

    picsFolderPath = "C://Users//UserName//Desktop//instaBot//pics//"
you also can change the duration between every post

    sleepDuration = random.randint(3600, 6 * 3600) 

it is set by defaults to post every hour to 6 hours, you can change that either to a fixed period or random 

## Notes

 1. Please make sure the images you provide respect Instagram's image
    aspect Ratio.
 2. please note that this is a 20min project, so there may be problems
    that you may run into.
 3. you take full responsibility for running this bot because it is
    using unofficial API.

## Run The BOT

you can simply run this bot by running the following command

    python run.py

## NEXT?
well I will add more features every now and then to this project, posting videos, reels and stories.
*or you can do that and commit it :3*




