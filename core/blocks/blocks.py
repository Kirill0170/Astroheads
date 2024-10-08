import os,importlib,inspect

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
    def __init__(self,name: str,textureName: str,blockProperties=BlockProperties(),sounds=None):
        self.name=name
        self.textureName=textureName
        self.blockProperties=blockProperties
        self.sounds=sounds


def importBlocks(directory): # UNTESTED
    """
    Import all classes from all .py files in the specified directory.
    Args:
        directory (str): The path to the directory containing .py files.
    Returns:
        dict: A dictionary where keys are module names and values are lists of class objects.
    """
    classes_dict = {}
    # List all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.py') and filename != '__init__.py':
            # Remove the .py extension to get the module name
            module_name = filename[:-3]
            module_path = os.path.join(directory, module_name)

            # Import the module
            module = importlib.import_module(module_path.replace('/', '.'))

            # Get all classes defined in the module
            classes = [cls for cls in inspect.getmembers(module, inspect.isclass)]
            classes_dict[module_name] = [cls[1] for cls in classes]
    return classes_dict