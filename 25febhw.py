class Schoolbag():
    def __init__(self,item):
        self.__items =[]
        self.__items.append(item)
        #first = input("What would you like to do today?()")
       

    def additemtobag(self,item):
        self.__items.append(item)
        print("added "+item+" to the bag")

    def removeitemfrombag(self,item):
        if item in self.__items:
            self.__items.remove(item)
            print("removed "+item+" from bag")
        else:
            print("cannot find the item in bag")
    
    def displayitemsinbag(self):
        print(self.__items)



bag = Schoolbag("pencils")
#print(bag.__items)
bag.displayitemsinbag()
bag.additemtobag("pen")
bag.displayitemsinbag()
bag.additemtobag("book")
bag.displayitemsinbag()
bag.removeitemfrombag("pencils")
bag.displayitemsinbag()