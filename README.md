# InstagramBot
The InstagramBot is a Python program with a GUI that allows you to automatically like posts in your selected "hashtags" from the Instagram explore page.
Created using the Chromedriver and Selenium webdriver, this bot is designed to help you gain more traffic to your own page automatically.
Users are allowed to select how many hashtags they would like to explore from and how many pictures to like per hashtag.


#### Note this only works for Google Chrome, also this was made in early 2018, I was 13 at that time and my code was extremely sloppy :)


#### An example would be: food, nyc and pictures per hashtag as 5. This way the bot will like 5 pictures from each hashtag respectively.

## How To Install
First begin by having Python already installed, make sure you setup the enviroment variables correctly to launch Python from it's installed location.

Now for adding the chromedriver, for this step please make sure you know what version of Google Chrome you are using. To do so follow this
1) Click on the Menu icon in the upper right corner of the screen.
2) Click on Help, and then About Google Chrome.
3) Your Chrome browser version number can be found here.

Once you find your chrome version, proceed to this website https://chromedriver.chromium.org and download the respective chromedriver based on your Google Chrome version.

Example: Google Chrome version of 77, download chromedriver V77

Once you download it, go to your Python installation directory and move the chromedriver exe file into the root directory.

And that's it! Now it should run fine.

In case it doesn't or if you want to mention a location from where the chromedriver is to be fetched, you can modify the driver assingment line.

## How To Use
Start by running the Python file, it should launch a GUI.
Continue by entering your Instagram login details and adding as many hashtags as you like with each one being seperated by a "," Eg. food, nyc.
Next, select how many pictures you want the bot to like per hashtag, don't put a really large number or your account could get blocked.
And then click run! 
