import configparser

config=configparser.RawConfigParser()
config.read(".\\Configurations\\mycred.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('common info','baseurl')
        return url

    @staticmethod
    def getUseremail():
        username=config.get('common info','username')
        return username

    @staticmethod
    def getPassword():
        password=config.get('common info','password')
        return password
    @staticmethod
    def getSearchitem():
        searchitem=input("enter your search keyword")
        return searchitem

