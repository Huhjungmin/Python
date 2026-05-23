class Car:
    def __init__(self, speed, color, model):
        self.speed = speed
        self.color = color
        self.model = model
    def drive(self):
        self.speed = 60
myCar = Car(0, "blue", "E-class")

print("자동차객체를생성하였습니다.")
print("자동차의속도는", myCar.speed)
print("자동차의색상은", myCar.color)
print("자동차의모델은", myCar.model)

myCar.drive()
print("자동차의속도는", myCar.speed)
