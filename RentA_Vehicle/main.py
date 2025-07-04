from rent.py import BikeRent,CarRent,Customer


bike = BikeRent(100)
car = CarRent(50)
customer = Customer()

main_menu = True
while True:
    
    if main_menu:
     
        print("""   Welcome Rent a Vehicle
              
                      A.Car Menu
                      B.Bike Menu
                      C.Exit
                      
                      """ )
        main_menu=False  
        choice = input("  Choose the choice: ")
 
    
    if choice =="A" or choice =="a":
        
        print("""  Car Menu
                   1.Display cars
                   2.Rent hourly 20 $
                   3.Rent daily  200 $
                   4.Return a Car
                   5.Main Menu
                   6.Exit
              """)
              
        choice = input("choice: ")
        try:
            choice = int(choice)
        except:
            print("Chooose a number")
            continue
        
        match choice:
            
            case 1:
                car.DisplayStock()
                choice = "A"   # return car menu
            
            case 2:
                customer.rentaltime_c  = car.RentHourly(RequestVehicle("cars"))
                customer.rentalbasis == 1
            case 3:
                customer.rentaltime_c  = car.RentHourly(RequestVehicle("cars"))
                customer.rentalbasis == 2
                main_menu =True #return menu
            case 4:
                
            case 5:
                
            case 6:
                
        
            
            
            
            
            
            
        elif choice =="B" or choice =="b":
            
            print("""  Bike Menu
                       1.Display bikes
                       2.Rent hourly 20 $
                       3.Rent daily  200 $
                       4.Return a Bike
                       5.Main Menu
                       6.Exit
                  """) print("Bike Menu")
            
            choice = input("choice: ")
            try:
               choice =  int(choice)
            except:
                print("Chooose a number")