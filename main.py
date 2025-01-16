import math

def rail_distance(coord1:tuple, coord2:tuple) -> int:
    """Calculates the Manhattan distance between two coordinates on a 2D plane (ignoring vertical movement).
    
    This function computes the total distance required to travel along a grid (x, z) in Minecraft using rails, 
    where movement is restricted to horizontal axes. It assumes that the vertical (y) axis is handled separately 
    by other mechanisms like powered rails or minecart elevators.
    
    Args:
        coord1 (tuple): The starting coordinates as (x1, z1).
        coord2 (tuple): The destination coordinates as (x2, z2).
    
    Returns:
        int: The distance between the two points along the rails, calculated as the sum of absolute differences
             between the x and z coordinates.
    """
    
    blocks = abs(coord2[0] - coord1[0]) + abs(coord2[1] - coord1[1])
    return blocks
    

class CraftingRecipe:
    def __init__(self, blocks:int):
        self.blocks = blocks

    def less_than_1(self, name, amount):
        """
        Ensures the resource amount meets the minimum required for crafting.

        Args:
            name (str): The name of the resource (e.g., 'iron_ingot', 'gold_ingot').
            amount (float): The current amount of the resource.

        Returns:
            int: The minimum required resource amount based on the recipe.
        """

        # Define minimum amount of resource required for recipe
        resource_thresholds = {
            'iron_ingot':6,
            'gold_ingot':6,
            'stick':1,
            'redstone':1
        }
        
        # Get the minimum threshold for the resource, defaulting to 1 if not specified
        min_required = resource_thresholds.get(name)
        
        # Ensure the amount meets the minimum requirement
        return max(amount, min_required)

    def normal_rail(self):
        """Calculates the number of resources required for the normal rails recipe based on number of blocks needed to travel."""
        iron_ingots = self.blocks * 0.675
        sticks = self.blocks * 0.0375
        return (iron_ingots, sticks)
    
    def powered_rail(self):
        """Calculates the number of resources required for the powered rails recipe based on number of blocks needed to travel."""
        gold_ingots = self.blocks * 0.675
        sticks = self.blocks * 0.0375
        redstone = sticks

        return (gold_ingots, sticks, redstone)
    
    def redstone_torch(self, powered_rails):
        """Calculates the number of resources required for the redstone torch recipe based on number of powered rails needed to travel."""
        sticks = powered_rails
        redstone = powered_rails
        return (sticks, redstone)
    


def run():
    # Retrieving the required distance between 2 coords
    starting_coord = tuple(map(int, input('Enter the starting x & z coords (without commas): ').split()))
    dest_coord = tuple(map(int, input('Enter the destination x & z coords (without commas): ').split()))

    distance = rail_distance(starting_coord, dest_coord)

    # Calculating number of resources required for normal rails
    crafting_recipe = CraftingRecipe(blocks=distance)
    print(crafting_recipe.normal_rail())
    

if __name__ == '__main__':
    run()
    # print(CraftingRecipe(blocks=1).powered_rail())