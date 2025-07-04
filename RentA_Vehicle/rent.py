""" Rent A Vehicle """

"""
vehicles:
-rent a car:
    -discount
-rent a bicycle

custom:
-request vehicle
-return vehicles

stock:
-display stock
-rent daily/hourly
-return vehicle

"""
import datetime

#parent class

class VehicleRent:
    
    def __init__(self,stock):
        self.stock = stock
        self.now=0;
        
    #display stock on system
    def DisplayStock(self):
        print("{} vehicle avaliable to rent".format(self.stock))
        return self.stock
        
    def RentDaily(self,n):
        if n <= 0:
            print("you should be positive number ")
            return None
        elif n > self.stock:
            print("not enough vehicle to rent")
            return None
        else:
            self.now = datetime.datetime.now()
            print("rented a {} vehicle for daily at {} hours".format(n,self.now.hour))
            self.stock -= n
            return self.now
        
    def RentHourly(self,n):
        if n <= 0:
            print("you should be positive number ")
            return None
        elif n > self.stock:
            print("not enough vehicle to rent")
            return None
        else:
            self.now = datetime.datetime.now()
            print("rented a {} vehicle for hourly at {} hours".format(n,self.now.hour))
            self.stock -= n
            return self.now
        
    def ReturnVehicle(self,request,brand):
        
        rentaltime ,rentalbasis,numofvehicle = request
        
        car_h_price = 20
        car_d_price = 200
        bike_h_price = 5
        bike_d_price = 100
        
        if brand == "car":
            if rentaltime and rentalbasis and numofvehicle:
                self.stock += numofvehicle
                now = datetime.datetime().now()
                rentalperiod = now - rentaltime
                
                if rentalbasis == 1:  # hourly:
                    bill = rentalperiod /3600*car_h_price*numofvehicle
                    
                elif rentalbasis == 2:  # daily:
                     bill = rentalperiod /(3600*24)*car_d_price*numofvehicle
                    
                if 2 < numofvehicle:
                    print("you have %20 discount ")
                    bill = bill*0.8
                    print("Thank you ")
                    print("you total bill {}".format(bill))
                    return bill
                
        elif brand == "bike":
            if rentaltime and rentalbasis and numofvehicle:
                self.stock += numofvehicle
                now = datetime.datetime().now()
                rentalperiod = now - rentaltime
                
                if rentalbasis == 1:  # hourly:
                    bill = rentalperiod /3600*bike_h_price*numofvehicle
                    
                elif rentalbasis == 2:  # daily:
                     bill = rentalperiod /(3600*24)*bike_d_price*numofvehicle
                    
                if 2 < numofvehicle:
                    print("you have %20 discount ")
                    bill = bill*0.8
                    print("Thank you ")
                    print("you total bill {}".format(bill))
                    return bill
                
            
        else:
            print("you do not rent a vehicle")
            return None
            
            
# child class       
class CarRent(VehicleRent):
    
    global discountrate
    discountrate = 15
    def __init__(self,stock):
        super().__init__(stock)
    
    def Discount(self,b):
        bill = b - (b*discountrate)/100
        return bill
    
    
    
class BikeRent(VehicleRent):    
    
    def __init__(self,stock):
        super().__init__(stock)
    
    
    
    
    
    
class Customer:

    def __init__(self):
        self.bikes = 0
        self.rentalbasis_b = 0
        self.rentaltime_b = 0
        
        self.cars = 0
        self.rentalbasis_c = 0
        self.rentaltime_c = 0
        
        
        
        self.car = 0
        
    def    RequestVehicle(self,brand):    
        
        if brand == "cars":
            
            try:
                cars = int(input("how many cars would you like to rent"))
            except:
                print("should be number")
                
            if cars < 1:
                print("number of cars should be greater than zero")
                return -1;
            else:
                self.cars = cars
            return self.cars
            
            
        elif brand == "bikes":
            
            try:
                bikes = int(input("how many bikes would you like to rent"))
            except:
                print("should be number")
                
            if bikes < 1:
                print("number of bikes should be greater than zero")
                return -1;
            else:
                self.bikes = bikes
            return self.bikes
        
        else:
            print("request vehicle eror")
    
    def  ReturnVehicle(self,brand):
        
        if brand == "bikes":
            if self.rentalbasis_b and self.rentaltime_b and self.bikes:
                return self.rentalbasis_b , self.rentaltime_b , self.bikes
            else:
                    return 0,0,0
            
        elif brand == "cars":
            if self.rentalbasis_c and self.rentaltime_c and self.cars:
                return self.rentalbasis_c , self.rentaltime_c , self.cars
            else:
                    return 0,0,0
            
            
        else:
            print("return vehicle error")
    
    
    