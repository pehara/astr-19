# Python scrpit that describes my favorite animals attributes.

class Animal:
    def __init__(self, arm_len, leg_len, eye_num, tail, furry):
        self.arm_len = arm_len
        self.leg_len = leg_len
        self.eye_num = eye_num
        self.tail = tail
        self.furry = furry
    
    def describe(self):
        print(f"My favorite animal has:")
        print(f"Arm length: {self.arm_len}")
        print(f"Leg length: {self.leg_len}")
        print(f"Eyes: {self.eye_num}")
        print(f"Has a tail: {self.tail}")
        print(f"Furry: {self.furry}")
        print("\n")

favorite_animal = Animal(0.7, 4.3, 3, True, False)

favorite_animal.describe()