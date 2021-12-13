#Comptuer Class
#mouse method
#keyboard method
#printer method
#main method
import time



class Computer():
    computerstation=False

    def __init__(self,model,brand,processor,display_card,amount_of_ram,motherboard,ssd,hdd):
        self.model=model
        self.brand=brand
        self.processor=processor
        self.display_card=display_card
        self.amount_of_ram=amount_of_ram
        self.motherboard=motherboard
        self.ssd=ssd
        self.hdd=hdd
        memory=hdd+ssd
        self.imformations_of_system(model,brand,processor,display_card,amount_of_ram,motherboard,memory)


    def keyboardstation(self):
        print("Keyboard ready to use! ")
    def giveinputformkeyboard(self):

        time.sleep(1)
        return input("Waiting for input from keyboard : ")
        

    def mouse(self):

        time.sleep(1)
        print("Mouse using..")

    def printer(self,document):

        print(f" {document} is printing..")

    def screen(self):

        print("Screen started to show")
    
    def station_of_computer(self,computerstation):
        if computerstation==True:
            self.screen()
            self.mouse()
            self.keyboardstation()
        else:
            print("Computer did not open yet!\nFirst you have to open computer!")
        



    def opencomputer(self):
        computerstation=True
        return computerstation

    def imformations_of_system(self,model,brand,processor,display_card,amount_of_ram,motherboard,memory):
        print(f"Model : {model}\nBrand : {brand}\nProcessor : {processor}\nDisplay Card : {display_card}\nAmount Of Ram : {amount_of_ram}\nMotherboard : {motherboard}\nMemory : {memory} ")



        

    


    





computer=Computer("Monster","Tulpar T7","Intel Core I7(11800H)","Nvidia RTX3060","16GB","Mobile Intel® HM570",500,1024)


bilgisayardurum=computer.opencomputer()
computer.station_of_computer(bilgisayardurum)
document=computer.giveinputformkeyboard()
computer.printer(document)
