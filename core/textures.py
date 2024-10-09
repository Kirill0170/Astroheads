import os,pygame
import core.log as log
def loadBlockTextures():
    textures={}
    files = os.listdir(os.path.join('textures','blocks'))
    for file in files:
        image = pygame.image.load(os.path.join('textures','blocks',file))
        textures[file] = pygame.transform.scale(image, (32, 32))
    log.log("TEXTURES",f'Loaded {len(textures)} block textures.')
    return textures