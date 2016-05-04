
def gen(stop = 0):
    while stop < 4:
        yield 0
        stop += 1

for x in gen():
    print(x)
