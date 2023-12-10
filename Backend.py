import pandas as pd

# Parameters
max_Votes = 5
liked_Photo = True
follows_Customer_Account = True
influencer = "andyappleseeds"


class ContestResultsGenerator:
    def __init__(self, CommentsHTMLFile, LikesHTMLFile):

        # The two spreadsheets required
        self.HTMLFile = CommentsHTMLFile
        self.LikesHTMLFile = LikesHTMLFile

        # Dictionaries for data flow
        #  {Username:"",}   Just used to verification purposes.

        # Users that only partially entered the contest. Good for bot monitoring or "sales leads".
        self.usersThatLikedButDidNotComment = []
        self.usersThatCommentedButDidNotLike = []

        # Firing order of all class functions.
        self.commentDict = self.readHTMLDataContestPost()
        print("self.commentDict: ")
        print(self.commentDict)

        print("# of comments on the photo: ")
        print(len(self.commentDict.keys()))

        self.likeList = self.getUsersThatLikedPhoto()
        print("self.likesList: ")
        print(self.likeList)

        print("# of people that liked the photo: ")
        print(len(self.likeList))

        self.confirmUsersLikedANDCommented()

    def readHTMLDataContestPost(self):
        # Open up all comments and "edit HTML as" the class= XQXOT

        export_Data = {}

        from bs4 import BeautifulSoup
        with open("templates/" + self.HTMLFile, encoding="utf8") as fp:
            soup = BeautifulSoup(fp, 'html.parser')
            for post in soup.find_all('div', class_="C4VMK"):
                try:
                    export_Data[post.find('a', class_="sqdOP yWX7d _8A5w5 ZIAjV")['href'][1:-1]].append([x.text for
                                                                                                         x in
                                                                                                         post.find_all(
                                                                                                             'a',
                                                                                                             "notranslate")])

                except KeyError:
                    export_Data[post.find('a', class_="sqdOP yWX7d _8A5w5 ZIAjV")['href'][1:-1]] = [x.text for
                                                                                                    x in
                                                                                                    post.find_all('a',
                                                                                                                  "notranslate")]

        return export_Data

    def getUsersThatLikedPhoto(self):
        # Returns a dataframe of the relevant data in the comments spreadsheet
        returnList = []
        from bs4 import BeautifulSoup
        with open("templates/" + self.LikesHTMLFile, encoding="utf8") as fp:
            soup = BeautifulSoup(fp, 'html.parser')
            for post in soup.find_all('a'):
                for x in post.find_all('div', class_='qF0y9 Igw0E rBNOH eGOV_ ybXk5 _4EzTm'):
                    returnList.append(x.text.strip())

        return returnList

    def confirmUsersLikedANDCommented(self):
        for user in self.likeList:
            if user in self.commentDict.keys():
                print(user + " like the photo and also commented: ")
                print(self.commentDict[user])
            else:
                print(user + " liked the photo but did not leave a comment.")


def confirmUsersThatCommentedAlsoLiked(self):
    # Make sure that the user liked AND commented on the photo.
    for username, entries in self.modifiedCommentDict.items():
        if username in self.likesDict.keys():
            print("Username " + username + " entered the competition, has " + str(
                entries) + " entries and liked the photo.")
            self.usersAndVoteCounts[username] = self.modifiedCommentDict[username]
        else:
            print("Username " + username + " entered the competition, has " + str(
                entries) + " entries BUT DID NOT LIKE THE PHOTO.")


def exportEligibleParticipantsToCSV(self):
    # Export the final results to a csv.
    import csv
    csv_file = "Eligible_Participants_Entries.csv"

    with open(csv_file, 'w', newline='') as csvFile:

        writer = csv.writer(csvFile)
        for name, votes in self.usersAndVoteCounts.items():
            loopNumber = 1
            while loopNumber <= votes:
                writer.writerow([name])
                loopNumber += 1


def returnListOfDicts(self):
    final_List = []
    for name, votes in self.usersAndVoteCounts.items():
        loopNumber = 1
        while loopNumber <= votes:
            final_List.append({"label": name, "value": 1, "question": name + " is the winner!"})
            loopNumber += 1
    return final_List


def getListOfPeopleThatCommented():
    from bs4 import BeautifulSoup
    with open("templates/Example Contest HTML File.html", encoding="utf8") as fp:
        soup = BeautifulSoup(fp, 'html.parser')

        return [commenter['href'][1:-1] for commenter in soup.find_all('a', class_="_2dbep qNELH kIKUG")]


def readHTMLCustomerLikes():
    pass


def document_initialised(driver):
    return driver.execute_script("return initialised")


def getLikesSpreadsheet():
    from bs4 import BeautifulSoup
    import requests
    from selenium.webdriver.chrome.options import Options
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait

    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    driver = webdriver.Chrome()  # options=chrome_options

    driver.get("https://www.instagram.com")
    import time
    time.sleep(5)

    driver.find_element(By.NAME, "username").send_keys("")
    driver.find_element(By.NAME, "password").send_keys("")


    while True:
        print("Waiting for input")
        time.sleep(5)

    #try:
    #    driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button').click()
    #except:
    #    print("No 'Save login info' screen? ")
    #    pass
#
    #driver.get(user_url)
    #input()




def get_description_and_image(giveaway_url):
        from bs4 import BeautifulSoup
        import requests
        import urllib.request

        soup = BeautifulSoup(requests.get(giveaway_url).content, "html.parser")
        description = soup.text.strip()
        print("Got description: ")
        print(description)

        image_url = giveaway_url + "media/?size=l"

        urllib.request.urlretrieve(image_url, "repost_image.jpg")

        print("Got image, saved as: repost_image.jpg")

        return description

def reposting_bot(giveaway_url):



    from instapy_cli import client

    username = ''  # your username

    password = ''  # your password

    text = get_description_and_image()

    image = ""  # here you can put the advertising image.



    with client(username, password) as cli:
        cli.upload(image, text)




if __name__ == '__main__':
    get_description_and_image("https://www.instagram.com/p/Ch0ZOxYPD-b/")

# https://www.instagram.com/p/ChulFzJL9Dj/
