# Our parking garage has 100 spaces available and keeps track of the active tickets using the current ticket dictionary.
# The garage keeps track of individual tickets by their number which is assigned by the available tickets list.
# That number is then removed from the available ticket list until payment at which point it goes back into circulation.
# The garage works on a donation based system where as long as you give something to the value key, you can leave. IT will let you know if you're cheap.
# At which point the dictionary flips your paid status to true and wishes you safe travels.


class ParkingGarage():

    def __init__(self):
        self.available_tickets=list(range(1,101))
        self.current_tickets={}

    def takeTicket(self):
        if len(self.available_tickets)<1:
            print("This parking garage is full, try again later\n")

        else:
            num=min(self.available_tickets)
            self.current_tickets.update({num:{'value':[],'paid':False}})
            self.available_tickets.remove(num)
            print(f"Your ticket number is {num}. Please keep this on hand for exit.\n")
        
    def payForParking(self):
        print("Pay for parking")
        while True:
            num=int(input('Please input ticket number:\t'))
            if self.current_tickets[num]['paid']==False:
                price=input('How much are you paying today?\t')
                self.current_tickets[num]['value'].append(price)
                self.current_tickets[num]['paid']=True
                if int(self.current_tickets[num]['value'][0])<2:
                    print(f"Ticket number {num} has been paid")
                    print("You are free to go, cheapskate\n")
                elif int(self.current_tickets[num]['value'][0])>50:
                    print("Thank you for the generous donation!")
                    print(f"Ticket number {num} has been paid\n")
                else:
                    print(f"Ticket number {num} has been paid\n") 
                break
            else:
                print(f"Ticket number {num} has already been paid. Please exit or double check ticket number.\n")
                break

    def leaveGarage(self):
        while True:
            num=int(input('Please input ticket number:\t'))
            if self.current_tickets[num]['paid']== True:
                del self.current_tickets [num]
                (self.available_tickets).append(num)
                print("Thank You! Safe travels and have a nice day!\n")
                break
            else:
                print("Please pay for ticket before exit.\n")
                self.payForParking()
                break

    def parking(self):
        while True:
            menu = input('What do you want to do today? T/Take ticket, P/Pay for parking, L/Leave garage S/Shut down:\t')
            print(" ")
            if menu == 'T' or menu == 't':
                self.takeTicket()
            elif menu == 'P' or menu == 'p':
                self.payForParking()
            elif menu == 'L' or menu == 'l':
                self.leaveGarage()
            elif menu == 'L' or menu == 'l':
                self.leaveGarage()
            elif menu == 'S' or menu == 's':
                print('Parking offline, hope everyone got out...\n')
                break
            else: 
                print('Invalid input, please try again')

parking=ParkingGarage()
parking.parking()


            
