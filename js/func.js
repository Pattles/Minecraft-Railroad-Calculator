function railDistance(coord1, coord2) {
    /* Calculates the Manhattan distance between two coordinates on a 2D plane (ignoring vertical movement).
    
    This function computes the total distance required to travel along a grid (x, z) in Minecraft using rails, 
    where movement is restricted to horizontal axes. It assumes that the vertical (y) axis is handled separately 
    by other mechanisms like powered rails or minecart elevators.
    
    Args:
        coord1 (tuple): The starting coordinates as (x1, z1).
        coord2 (tuple): The destination coordinates as (x2, z2).
    
    Returns:
        int: The distance between the two points along the rails, calculated as the sum of absolute differences
             between the x and z coordinates.
    */

    let distance = Math.abs(coord2[0] - coord1[0]) + Math.abs(coord2[1] - coord1[1]);
    return distance
}

function stacks(amount) {
    /*
    Calculates the amount of stacks (1 stack = 64 items) and remainder from a non-simplified integer.
    */

    let numStacks = 0;
    let numRemainder = 0;
    // If there's an even amount of stacks, return the amount of stacks and nothing left over.
    if (amount % 64 == 0) {
        numStacks = Math.floor(amount / 64 );
        return [numStacks, 0];
    }
    // Otherwise, return the amount of stacks and the remainder.
    numStacks = Math.floor(amount / 64);
    numRemainder = amount % 64
    return [numStacks, numRemainder];
}

function displayStacks(amount) {
    let numStacks = stacks(amount)[0]
    let numRemainder = stacks(amount)[1]
    let message = ''

    if (numStacks == 0) {
        message = `${numRemainder} item${numRemainder == 1 ? '' : 's'}`
    } else if (numRemainder == 0) {
        message = `${numStacks} stack${numStacks == 1 ? '' : 's'}`;
    } else {
        message = `${numStacks} stack${numStacks == 1 ? '' : 's'} and ${numRemainder} item${numRemainder == 1 ? '' : 's'}`;
    }

    return message;

}

function updateTableRow(trId, tooltipId, resourceKey, resourceDict) {
    /**
    * Updates a table row's required resources and tooltip text.
    *
    * @param {string} rowId - The ID of the table row to update.
    * @param {string} tooltipId - The ID of the tooltip element to update.
    * @param {string} resourceKey - The key in the resource dictionary corresponding to the resource value.
    * @param {Object} resourceDict - An object containing resource values keyed by resource names.
    *
    * @example
    * const resources = { torches: 128, sticks: 64 };
    * updateTableRow('redstone-torches', 'redstone-torches-tooltip-torches', 'torches', resources);
    */

    // Locate the row and tooltip container
    let tr = document.getElementById(trId);
    let ttContainer = tr.children[1].querySelector('.tooltip-container');

    // Update the tr textContent with the required resource amount (e.g. 0, 1024, etc.)
    ttContainer.firstChild.textContent = resourceDict[resourceKey]; // Req resources

    // Update the tooltip text with stacks and remainder
    let tooltip = document.getElementById(tooltipId);
    tooltip.textContent = displayStacks(resourceDict[resourceKey]); // Num stacks & remainder tooltip
}


class CraftingRecipe {
    constructor(blocks) {
        this.blocks = blocks;

        this.resources = {
            'normalRails':{
                'rails':0,
                'ironIngots':0,
                'sticks':0
                },
            'poweredRails':{
                'rails':0,
                'goldIngots':0,
                'sticks':0,
                'redstone':0
                },
            'redstoneTorches':{
                'torches':0,
                'sticks':0,
                'redstone':0
                }
            };

        } 

