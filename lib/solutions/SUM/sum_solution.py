
class SumSolution:
    
    def compute(self, x, y):
        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError("input must be integers")
        
        if (0 <= x <= 100) or (0 <= y <= 100):
            raise ValueError("input must be positive integers between 0-100 inclusive")

        return x+y
