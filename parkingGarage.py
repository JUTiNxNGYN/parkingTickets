# class Ticket():

#     def __init__(self):
#         self.value=[]
#         self.paid=False

class ParkingGarage():

    def __init__(self):
        self.available_tickets=list(range(1,100+1))
        self.available_spaces=100
        self.current_tickets={}

    def takeTicket(self):
        self.available_spaces -= 1
        num=min(self.available_tickets)
        self.current_tickets.update({num:{'value':[],'paid':False}})
        self.available_tickets.remove(num)
        print(f"your ticket number is {num}")
        print(self.current_tickets)

    def payForParking(self):
        print("Pay for parking")
        while True:
            num=int(input('Please input ticket #'))
        # while not self.current_tickets['paid']:
            price=input('How much are you paying today?\t')
            self.current_tickets[num]['value'].append(price)
            self.current_tickets[num]['paid']=True
            break

    def leaveGarage(self):
        while True:
            num=int(input('Please input ticket #'))
            if self.current_tickets[num]['paid']== True:
                self.available_spaces += 1
                del self.current_tickets [num]
                (self.available_tickets).append(num)
                print("Thank You, have a nice day")
                break
            else:
                print("Please pay for ticket before exit.\n")
                self.payForParking()
                break

    def parking(self):
        while True:
            menu = input('What do you want to do today? t/take ticket, p/pay for parking, l/leave garage\t')
            if menu == 't':
                self.takeTicket()
            elif menu == 'p':
                self.payForParking()
            elif menu == 'l':
                self.leaveGarage()
                break
            else: 
                print('Invalid input, please try again')

parking=ParkingGarage()
parking.parking()


            
