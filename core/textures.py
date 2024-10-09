import os,pygame
from core.log import log
def loadBlockTextures():
    log("TEXTURES","Loading block textures from textures/blocks")
    textures={}
    files = os.listdir(os.path.join('textures','blocks'))
    for file in files:
        image = pygame.image.load(os.path.join('textures','blocks',file))
        textures[file] = pygame.transform.scale(image, (32, 32))
    log("TEXTURES",f'Loaded {len(textures)} block textures.',1)
    return textures