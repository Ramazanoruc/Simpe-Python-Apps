import random
import time  # modules


class Remote_control():

    def __init__(self, tv_station="Close", tv_voice=0, channel_list=["Trt"], channel="Trt"):   #features

        self.tv_station = tv_station

        self.tv_voice = tv_voice

        self.channel_list = channel_list

        self.channel = channel

    def open_tv(self):                         #the module for turn on the tv

        if (self.tv_station == "Open"):
            print("The television already open")

        else:
            print("Television opening...")
            self.tv_station = "Open"
 
    def close_tv(self):                         #the module for turn off the tv


        if (self.tv_station == "Close"):
            print("The television already close")

        else:
            print("television closing...")
            self.tv_station == "Close"

    def sound_settings(self):                    #the module for sound settings


        while True:

            answer = input("Lower the volume: '<'\nIncrease the volume: '>'\n Exit : exit  ")

            if answer == "<":

                if (self.tv_voice != 0):
                    self.tv_voice -= 1

                    print("Volume : ", self.tv_voice)
            elif answer == ">":

                if (self.tv_voice != 32):
                    self.tv_voice += 1

                    print("Volume : ", self.tv_voice)
            else:

                print("the sound has been updated", self.tv_voice)
                break

    def add_chanel(self, channel_name):           #module for adding channel

        print("Channel Adding...")
        time.sleep(1)

        self.channel_list.append(channel_name)

        print("Channel has been added")

    def random_channel(self):                       #module for random channel

        passing = random.randint(0, len(self.channel_list) - 1)

        self.channel = self.channel_list[passing]

        print("current channel is :", self.channel)

    def __len__(self):                        #module for learn channels

        return len(self.channel_list)

    def __str__(self):                  #module for station of tv
        return "Tv Station : {}\nTV Voice : {}\nChannel List : {}\nCurrent Channel : {}\n".format(self.tv_station,
                                                                                                  self.tv_voice,
                                                                                                  self.channel_list,
                                                                                                  self.channel)


remote = Remote_control()       #my object

print("""
Television app 

1.Open Tv

2.Close Tv

3.Voice Settings

4.Add Channel

5.learn Channel Number

6.Random Channel

7.Informations of Television

Exit = press 'q'
""")

while True:

    process = input("Choose the process : ")

    if process == "q":

        print("The program is terminating..")
        break

    elif (process == "1"):

        remote.open_tv()

    elif (process == "2"):

        remote.close_tv()

    elif (process == "3"):

        remote.sound_settings()

    elif (process == "4"):

        channel_names = input("Enter channel names separated by ',' ") # I did this because ı want it to be regular

        channel_list = channel_names.split(",")   #like you see I seperate the channels with ','

        for adding in channel_list:
            remote.add_chanel(adding)

    elif (process == "5"):

        print("Number of channels :", len(remote))

    elif (process == "6"):

        remote.random_channel()

    elif (process == "7"):

        print(remote)
    else:
        print("Invalid transaction..")














