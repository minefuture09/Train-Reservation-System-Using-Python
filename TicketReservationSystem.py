class Train:
    
    def __init__(self,name,fare,seats):
        self.name = name
        self.fare = fare
        self.seats = []
        print("********************** Welcome To Train Reservation System **********************")
        for i in range(0,seats):
            self.seats.append(i)

        print("1) Press 1 to Get Train Info")
        print("2) Press 2 to book ticket")
        print("3) Press 3 to Exit")
        print("\n\n")
    
    def getStatus(self):
        try:
            
            print(f"The Name of train is {self.name}")
            print(f"The seats available in train are {len(self.seats)}")
            print(f"The ticket coast is {self.fare}")
            print("\n\n")
        except:
            print("Please Enter valid name of train")
    def bookTicket(self):
        try:
            if len(self.seats)>0:
                print(f"Booking seat successfully!")
                print(f"Your seat number is {(self.seats).pop()}")
                print("\n\n")
                
            else:
                print("Train is full please try in Tatkal!!!")
                print("\n\n")
        except:
            print("Please Try again!!!")
            
    def cancelTicket(self):
        try:
            seatNo = int(input("Enter Seat No. :- "))
            print("Your Reservation successfully cancelled!!")
            (self.seats).append(seatNo)
        except:
            print("Please Enter Valid seatNo.!!")

train_name = input("Enter train name:- ")

t1 = Train(train_name,100,300)
while True:
    
    try:
        choice = int(input("Enter Your Chocie:- "))
        if choice == 1:
            t1.getStatus()
        elif choice == 2:
            t1.bookTicket()
        elif choice == 3:
            t1.cancelTicket()
        elif choice == 4:
            break

        else:
            print("Please Enter correct choice")
    except:
        print("Please Try again!!!!")
        



