import csv
import time
import tweepy

consumer_key = 'LwjoSPrxYf2soKLkgcyvQ2zDT'
consumer_secret = 'YLaZ3XCWgEkl4ZbJHhaI2JzxY2FcQTGOwrre7gj3Tm4JFO2mvR'
access_token = '1201408581792411648-oASQP3VeUGNuwmQXIctjY8FFOABsoo'
access_token_secret = 'HDOSllW3lKgaZEcfmtSdwedyxC2BnpvE794v1nuG1rQdt'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

with open('Titanic_Passengers.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    Bios = []
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            Bios.append(f'\t Hi, my name is {row[4]} {row[3]} and I {row[1]} survive the Titanic.')
            line_count += 1
    for i in Bios:
        api.update_status(status=i)
        time.sleep(3600)
    #print(*Bios, sep = "\n")
    #print(f'Processed {line_count} lines.')