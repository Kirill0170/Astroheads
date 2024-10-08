from core.blocks.blocks import BlockProperties,Block

# system blocks
class Void(Block):
    def __init__(self):
        super().__init__(name='Void',textureName='void.png',blockProperties=BlockProperties(miningLevel=-1,canCollide=False))

class MissingBlock(Block):
    def __init__(self):
        super().__init__(name='Missing',textureName='missing1.png',blockProperties=BlockProperties(-1))

class Corestone(Block):
    def __init__(self):
        super().__init__(name='Corestone', textureName='corestone.png', blockProperties=BlockProperties(-1))

# other
class Dirt(Block):
    def __init__(self):
        super().__init__(name='Dirt', textureName='dirt.png',blockProperties=BlockProperties(
            miningType=2
        ))
class GrassBlock(Block):
    def __init__(self):
        super().__init__(name='Grass block', textureName='grassblock.png',blockProperties=BlockProperties(
            miningType=2
        ))
class Grass(Block):
    def __init__(self):
        super().__init__(name='Grass', textureName='grass.png',blockProperties=BlockProperties(
            miningLevel=0,
            canCollide=False,
            renderLevel=1
        ))
class Stone(Block):
    def __init__(self):
        super().__init__(name='Stone',textureName='stone.png',blockProperties=BlockProperties(
            miningLevel=2
        ))
class Cobblestone(Block):
    def __init__(self):
        super().__init__(name='Cobblestone',textureName='cobble.png',blockProperties=BlockProperties(
            miningLevel=2
        ))