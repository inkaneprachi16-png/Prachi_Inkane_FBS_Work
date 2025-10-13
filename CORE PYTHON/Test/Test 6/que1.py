from abc import ABC,abstractmethod
class Vehical(ABC):
        def __init__(self,person_num):
            self.person_num = person_num

        @abstractmethod
        def calculateToll(self):
            pass

class TwoWheelVehical(Vehical):
    def calculateToll(self):
        basic_toll = 20
        extra_charge= 0
        if self.person_num > 2:
            extra_charge = (self.person_num -2 )*10

        return basic_toll + extra_charge
    
class ThreeWheelVehical(Vehical):
    def calculateToll(self):
        basic_toll = 30
        extra_charge = 0
        if self.person_num>3:
            extra_charge = (self.person_num -3 )*20
        return basic_toll +extra_charge
    
class FourWheelVehical(Vehical):
    def calculateToll(self):
        basic_toll = 40
        extra_charge = 0
        if self.person_num>4:
            extra_charge = (self.person_num -4) * 40
        return basic_toll + extra_charge

class HeavyVehical(Vehical):
    def calculateToll(self):
        basic_toll = 60
        extra_charge = 0
        if self.person_num >6:
            extra_charge = (self.person_num -6) * 100
        return basic_toll + extra_charge
    


def is_number(s):
    return s.isdigit()

def totalToll():
    ch = 0 
    while ch != 6:
        print("1. Two Wheeler")
        print("2. Three Wheeler")
        print("3. Four Wheeler")
        print("4. Heavy Vehicle")
        print("5. Exit")

        choice = input("enter your choice:")

        if choice == '5':
            print("thank you!")
            break

        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Try again.")
            continue

        persons_input = input("Enter number of persons in vehicle: ")
        if not is_number(persons_input):
            print("Invalid number. Try again.")
            continue

        persons = int(persons_input)

        if choice == '1':
            vehicle = TwoWheelVehical(persons)
        elif choice == '2':
            vehicle = ThreeWheelVehical(persons)
        elif choice == '3':
            vehicle = FourWheelVehical(persons)
        elif choice == '4':
            vehicle = HeavyVehical(persons)

        # Same method called, different behavior
        toll = vehicle.calculateToll()
        print("Total Toll to be Paid: ₹", toll)


totalToll()








