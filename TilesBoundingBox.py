import math

def getNumberOfTiles(size, tile_size, min_overlap):
    return math.ceil(size/(tile_size-min_overlap))

def getOverlap(size, num_tiles, tile_size):
    return abs(((size-tile_size)/(num_tiles-1))-tile_size)


if __name__ == "__main__":
    #print(Operazione.somma(3,4))
    print(getNumberOfTiles(1000, 50, 2))