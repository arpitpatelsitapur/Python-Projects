''' Train-Ticket booking '''
import random
class train:
    avl_seatlist=[]
    booked_seatlist=[]
    def __init__(self,name,number,avl_seats,fare):
        self.name=name
        self.number=number
        self.avl_seats=avl_seats
        self.seat_no=0
        self.fare=fare
        for i in range(self.avl_seats+1):
            if i>0:
                (self.avl_seatlist).append(i)
                
    def getstatus(self):
        print(f"""*********************************************************************
Train name : {self.name}
Train number : {self.number}
Fare on seats : {self.fare}
Available seats : {self.avl_seats}
{self.avl_seatlist}
Booked seats : {self.booked_seatlist}
*********************************************************************""")
    def bookticket(self):
        if self.avl_seats >0:
            self.seat_no=random.choice(self.avl_seatlist)
            print(f"Ticket Booked!!!! The seat no is {self.seat_no}")
            (self.avl_seatlist).remove(self.seat_no)
            (self.booked_seatlist).append(self.seat_no)
            self.avl_seats-=1
        else:
            print("Sorry,Train is full. No seats Available!!!!! Try in Tatkaal.")
            
    def cancelticket(self):
        print(f"{self.booked_seatlist}")
        cancel_seat=int(input("which seat you want to cancel : "))
        print(f"Ticket cancelled!!!! with seat no {cancel_seat}")
        (self.avl_seatlist).append(cancel_seat)
        (self.booked_seatlist).remove(cancel_seat)
        self.avl_seats+=1
            
betwa=train("Betwa Express",15207,20,350)
betwa.getstatus()
betwa.bookticket()
betwa.bookticket()
betwa.cancelticket()
betwa.getstatus()
betwa.bookticket()
betwa.cancelticket()
betwa.getstatus()