    minimumCraft(name, amount) {
        /*
        Ensures the resource amount meets the minimum required for crafting.

        Args:
            name (str): The name of the resource (e.g., 'ironIngot', 'goldIngot').
            amount (float): The current amount of the resource.

        Returns:
            int: The minimum required resource amount based on the recipe.
        */

        // Define minimum amount of resource required for recipe
        const resourceThresholds = {
            'ironIngot':6,
            'goldIngot':6,
            'stick':1,
            'redstone':1
        };

        // Check if the amount is not a multiple of the threshold.
        // If it's not, calculate the nearest multiple of the threshold that is greater than or equal to the amount.
        // This is done by adding the difference between the threshold and the remainder (amount % threshold) to the amount.
        if (amount % resourceThresholds[name] != 0) {
            const x = amount + (resourceThresholds[name] - (amount % resourceThresholds[name]));
            return x;
        }

        // If the amount is already a multiple, return it as is.
        return amount;
        }
    
    poweredRail() {
        /*
        Calculates the resources required to craft powered rails based on the travel distance.

        Powered rails need to be placed once every 32 blocks for optimal performance, 
        meaning the total number of powered rail blocks ('powered blocks') is determined by dividing 
        the travel distance by 32 (rounded up). 

        This method computes the required quantities of gold ingots, sticks, and redstone dust 
        for the powered rails, ensuring that minimum crafting thresholds are met (e.g., gold ingots).

        Returns:
            None: Updates the `resources['poweredRails']` dictionary with:
                - 'rails' (int): The number of powered rail blocks required.
                - 'goldIngots' (int): The number of gold ingots needed.
                - 'sticks' (int): The number of sticks needed.
                - 'redstone' (int): The amount of redstone dust needed.
        */

        let poweredBlocks = Math.ceil(this.blocks / 32);

        this.resources['poweredRails']['rails'] = poweredBlocks;
        this.resources['poweredRails']['goldIngots'] = this.minimumCraft('goldIngot', Math.ceil(poweredBlocks * 0.375));
        this.resources['poweredRails']['sticks'] = Math.ceil(poweredBlocks * 0.0625);
        this.resources['poweredRails']['redstone'] = Math.ceil(poweredBlocks * 0.0625);
        return;
        }

    normalRail() {
        /*
        Calculates the resources required to craft normal rails based on the number 
        of blocks in the travel distance. 
        
        This method computes the required quantities of iron ingots and sticks 
        for the powered rails, ensuring that minimum crafting thresholds are met (e.g., iron ingots).

        Returns:
            None: Updates the `resources['normalRails']` dictionary with:
                - 'rails' (int): The number of powered rail blocks required.
                - 'ironIngots' (int): The number of iron ingots needed.
                - 'sticks' (int): The number of sticks needed.
        */
        // Calculate the actual number of normal rails required. 
        // This is determined by subtracting the number of powered rails from the total rails needed,
        // as powered rails replace some normal rails along the track.
        let actualBlocks = this.blocks - this.resources['poweredRails']['rails']

        
        this.resources['normalRails']['rails'] = actualBlocks;
        this.resources['normalRails']['ironIngots'] = this.minimumCraft('ironIngot', Math.ceil(actualBlocks * 0.375));
        this.resources['normalRails']['sticks'] = Math.ceil(actualBlocks * 0.0625);
        return;
        }

    redstoneTorch(poweredRails) {
        /*
        Calculates the resources required to craft redstone torches based on the number 
        of powered rails needed for the travel distance.

        This method computes the required quantities of sticks and redstone dust 
        to craft the necessary number of redstone torches. The calculations assume that 
        one stick and one redstone dust are needed for each redstone torch.

        Returns:
            None: Updates the `resources['redstone_torches']` dictionary with:
                - 'torches' (int): The total number of redstone torches required (equal to `poweredRails`).
                - 'sticks' (int): The total number of sticks needed (equal to `poweredRails`).
                - 'redstone' (int): The total amount of redstone dust needed (equal to `poweredRails`).
        */

        this.resources['redstoneTorches']['torches'] = poweredRails;
        this.resources['redstoneTorches']['sticks'] = poweredRails;
        this.resources['redstoneTorches']['redstone'] = poweredRails;
        return;
        }

