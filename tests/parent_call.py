class A:
    def __init__(self):
         self.x = 0
    def spam(self):
        print('A.spam',self.x)

class B(A):
    def __init__(self):
        super().__init__()
        self.y = 1
    def spam(self):
        super().spam()
        print('B.Spam',self.y)

if __name__ == "__main__":
    b=B()
    b.spam()
