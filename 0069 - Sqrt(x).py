class Solution(object):
    @staticmethod
    def mySqrt(x):
        # Arithmetic Mean >= Geometric Mean >= Harmonic Mean
        # Arithmetic Mean = (a + b) / 2
        # Geometric Mean = sqrt(a.b)
        # Harmonic Mean = (2.a.b) / (a + b)
        # Let, a = x and b = 1
        # AM = (x + 1) / 2
        # GM = sqrt(x) ---> That's the point.
        # HM = (2.x) / (x + 1)

        left = int((2 * x) / (x + 1)) # Min value, Harmonic Mean
        right = int((x + 1) / 2) # Max value, Arithmetic Mean
        while left <= right:
            center = int((left + right) / 2)

            if pow(center, 2) == x:
                return center
            
            elif pow(center, 2) > x:
                right = center - 1

            elif pow(center, 2) < x:
                left = center + 1

        return right