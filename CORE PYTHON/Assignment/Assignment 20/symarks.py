class SYMARKS:
    def __init__(self,computer_total, maths_total, electronic_total ):
        self.computer_total = computer_total
        self.maths_total = maths_total
        self.electronic_total = electronic_total

    def displayMarks(self):
        print('- - - SY Marks - - -')
        print(f'computer Total: {self.computer_total}')
        print(f'Math Total: {self.maths_total}')
        print(f'Electronic Total: {self.electronic_total}')
