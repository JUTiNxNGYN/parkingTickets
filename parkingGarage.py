class Ticket():

    def __init__(self):
        self.value=[]
        self.paid=False

class ParkingGarage():

    def __init__(self):
        self.available_tickets=list(range(1,100+1))
        self.available_spaces=list(range(1,100+1))
        self.current_ticket={'number':[],'value':[],'paid':False}


    def takeTicket(self):
        self.available_tickets -= 1
        self.available_spaces -= 1
        x=self.available_tickets.pop(min(self.available_tickets))
        self.current_tickets['number'].append(x)

    def payForParking(self):
        while not self.current_tickets['paid']:
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
            
