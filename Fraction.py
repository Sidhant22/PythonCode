import math

class Fraction:
    # Initializing the Constructor to initialize Numerator and Denominator
    def __init__(self, n, d):
        self.num = n
        self.den = d

    # Method to simplify the fraction
    def simplify(self, num, den):
        # Find the greatest common divisor of the numerator and denominator
        gcd = math.gcd(num, den)
        # Simplify the fraction by dividing both num and den by gcd
        return num // gcd, den // gcd

    # To display the fraction: Numerator / Denominator
    def __str__(self):
        return "{}/{}".format(self.num, self.den)

    # For addition operation in Fraction
    def __add__(self, other):
        temp_num = self.num * other.den + other.num * self.den
        temp_den = self.den * other.den
        # Simplify the result before returning
        simplified_num, simplified_den = self.simplify(temp_num, temp_den)
        return "{}/{}".format(simplified_num, simplified_den)

    # For subtraction operation in Fraction
    def __sub__(self, other):
        temp_num = self.num * other.den - other.num * self.den
        temp_den = self.den * other.den
        # Simplify the result before returning
        simplified_num, simplified_den = self.simplify(temp_num, temp_den)
        # return "{}/{}".format(temp_num,temp_den)
        return "Simplified Result: {}/{}".format(simplified_num, simplified_den)
    
    def __mul__ (self,other):
        temp_num = self.num * other.num
        temp_dem = self.den * other.den

        return "{}/{}".format(temp_num,temp_dem)

    def __truediv__ (self, other):
        temp_num = self.num * other.den 
        temp_den = self.den * other.num
        return "{}/{}".format(temp_num,temp_den)
