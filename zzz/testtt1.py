def make_multiplier(no):
    def multiply(x):
        return x*no
    return multiply

double=make_multiplier(2)

print(double(10))