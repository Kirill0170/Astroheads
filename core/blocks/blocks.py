import os,importlib,inspect
from core.log import log

class BlockProperties:
    def __init__(self,miningLevel=1,miningType=0,renderLevel=0,canCollide=True,visible=True,itemOverride=None):
        self.visible=visible # can be seen
        self.canCollide=canCollide # if physics are applied
        self.miningLevel=miningLevel # mining level
        self.miningType=miningType
        self.renderLevel=renderLevel # for rendering
        self.itemName=None #ignore that

""""
mining levels:          mining types:
 0 = instant
 1 = hand               0 = default(pickaxe)
 2 = flint pick         1 = axe
 3 = iron pick          2 = shovel
 4 = drill              
 -1 = unbreakable
 
 !!change mining type to mining.axe etc
 """

class Block:
    def __init__(self,name: str,textureName: str,blockProperties=BlockProperties(),sounds=None,tileEntity=None):
        self.name=name
        self.textureName=textureName
        self.blockProperties=blockProperties
        self.sounds=sounds
        self.tileEntity=None


def loadBlocks(directory): # UNTESTED
    """
    Import all classes from all .py files in the specified directory.
    Args:
        directory (str): The path to the directory containing .py files.
    Returns:
        dict: A dictionary where keys are module names and values are lists of class objects.
    """
    classes = {}
    log("BLOCKS","Loading blocks in core/blocks/blocksdir/")
    # List all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.py') and filename != '__init__.py':
            # Remove the .py extension to get the module name
            module_name = filename[:-3]
            module_path = f"{directory.replace('/', '.')}.{module_name}"

            # Import the module
            module = importlib.import_module(module_path)

            # Get all classes in the module
            for name, obj in inspect.getmembers(module, inspect.isclass):
                classes[name] = obj
    del classes['Block']
    del classes['BlockProperties']
    log("BLOCKS",f"Loaded {len(classes)} blocks",1)
    return classes