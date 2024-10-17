class Dimension:
    def __init__(self, name, chunks=None):
        if chunks is None:
            chunks = []
        self.name=name
        self.chunks=chunks
        self.biomes=[]
        self.worldgenSettings=None
class World:
    def __init__(self,name):
        self.name=name
        self.dimensions={}
        self.players=[]