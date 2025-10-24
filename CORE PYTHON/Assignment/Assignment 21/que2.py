class Television():
    def __init__(self):
        self.model_number= 0
        self.screen_size = 0
        self.price = 0

    def getData(self):
        try:
            self.model_number = int(input('enter model number not more than 4 digits:'))
            self.screen_size = int(input('enter screen size in inch:'))
            self.price = int(input('enter the price of model less than 5000 rs:'))


            if self.model_number > 9999:
                raise ValueError('model number is more than 4 digits')
            if self.screen_size < 12 or self.screen_size > 70:
                raise ValueError('screen size between 12 and 70 inches.')
            if self.price <0 or self.price >5000:
                raise ValueError('price between 0 and 5000 rs.')
            
        except ValueError as e:
            print('error:',e)
            print('reset all data member are zero:')
            self.model_number= 0
            self.screen_size = 0
            self.price = 0


    def display_data(self):
        print("\n---- Television Details ----")
        print(f"Model Number : {self.model_number}")
        print(f"Screen Size  : {self.screen_size} inches")
        print(f"Price        : Rs {self.price}")

if( __name__ == "__main__"):
    tv = Television()
    tv.getData()
    tv.display_data()