    display() {
        /*
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
        */ 

        let normalRailsDict = this.resources['normalRails'];
        let poweredRailsDict = this.resources['poweredRails'];
        let redstoneTorchesDict = this.resources['redstoneTorches'];

        // Computing totals for all required materials across all components
        let totalsDict = {
            'ironIngots':this.minimumCraft('ironIngot', normalRailsDict['ironIngots']),
            'goldIngots':this.minimumCraft('ironIngot', poweredRailsDict['goldIngots']),
            'sticks':normalRailsDict['sticks'] + poweredRailsDict['sticks'] + redstoneTorchesDict['sticks'],
            'redstone':poweredRailsDict['redstone'] + redstoneTorchesDict['redstone']
            };

        // Updating Normal Rails table
        // Rails
        updateTableRow(
            'normal-rails',
            'normal-rails-tooltip',
            'rails',
            normalRailsDict
        );

        // Iron Ingots
        updateTableRow(
            'normal-rails-iron-ingots',
            'normal-rails-tooltip-iron-ingots',
            'ironIngots',
            normalRailsDict
        );

        // Sticks
        updateTableRow(
            'normal-rails-sticks',
            'normal-rails-tooltip-sticks',
            'sticks',
            normalRailsDict
        );

        // Updating Redstone Torches table
        // Torches
        updateTableRow(
            'redstone-torches',
            'redstone-torches-tooltip-torches',
            'torches',
            redstoneTorchesDict
        );

        // Sticks
        updateTableRow(
            'redstone-torches-sticks',
            'redstone-torches-tooltip-sticks',
            'sticks',
            redstoneTorchesDict
        );
        
        // Redstone
        updateTableRow(
            'redstone-torches-redstone',
            'redstone-torches-tooltip-redstone',
            'redstone',
            redstoneTorchesDict
        );

        // Updating Powered Rails table
        // Rails
        updateTableRow(
            'powered-rails',
            'powered-rails-tooltip-rails',
            'rails',
            poweredRailsDict
        );

        // Gold Ingots
        updateTableRow(
            'powered-rails-gold-ingots',
            'powered-rails-tooltip-gold-ingots',
            'goldIngots',
            poweredRailsDict
        );

        // Sticks
        updateTableRow(
            'powered-rails-sticks',
            'powered-rails-tooltip-sticks',
            'sticks',
            poweredRailsDict
        );

        // Redstone
        updateTableRow(
            'powered-rails-redstone',
            'powered-rails-tooltip-redstone',
            'redstone',
            poweredRailsDict
        );

    
        // Updating Totals table
        // Normal Rails
        updateTableRow(
            'totals-normal-rails',
            'totals-tooltip-normal-rails',
            'rails',
            normalRailsDict
        );

        // Powered Rails
        updateTableRow(
            'totals-powered-rails',
            'totals-tooltip-powered-rails',
            'rails',
            poweredRailsDict
        );

        // Redstone Torches
        updateTableRow(
            'totals-redstone-torches',
            'totals-tooltip-redstone-torches',
            'torches',
            redstoneTorchesDict
        );

        // Iron Ingots
        updateTableRow(
            'totals-iron-ingots',
            'totals-tooltip-iron-ingots',
            'ironIngots',
            totalsDict
        );

        // Gold Ingots
        updateTableRow(
            'totals-gold-ingots',
            'totals-tooltip-gold-ingots',
            'goldIngots',
            totalsDict
        );

        // Sticks
        updateTableRow(
            'totals-sticks',
            'totals-tooltip-sticks',
            'sticks',
            totalsDict
        );

        // Redstone
        updateTableRow(
            'totals-redstone',
            'totals-tooltip-redstone',
            'redstone',
            totalsDict
        );
        
        }
    }

function buttonSubmit() {
    // Retrieving the required distance between 2 coords
    const inputStartCoord = document.getElementById('start-coord').value.split(' ');
    const inputEndCoord = document.getElementById('end-coord').value.split(' ');

    let inputBlocks = railDistance(inputStartCoord, inputEndCoord);
    let cRecipe = new CraftingRecipe(inputBlocks);

    // Calculating resources required
    cRecipe.poweredRail();
    cRecipe.normalRail();
    cRecipe.redstoneTorch(cRecipe.resources['poweredRails']['rails']);

    // Displaying all of it
    cRecipe.display();

}