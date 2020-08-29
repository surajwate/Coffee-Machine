class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        self.S = 0.5 * self.a * self.b
        # calculate the area here



# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]

# write your code here
if input_c ** 2 == input_a ** 2 + input_b ** 2:
    your_triangle = RightTriangle(input_c, input_a, input_b)
    print(your_triangle.S)
else:
    print("Not right")