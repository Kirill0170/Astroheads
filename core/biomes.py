class BiomeProperties:
    def __init__(self,temperature,foliageType,soilFertility=1):
        self.temperature=temperature
        self.foliageType=foliageType
        self.soilFertility=soilFertility
'''
temperatures:
-10 - polar
0 - cold biome(winter)
10 - autumn
15 - spring
20 - summer
30 - desert
foliage types:
"empty" - no foliage
"plain" - some vegetation, bushes
"mixed" - plains and rare trees
"forest" - trees :)
'''
class Biome:
    def __init__(self,name,chunks,biomeProperties: BiomeProperties):
        self.name=name
        self.chunks=chunks #(start,end)
        self.biomeProperties=biomeProperties