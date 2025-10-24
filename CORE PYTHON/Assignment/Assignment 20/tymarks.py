class TYMARKS:
    def __init__(self, theory, practicle ):
        self.theory = theory
        self.practicle = practicle

    def displayMarks(self):
        print('---TY Marks---')
        print(f'Theory marks:{self.theory}')
        print(f'Practicle marks: {self.practicle}')