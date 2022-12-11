class point :
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def sqSum(self):
        square_sum=(self.x**2)+(self.y**2)+(self.z**2)
        return square_sum


Point = point(1,3,5)
data = Point.sqSum()
print("sum of square of the numbers is: ",data)
        

        