class Outputview:
    def __init__(self):
        self.pd = None

    def set(self, pd):
        self.pd = pd

    def output(self):
        print(self.pd.id)
        print(self.pd.name)
        print(self.pd.price)