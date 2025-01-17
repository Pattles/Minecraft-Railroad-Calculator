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

        # Resources
        self.resources = {
            'normal_rails':{
                'rails':0,
                'iron_ingots':0,
                'sticks':0
                },
            'powered_rails':{
                'rails':0,
                'gold_ingots':0,
                'sticks':0,
                'redstone':0
                },
            'redstone_torches':{
                'torches':0,
                'sticks':0,
                'redstone':0
                }
            }

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
        """
        Calculates the resources required to craft normal rails based on the number 
        of blocks in the travel distance. 
        
        The function returns the quantities of iron ingots and sticks required for crafting 
        the necessary number of rails.

        Returns:
            tuple: A tuple containing:
                - iron_ingots (float): The total number of iron ingots required.
                - sticks (float): The total number of sticks required.
        """
        
        self.resources['normal_rails']['rails'] = self.blocks
        self.resources['normal_rails']['iron_ingots'] = math.ceil(self.blocks * 0.375)
        self.resources['normal_rails']['sticks'] = math.ceil(self.blocks * 0.0625)
        return
    
    def powered_rail(self):
        """
        Calculates the number of resources required to craft powered rails, 
        based on the number of powered rail blocks needed to cover the travel distance.

        A powered rail needs to be placed once every 32 blocks for optimal performance, 
        so the calculation is based on the number of 'powered blocks' (total blocks / 32). 
        The function returns the required amounts of gold ingots, sticks, and redstone 
        for the given number of powered blocks.

        Returns:
            tuple: A tuple containing the required amounts of:
                - gold_ingots (float): The number of gold ingots needed.
                - sticks (float): The number of sticks needed.
                - redstone (float): The number of redstone dust needed (equal to sticks).
        """
        powered_blocks = math.ceil(self.blocks / 32)

        self.resources['powered_rails']['rails'] = powered_blocks
        self.resources['powered_rails']['gold_ingots'] = math.ceil(powered_blocks * 0.375)
        self.resources['powered_rails']['sticks'] = math.ceil(powered_blocks * 0.0625)
        self.resources['powered_rails']['redstone'] = math.ceil(powered_blocks * 0.0625)
        return
    
    def redstone_torch(self, powered_rails):
        """Calculates the number of resources required for the redstone torch recipe based on number of powered rails needed to travel."""
        self.resources['redstone_torches']['torches'] = powered_rails
        self.resources['redstone_torches']['sticks'] = powered_rails
        self.resources['redstone_torches']['redstone'] = powered_rails
        return
    

    def display(self):
        normal_rails_dict = self.resources['normal_rails']
        powered_rails_dict = self.resources['powered_rails']
        redstone_torches_dict = self.resources['redstone_torches']

        normal_rails_req = normal_rails_dict["rails"] - powered_rails_dict["rails"]

        # Computing totals
        totals = {
            'iron_ingots':normal_rails_dict['iron_ingots'],
            'gold_ingots':powered_rails_dict['gold_ingots'],
            'sticks':normal_rails_dict['sticks'] + powered_rails_dict['sticks'] + redstone_torches_dict['sticks'],
            'redstone':powered_rails_dict['redstone'] + redstone_torches_dict['redstone']
        }

        print('REQUIRED COMPONENTS:',
            f'Normal rails: {normal_rails_req}',
            f'Powered rails: {powered_rails_dict["rails"]}',
            f'Redstone torches: {redstone_torches_dict["torches"]}',
            '--',
            'REQUIRED MATERIALS:',
            'Normal rails:',
            f'   Iron ingots: {normal_rails_dict["iron_ingots"]}',
            f'   Sticks: {normal_rails_dict["sticks"]}',
            'Powered rails:',
            f'   Gold ingots: {powered_rails_dict["gold_ingots"]}',
            f'   Sticks: {powered_rails_dict["sticks"]}',
            f'   Redstone dust: {powered_rails_dict["redstone"]}',
            'Redstone torches:',
            f'   Sticks: {redstone_torches_dict["sticks"]}',
            f'   Redstone dust: {redstone_torches_dict["redstone"]}',
            'Total:',
            f'   Iron ingots: {totals["iron_ingots"]}',
            f'   Gold ingots: {totals["gold_ingots"]}',
            f'   Sticks: {totals["sticks"]}',
            f'   Redstone dust: {totals["redstone"]}',
            sep='\n'
            )

def run():
    # Retrieving the required distance between 2 coords
    starting_coord = tuple(map(int, input('Enter the starting x & z coords (without commas): ').split()))
    dest_coord = tuple(map(int, input('Enter the destination x & z coords (without commas): ').split()))

    blocks = rail_distance(starting_coord, dest_coord)
    self = CraftingRecipe(blocks=blocks)

    # Calculating number of resources required
    self.normal_rail()
    self.powered_rail()
    self.redstone_torch(powered_rails=self.resources['powered_rails']['rails'])

    
    # Displaying all of it
    self.display()
    

if __name__ == '__main__':
    run()