# class Ticket():

#     def __init__(self):
#         self.value=[]
#         self.paid=False

class ParkingGarage():

    def __init__(self):
        self.available_tickets=list(range(1,100+1))
        self.available_spaces=list(range(1,100+1))
        self.current_tickets=[]

    def takeTicket(self):
        print("Take Ticket")
        self.available_tickets -= 1
        self.available_spaces -= 1
        x=self.available_tickets.pop(min(self.available_tickets))
        self.current_tickets.append({x,{'value':[],'paid':False}})

    def payForParking(self):
        print("Pay for parking")
        while True:
            num=input('Please input ticket #')
        # while not self.current_tickets['paid']:
            price=input('How much are you paying today?\t')
            self.current_tickets['value'].append(price)
            self.current_tickets['paid']=True

    def leaveGarage(self):
        if self.current_tickets['paid']:
            self.available_tickets += 1
            self.available_spaces += 1
            x=self.available_tickets.pop(self.current_tickets['number'])
            (self.available_tickets).append(x)
            print("Thank You, have a nice day")
        else:
            print("Please pay for ticket before exit.\n")
            self.payForParking()

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


            
