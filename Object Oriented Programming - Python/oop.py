class Kettle(object):

    def __init__(self, make, price, quality):
        self.make = make
        self.price = price
        self.quality = quality
        self.on = False

day = Kettle("day", 8.99, "okay")
print(day.make)
print(day.price)
print(day.quality)

day.quality = "good"
day.price = 12.75
print(day.price)
print(day.quality)




