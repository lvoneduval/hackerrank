from math import sqrt
class Complex(object):
    def __init__(self, real = 0, imag = 0):
        self.real = real
        self.imag = imag
    def __add__(self, no):
        return(Complex(self.real + no.real, self.imag + no.imag))
    def __sub__(self, no):
        return(Complex(self.real - no.real, self.imag - no.imag))
    def __mul__(self, no):
        return(Complex(self.real * no.real - self.imag * no.imag, self.real * no.imag + self.imag * no.real))
    def __truediv__(self, no):
        return(Complex((self.real * no.real + self.imag * no.imag) / (no.real**2+no.imag**2),(self.imag*no.real-self.real*no.imag)/(no.real**2+no.imag**2)))
        return res

    def mod(self):
      return(Complex(sqrt(self.real**2 + self.imag**2),0))
    def __str__(self):
        if self.imag == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imag >= 0:
                result = "0.00+%.2fi" % (self.imag)
            else:
                result = "0.00-%.2fi" % (abs(self.imag))
        elif self.imag > 0:
            result = "%.2f+%.2fi" % (self.real, self.imag)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imag))
        return result
