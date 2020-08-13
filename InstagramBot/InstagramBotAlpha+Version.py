import tkinter as tk
from selenium import webdriver
import time
import threading
import random
import sys 
import mysql.connector
from mysql.connector import errorcode
from datetime import datetime
from tkinter import *
from tkinter import ttk
from time import strftime 
from tkinter import messagebox
from selenium.webdriver.support import expected_conditions as EC
import mysql.connector
import datetime
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options




class InstagramBot():
    # Run page
    
    def Gui(self):
    # Load application
        
        try:
            root = tk.Tk()
            root.lift()

            
            root.title("Instagram Bot - Created By HudZah")
            menubar = Menu(root)

            print("Application loading, please wait \n\n")
            print("When you install this application, you agree to the abide by the Terms And Conditions stated in the installtion folder. This software is not intended to be used for the exploitation of Instagram, rather as a means of promoting your product. Any detention or suspension that is resulted due to excessive use of this Bot is in no means the fault of the publisher, but the consequences faced by the user. It should be clear that this Bot should not be misused or overused, this might result in unknown penalties to be faced by the user." + "\n Created by HudZah") 

            Border = 3
            
            MEDIUM_FONT= ("Verdana", 12)
            LARGE_FONT= ("Arial", 12)


            # Creating Canvas
            canvas = tk.Canvas(root, width=600, height=630)
            canvas.pack()
            MainFrame = tk.Frame(root, bg="white")
            MainFrame.place(relwidth=1, relheight=1)

            # Adding file menu and commands
            file = Menu(menubar, tearoff = 0)
            menubar.add_cascade(label = "Run", menu = file)
            file.add_command(label ='Run', command=lambda:self.Threader(Username.get(), Password.get(), List.get(), PicsInput.get(), BackgroundRun.get())) 
            file.add_separator() 
            file.add_command(label ='Exit', command = root.destroy) 

            # Username label
            UsernameFrame = tk.Frame(root, bg="lightgrey", bd=Border)
            UsernameFrame.place(relx=0.5, rely=0.135, relwidth=0.60,
                                relheight=0.1, anchor="n")

            Username = ttk.Entry(UsernameFrame, font=LARGE_FONT)
            #Username.insert(0, "Username")
            Username.insert(0, "hudzah")
            Username.place(relwidth=1, relheight=1)
            Username.focus()

            # Password label
            PasswordFrame = tk.Frame(root, bg="lightgrey", bd=Border)
            PasswordFrame.place(relx=0.5, rely=0.26, relwidth=0.60,
                                relheight=0.1, anchor="n")

            Password = ttk.Entry(PasswordFrame, show="*",  font=LARGE_FONT)
            #Password.insert(0, "Password")
            Password.insert(0, "HUdhayfart_123")
            Password.place(relwidth=1, relheight=1)

            # Hashtags label
            ListFrame = tk.Frame(root, bg="lightgrey", bd=Border)
            ListFrame.place(relx=0.5, rely=0.385, relwidth=0.60,
                            relheight=0.1, anchor="n")

            List = ttk.Entry(ListFrame, font=LARGE_FONT)
            #List.insert(0, "Explore Hashtags, eg: food, nyc")
            List.insert(0, "food, nyc")
            List.place(relwidth=1, relheight=1)

            # Number of pictures dropdown
            PicsInput = Spinbox(root, from_= 5, to = 2000, font = LARGE_FONT)
            PicsInput.place(relx=0.35, rely=0.61, relwidth=0.14,
                        relheight=0.055, anchor = "n")

            BackgroundRun = IntVar()
            c = Checkbutton(root, text="Run in the background", variable=BackgroundRun, onvalue=1, offvalue=0, bg=None)
            c.place(relx=0.65, rely=0.61, relwidth=0.3,
                        relheight=0.055, anchor = "n")
            
            c.configure(background='white')


            # Run button
            button = ttk.Button(MainFrame, text="Run",
                            command=lambda:self.Threader(Username.get(), Password.get(), List.get(), PicsInput.get(), BackgroundRun.get()))
            
            button.place(relx=0.5, rely=0.71, relwidth=0.25,
                        relheight=0.085, anchor="n")           
            
            # Quit button
            Quitbutton = ttk.Button(MainFrame, text="Quit",
                            command= lambda:self.CloseThreader())

            Quitbutton.place(relx=0.5, rely=0.81, relwidth=0.25,
                        relheight=0.085, anchor="n")


            label = ttk.Label(root, text = "Created by HudZah © 2019", font=MEDIUM_FONT)
            label.place(relx = 0.5, rely = 0.93, anchor = "n")

            PicsInputLabel = ttk.Label(root, text = "Pictures Per Hashtag", font=MEDIUM_FONT)
            PicsInputLabel.place(relx = 0.35, rely = 0.55, relwidth = 0.3, anchor = "n")


            # Create label to show errors to users and Info of bot when closed
            root.config(menu = menubar)
            root.mainloop() 
        except Exception:
            print("Failed to create gui")

    def CheckUserInfo(self, username, password, hashtagReceived, nOfPics, BackgroundRun):

        
        browserCount.append(nOfPics)
        if username and username != "Username":
            pass
            if password and len(password) > 5:
                pass
                if hashtagReceived and hashtagReceived != "Explore Hashtags, eg: food, nyc":
                    pass
                    if int(nOfPics) > 0 and int(nOfPics) < 2000:
                        browserRunning = self.IsBrowserRunning(browserCount)
                        print(browserRunning,browserCount)
                        if browserRunning == False:
                            if messagebox.askokcancel('Application','Application is running, press OK to continue') == True:

                                try:
                                    pages = int(nOfPics)/10
                                    pages = int(pages)
                                    if pages < 1:
                                        pages = 1
                                    else:
                                        pass

                                except Exception:
                                    messagebox.showwarning("Error", "An error has occured")

                                infoError = False
                            
                            else:
                                browserRunning = False
                                browserCount.clear()

                        else:
                            messagebox.showerror("Multiple Instances", "Only one instance of the program can be run at a time. Please wait")
                            print("Only one instance of the program can be run at a time!")

                    else:
                        messagebox.showwarning("Error", "Please enter a valid number of posts to like")
                        print("Please enter a valid number of posts to like")                      
                else:
                    messagebox.showwarning("Error", "Please enter your correct information.")
                    print("Please enter suitable data")
            else:
                messagebox.showwarning("Error", "Please enter your correct information.")
                print("Please enter suitable data")
        else:
            messagebox.showwarning('Error', 'Please enter a username or password')
            print("Please enter a username and password")

        try:
            if infoError == False and browserRunning == False:
                self.Login(username, password, hashtagReceived, nOfPics, pages, BackgroundRun)

            else:
                print("Multiple instances or wrong information\n")
        except:
            pass

    def Threader(self, username, password, hashtagReceived, nOfPics, BackgroundRun):

        #Start a new thread to run the webdriver seperately to stop the gui from freezing
        t1 = threading.Thread(target = self.CheckUserInfo, args = (username, password, hashtagReceived, nOfPics, BackgroundRun))
        t1.start()

    def CloseThreader(self):
        
        t2 = threading.Thread(target=self.CloseBrowser)
        print("Close threader")
        t2.start()
        #self.CloseBrowser()
        
    
    def CloseBrowser(self):
        try:
            browserRunning = False
            browserCount.clear()
            self.driver.quit()
            print("Browser quit\n")
            
        except Exception as e:
            print(e)
            pass

    def Login(self, username, password, hashtagReceived, nOfPics, pages, BackgroundRun):

        browserRunning = True
        self.username = username
        self.password = password
        self.BackgroundRun = BackgroundRun
        hashtags = []
        hashtags = hashtagReceived.split(",")
        hashtagsOut = False
        i = 0

        if BackgroundRun == 1:
                    
                options = Options()
                options.add_argument('--headless')
                options.add_argument('--disable-gpu')
                print("Running headless- in background")
                self.driver = webdriver.Chrome(options=options)


        else:
            print("Running normally")

            try:
                self.driver = webdriver.Chrome()
            except Exception as e:
                print(e)

        

        try:
        
            driver = self.driver
            driver.get("https://www.instagram.com/")
            time.sleep(3)


            # LoginButton = driver.find_element_by_xpath(
            #     "//a[@href='/accounts/login/?source=auth_switcher']")
            # LoginButton.click()

            time.sleep(3)


            UsernameElem = driver.find_element_by_xpath(
                "//input[@name='username']")
            UsernameElem.clear()
            UsernameElem.send_keys(self.username)


            PasswordElem = driver.find_element_by_xpath(
                "//input[@name='password']")
            PasswordElem.clear()
            PasswordElem.send_keys(self.password)
            PasswordElem.send_keys(Keys.RETURN)

            time.sleep(2)
        
        except WebDriverException or NoSuchWindowException as e:
            print("Browser has been closed by manual intervention \n")
            print(e)
            browserRunning = False
            self.CloseThreader()
            pass
        
        else:

            try:
                loginCheck = driver.find_element_by_id("slfErrorAlert")
                

            except NoSuchElementException:
                infoValidity = True
                pass

            else:
                tk.messagebox.showerror("Login Error", "Please re-verify your login details")
                print("Login details are incorrect \n")
                self.CloseThreader()
                infoValidity = False

        
        if infoValidity == True:
            try:
                while i <= len(hashtags) and hashtagsOut == False:  
                       
                    # Choose a tag from the list of tags 
                    hashtag = hashtags[i]
                    hashtag = hashtag.replace(" ", "")

                    self.LikePhoto(hashtag, nOfPics, pages)
                    i = i + 1

            except Exception:

                if i != len(hashtags):
                    self.CloseBrowser()
                    print("Browser crashed")
                    time.sleep(3)
                    i = 0

                elif i == len(hashtags):
                    self.CloseThreader()
                    hashtagsOut = True

            if hashtagsOut:
                messagebox.showinfo("Complete", "Program has completed")
                

    def LikePhoto(self, hashtag, NumOfPics, pages):
        
        
        driver = self.driver
        print(hashtag)
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(1)
        PicLinks = []
        print("Check : Number of pages are", pages)

        currentUrl = driver.current_url

        if currentUrl != "https://www.instagram.com/explore/tags/" + hashtag + "/":
            driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
            time.sleep(3)

        try:    
            for i in range(0,pages):

                driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)

                    
                Links = driver.find_elements_by_tag_name('a')

                Links = [elem.get_attribute('href') for elem in Links
                        if ".com/p/" in elem.get_attribute("href")]

                for Link in Links:
                    if Link not in PicLinks:
                        PicLinks.append(Link)
                    
                print(
                    "Check: Total N.of pic hrefs stored after array : " + str(len(PicLinks)) + " , in " + hashtag)
        
            LikedPhotos = 0 


            for i in range(0, len(PicLinks)):
                print("Num" , i , ": " ,  PicLinks[i])

            UniquePhotos = int(NumOfPics)
            print(UniquePhotos)

            # For all the images in the array, like each one
            for i in range(0,int(NumOfPics)):
                try:
                    driver.get(PicLinks[i])
                    time.sleep(random.randint(1, 3))
                
                except Exception as e:
                    print(e)
                    

                # try:
                #     # driver.execute_script(
                #     #     "window.scrollTo(0, document.body.scrollHeight);")
                
                # except NoSuchElementException as e:
                #     print(e)


                try:
                    
                    driver.find_element_by_xpath('//button[@class="wpO6b "]').click()
                    UniquePhotos = UniquePhotos - 1
                    LikedPhotos = LikedPhotos + 1

                except Exception as e:
                    print(e)
                
                time.sleep(random.randint(1, 3))
                
                try:
                    driver.find_element_by_xpath('//button[@class="aOOlW   HoLwm"]').click()
                    self.CloseThreader()
                    print("Blocked")

                except Exception:
                    pass

                
                print("Picture liked : ",LikedPhotos , " Pictures left : ", UniquePhotos)

        except NoSuchWindowException or WebDriverException or NoSuchFrameException as e:
            print(e)
            browserRunning = False
        
        finally:
            print("LikePhotos function is now over\n")

    def IsBrowserRunning(self, browserCount):
        if len(browserCount) > 1:
            print(len(browserCount))
            return True

        else:
            return False




if __name__ == "__main__":
    print("Run from main \n")

    NewLimit = 3000
    sys.setrecursionlimit(NewLimit)
    global browserCount
    browserCount = []


    IG = InstagramBot()
    IG.Gui()

else:
    print("Run from import")
