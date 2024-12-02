import numpy as np
def block(values, block_size=100, equil=1000):
    blocks = [np.average(block) for block in np.array_split(values[equil:], block_size)]
    return str(np.average(values[equil:])) + ' stdev ' + str(np.std(blocks)/np.sqrt(len(blocks)))
