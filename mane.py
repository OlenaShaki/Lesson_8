def mane_function(s):
    if s == "":
        print("Hello, world!")
    elif s > 10:
        print("Hello, my big friend!")
    elif s <= 10:
        print("Hello, my little friend!")
    else:
        print(f"Hello, {s}!")

mane_function(11)
def test_function(x,y,z):
    return (x+y-z)
