#!/usr/bin/env python3

import os
import re

class ContactInfo:

    #class constructor
    def __init__(self):
        self.name = None
        self.address = None
        self.phone = None
        self.savedir = None
        self.savefile = None
        #call methods to collect info
        while self.getSaveDir() == None:
            self.setSaveDir(self.chooseSaveDir())
        while self.getSaveFile() == None:
            self.setSaveFile(self.chooseSaveFile())
        self.enterContactInfo()

    #setter methods

    def setName(self, n):
        self.name = n

    def setAddress(self, a):
        self.address = a

    def setPhone(self, p):
        self.phone = p

    def setSaveDir(self, d):
        self.savedir = d

    def setSaveFile(self, f):
        self.savefile = f

    #getter methods

    def getName(self):
        return self.name

    def getAddress(self):
        return self.address

    def getPhone(self):
        return self.phone

    def getSaveDir(self):
        return self.savedir

    def getSaveFile(self):
        return self.savefile

    #some additional methods

    #pick save dir and validate
    def chooseSaveDir(self):
        dr = input("Name of Save Directory: ")
        if os.path.isdir(dr) and os.access(dr,os.W_OK):
            print("Path check succeeded.")
            return dr
        else:
            print("Path check failed. Try Again.")
            return None

    #pick save file and validate or check dir is writable
    def chooseSaveFile(self):
        fi = input("Name of Save File: ")
        full = "{0}/{1}".format(self.getSaveDir(),fi)
        if os.path.exists(full):
            if os.access(full,os.W_OK):
                print("Save file is writable and will be overwritten.")
                return fi
            else:
                print("Save file is not writable. Try again.")
                return None
        else:
            print("Save doesn't exist yet but directory is writable.")
            return fi

    #gather contact info, check phone format
    def enterContactInfo(self):
        na = input("Your name: ")
        ad = input("Your address: ")
        phfmt = r'^\d{3}-\d{3}-\d{4}$'
        while True:
            ph = input("Your phone as ###-###-####: ")
            if re.match(phfmt, ph):
                break
            else:
                print("Incorrrect phone format. Try again.")
        self.setName(na)
        self.setAddress(ad)
        self.setPhone(ph)

    def saveContactInfo(self):
        full="{0}/{1}".format(self.getSaveDir(),self.getSaveFile())
        try:
            fw = open(full,"w")
            fw.write("{0},{1},{2}\n".format(self.getName(),self.getAddress(),self.getPhone()))
            fw.close()
        except Exception as ex:
            print("Error saving file: %s " % (ex))
            exit(-1)
        print("Successfully saved {0}".format(full))

    def reviewContactInfo(self):
        full="{0}/{1}".format(self.getSaveDir(),self.getSaveFile())
        print("For your review...")
        try:
            fr = open(full,"r")
            line = fr.readline()
            fr.close()
            fields=line.split(",")
            print("Name: {0}".format(fields[0]))
            print("Address: {0}".format(fields[1]))
            print("Phone: {0}".format(fields[2]))
        except Exception as ex:
            print("Error reading file: %s " % (ex))
            exit(-2)






import os

# main function for app
def main():
    print("**********************************************")
    print("*Welcome to ContactInfo 1.0 by Chris Williams*")
    print("**********************************************")

    #create a ContactInfo Object
    ci = ContactInfo()
    ci.saveContactInfo()
    ci.reviewContactInfo()
  
# call main if interpreter passes name __main__
if __name__=="__main__":
    main()
