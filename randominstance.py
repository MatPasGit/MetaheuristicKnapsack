from RandomNumberGenerator import *
from Item import *
def random_instance(seed, size ):
    x = RandomNumberGenerator(seed)
    instance = []
    for i in range(0, size):
        instance.append(Item(i ,x.nextInt(0,20), x.nextInt(1,20)))

    return instance


