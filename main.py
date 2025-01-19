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

    def minimum_craft(self, name, amount):
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
        
        # Check if the amount is not a multiple of the threshold.
        # If it's not, calculate the nearest multiple of the threshold that is greater than or equal to the amount.
        # This is done by adding the difference between the threshold and the remainder (amount % threshold) to the amount.
        # If the amount is already a multiple, return it as is.
        if amount % resource_thresholds[name] != 0:
            x = amount + (resource_thresholds[name] - (amount % resource_thresholds[name]))
            return x
        return amount

    def normal_rail(self):
        """
        Calculates the resources required to craft normal rails based on the number 
        of blocks in the travel distance. 
        
        This method computes the required quantities of iron ingots and sticks 
        for the powered rails, ensuring that minimum crafting thresholds are met (e.g., iron ingots).

        Returns:
            None: Updates the `resources['normal_rails']` dictionary with:
                - 'rails' (int): The number of powered rail blocks required.
                - 'iron_ingots' (int): The number of iron ingots needed.
                - 'sticks' (int): The number of sticks needed.
        """
        self.resources['normal_rails']['rails'] = self.blocks
        self.resources['normal_rails']['iron_ingots'] = self.minimum_craft('iron_ingot', math.ceil(self.blocks * 0.375))
        self.resources['normal_rails']['sticks'] = math.ceil(self.blocks * 0.0625)
        return
    
    def powered_rail(self):
        """
        Calculates the resources required to craft powered rails based on the travel distance.

        Powered rails need to be placed once every 32 blocks for optimal performance, 
        meaning the total number of powered rail blocks ('powered blocks') is determined by dividing 
        the travel distance by 32 (rounded up). 

        This method computes the required quantities of gold ingots, sticks, and redstone dust 
        for the powered rails, ensuring that minimum crafting thresholds are met (e.g., gold ingots).

        Returns:
            None: Updates the `resources['powered_rails']` dictionary with:
                - 'rails' (int): The number of powered rail blocks required.
                - 'gold_ingots' (int): The number of gold ingots needed.
                - 'sticks' (int): The number of sticks needed.
                - 'redstone' (int): The amount of redstone dust needed.
        """
        powered_blocks = math.ceil(self.blocks / 32)

        self.resources['powered_rails']['rails'] = powered_blocks
        self.resources['powered_rails']['gold_ingots'] = self.minimum_craft('gold_ingot', math.ceil(powered_blocks * 0.375))
        self.resources['powered_rails']['sticks'] = math.ceil(powered_blocks * 0.0625)
        self.resources['powered_rails']['redstone'] = math.ceil(powered_blocks * 0.0625)
        return
    
    def redstone_torch(self, powered_rails):
        """
        Calculates the resources required to craft redstone torches based on the number 
        of powered rails needed for the travel distance.

        This method computes the required quantities of sticks and redstone dust 
        to craft the necessary number of redstone torches. The calculations assume that 
        one stick and one redstone dust are needed for each redstone torch.

        Returns:
            None: Updates the `resources['redstone_torches']` dictionary with:
                - 'torches' (int): The total number of redstone torches required (equal to `powered_rails`).
                - 'sticks' (int): The total number of sticks needed (equal to `powered_rails`).
                - 'redstone' (int): The total amount of redstone dust needed (equal to `powered_rails`).
        """
        self.resources['redstone_torches']['torches'] = powered_rails
        self.resources['redstone_torches']['sticks'] = powered_rails
        self.resources['redstone_torches']['redstone'] = powered_rails
        return
    

    def display(self):
        """
        Displays a summary of the resources required for crafting rails and redstone torches.

        This method calculates and prints the total quantities of materials (e.g., iron ingots, gold ingots, 
        sticks, redstone dust) needed to craft the required number of normal rails, powered rails, 
        and redstone torches based on the travel distance.

        Key calculations:
            - Computes the number of normal rails required after accounting for powered rails.
            - Ensures resource requirements meet minimum crafting thresholds where applicable.
            - Aggregates totals for all required materials across all components.

        Output Format:
            The printed summary includes:
            1. The number of each component required:
                - Normal rails (adjusted for powered rails).
                - Powered rails.
                - Redstone torches.
            2. The materials needed for each component:
                - Normal rails: iron ingots and sticks.
                - Powered rails: gold ingots, sticks, and redstone dust.
                - Redstone torches: sticks and redstone dust.
            3. Total resources required across all components.

        Args:
            None

        Returns:
            None: Outputs the summary to the console.
        """

        normal_rails_dict = self.resources['normal_rails']
        powered_rails_dict = self.resources['powered_rails']
        redstone_torches_dict = self.resources['redstone_torches']

        # Calculate the actual number of normal rails required. 
        # This is determined by subtracting the number of powered rails from the total rails needed,
        # as powered rails replace some normal rails along the track.
        normal_rails_req = normal_rails_dict["rails"] - powered_rails_dict["rails"]

        # Computing totals for all required materials across all components
        totals = {
            'iron_ingots':self.minimum_craft('iron_ingot', normal_rails_dict['iron_ingots']),
            'gold_ingots':self.minimum_craft('iron_ingot', powered_rails_dict['gold_ingots']),
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