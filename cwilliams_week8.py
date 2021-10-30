#!/usr/bin/env python3
#Christopher Williams CIS245 chrwilliams2@my365.bellevue.edu

#some helper functions for prompting for input with text menus

#single choice, takes a list and returns selection as string
def numbered_menu(choices):

    #check list of choices are sane
    if choices == None:
        return None
    if not isinstance(choices, list):
        raise ValueError("Choice must be a list!")
        return None

    #initialize menu
    arr = {}
    i = 1
    for item in choices:
        arr[i] = item
        i = i + 1
    j = i

    #loop until we get a valid choice
    while True:
        print("Select a choice by number.....")
        for k in range(1,j):
            print("%d.....%s" % (k,arr[k]))
        s = input("Your choice...?")
        try:
            c = int(s)
        except:
            print("Invalid choice!")
            continue
        if (c < 1 or c >= j):
            print("Invalid choice!")
            continue
        #we have a good choice, display and return
        print("You chose %s.\n\n" % arr[c])
        return arr[c]

#multiple choice, takes a list and returns selection a list of strings
def numbered_menu_multi(choices):
    #check list of choices are sane
    if choices == None:
        return None
    if not isinstance(choices, list):
        raise ValueError("Choice must be a list!")
        return None

    #initialize menu selection and choice arrays
    arr = {}
    chosen = []
    nchoices = 0
    i = 1
    for item in choices:
        arr[i] = item
        i = i + 1
    j = i

    #multiple choice menu loop, removing previous selections
    while True:
        print("Select a choice by number.....")
        for k in range(1,j):
            if arr[k] not in chosen:
                print("%d.....%s" % (k,arr[k]))
        print("(You may pick more than one hitting enter after each)")
        s = input("Your choice...? (0 for no more)")
        try:
            c = int(s)
        except:
            print("Invalid choice!")
            continue
        if (c < 0 or c >= j):
            print("Invalid choice!")
            continue
        if (c == 0 and choices == 0):
            print("Invalid choice! You have to pick at least one!")
            continue
        #early exit, we chose some of the elements
        if c == 0 :
            print("\n\n")
            return chosen
        else:
            print("You chose %s.\n\n" % arr[c])
            chosen.append(arr[c])
            nchoices = nchoices + 1
            if nchoices == len(choices):
                print("\n\n")
                return chosen


#vehicle base class
class Vehicle:

    #initialize attributes
    def __init__(self):
        self.make = None
        self.model = None
        self.color = None
        self.fuelType = None
        self.options = None

    #getter and setter methods for attributes

    def setMake(self, m):
        self.make = m

    def getMake(self):
        print("Make: %s" % self.make)
        return self.make

    def setModel(self, m):
        self.model = m

    def getModel(self):
        print("Model: %s" % self.model)
        return self.model

    def setColor(self, m):
        self.color = m

    def getColor(self):
        print("Color: %s" % self.color)
        return self.color

    def setFuelType(self, m):
        self.fuelType = m

    def getFuelType(self):
        print("fuelType: %s" % self.fuelType)
        return self.fuelType

    def setOptions(self, m):
        self.options = m

    def getOptions(self):
        print("Options: %s" % self.options)
        return self.options

    #build method does most of the work
    #we call our numbered menus for some closed ended options
    def build(self):
        self.setMake(input("Please enter make of your vehicle:"))
        self.setModel(input("Please enter model of your vehicle:"))
        self.setColor(input("Please enter color of your vehicle:"))
        self.setFuelType(numbered_menu(['Gasoline', 'Diesel','Electic','Hybird']))
        self.setOptions(numbered_menu_multi(['PowerMirrors', 'PowerLocks','RemoteStart','BackupCamera',"Bluetooth","CruiseControl","TowingPackage","SatelliteRadio","Sunroof","PremiumSound","BuiltinGPS"]))

    #display all of these to screen
    def show(self):
        self.getMake()
        self.getModel()
        self.getColor()
        self.getFuelType()
        self.getOptions()


#car class inherts from Vehicle class
class Car(Vehicle):
    #initialize properties
    #call our base as well
    def __init__(self):
        super().__init__()
        self.engineSize = None
        self.numDoors = None

    #getter and setter methods for attributes of car class
    def setEngineSize(self, v):
        self.engineSize = v

    def getEngineSize(self):
        print("EngineSize: %s" % self.engineSize)
        return self.engineSize

    def setNumDoors(self, v):
        self.numDoors = v

    def getNumDoors(self):
        print("NumDoors: %s" % self.numDoors)
        return self.numDoors

    def build(self):
        Vehicle.build(self)
        self.setEngineSize(numbered_menu(['4-cyllinder', '6-cyllinder','8-cyllinder']))
        self.setNumDoors(numbered_menu(['2-door', '4-door']))

    def show(self):
        Vehicle.show(self)
        self.getEngineSize()
        self.getNumDoors()


#pickup class inherts from Vehicle class
class Pickup(Vehicle):
    #initialize properties
    #call our base as well
    def __init__(self):
        super().__init__()
        self.cabStyle = None
        self.bedLenth = None

    #getter and setter methods for attributes of pickup class
    def setCabStyle(self, v):
        self.cabStyle = v

    def getCabStyle(self):
        print("CabStyle: %s" % self.cabStyle)
        return self.cabStyle

    def setBedLength(self, v):
        self.bedLength = v

    def getBedLength(self):
        print("BedLength: %s" % self.bedLength)
        return self.bedLength

    def build(self):
        Vehicle.build(self)
        self.setCabStyle(numbered_menu(['Standard Cab', 'Quad Cab','Crew Cab']))
        self.setBedLength(numbered_menu(['Short Bed', 'Long Bed']))

    def show(self):
        Vehicle.show(self)
        self.getCabStyle()
        self.getBedLength()



#track vehicles
cars = 0
pickups = 0
bays = []
#loop until we have one of each built
while True:
    print("Welcome to your garage, you have %d cars and %d pickup trucks parked." % (cars, pickups))
    print("Note: you must build at least one of each to leave the garage.\n\n")
    veh = numbered_menu(['Build a car','Build a pickup','Quit'])
    if veh == "Quit":
        #per assignment, we must have at least one car and truck
        if pickups == 0 or cars == 0:
            print("You can't leave until you build at least one of each!")
            continue
        else:
            break
    if veh == "Build a car":
        newcar = Car()
        newcar.build()
        bays.append(newcar)
        cars = cars + 1
        continue
    else:
        newpu = Pickup()
        newpu.build()
        bays.append(newpu)
        pickups = pickups + 1


#printing routine here
i = 1
for v in bays:
    print("#####################################################")
    print("Displaying vehicle #%d..." % i)
    v.show()
    print("#####################################################")
    i = i + 1


