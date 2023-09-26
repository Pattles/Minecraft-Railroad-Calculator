total_iron_ingots, total_gold_ingots, total_sticks, total_redstone = 0, 0, 0, 0


def stack(resource:int):
    """
    Returns the amount of stacks a resource is, and how much is leftover
    rtype: int, int
    rdesc: stacks, remainder
    """
    remainder = resource % 64
    stacks = (resource / 64) - (remainder / 64)

    return round(stacks), round(remainder)

def rails(distance):
    """
    Returns the required amount of iron ingots and sticks (not stacked) for regular rails.
    rtype: int, int
    rdesc: iron_ingots, sticks
    """
    iron_ingots = 0.375 * distance
    sticks = 0.0625 * distance

    if iron_ingots % 6 != 0:
        round_up = 6 - (iron_ingots % 6)
        iron_ingots += round_up
    if sticks % 8 != 0:
        round_up = 8 - (sticks % 8)
        sticks += round_up

    # Tracking the total number of iron ingots and sticks.
    global total_iron_ingots
    global total_sticks
    total_iron_ingots += iron_ingots
    total_sticks += sticks

    return round(iron_ingots), round(sticks)
        
def powered_rails(distance:int):
    """
    Returns the required amount of gold ingots, sticks, and redstone (not stacked) for powered rails.
    rtype: int, int, int
    rdesc: gold_ingots, sticks, redstone
    """
    distance = round(distance / 32)
    gold_ingots = 0.375 * distance
    sticks = 0.0625 * distance
    
    if gold_ingots % 6 != 0:
        round_up = 6 - (gold_ingots % 6)
        gold_ingots += round_up
    if sticks % 8 != 0:
        round_up = 8 - (sticks % 8)
        sticks += round_up

    redstone = sticks
    
    # Tracking the total number of gold ingots, sticks, and redstone.
    global total_gold_ingots
    global total_sticks
    global total_redstone
    total_gold_ingots += gold_ingots
    total_sticks += sticks
    total_redstone += redstone
        
    return round(gold_ingots), round(sticks), round(redstone)

def redstone_torches(distance:int):
    """
    Returns the required amount of sticks and redstone (not stacked) for redstone torches.
    rtype: int, int
    rdesc: sticks, redstone
    """
    sticks = round(distance / 32)
    redstone = sticks

    # Tracking the total number of sticks and redstone.
    global total_sticks
    global total_redstone
    total_sticks += sticks
    total_redstone += redstone

    return sticks, redstone

if __name__ == '__main__':
    distance = int(input('How many blocks do you wish to travel?\nBlocks: '))
    
    iron_ingots, sticks = rails(distance)
    rail_resources = 'Regular rail resources required:\n' \
        + f'Iron Ingots: {stack(iron_ingots)[0]} stacks and {stack(iron_ingots)[1]}.\n' \
        + f'Sticks: {stack(sticks)[0]} stacks and {stack(sticks)[1]}.'
    print(rail_resources)

    gold_ingots, sticks, redstone = powered_rails(distance)
    powered_rail_resources = 'Powered rail resources required:\n' \
        + f'Gold Ingots: {stack(gold_ingots)[0]} stacks and {stack(gold_ingots)[1]}.\n' \
        + f'Sticks: {stack(sticks)[0]} stacks and {stack(sticks)[1]}.\n' \
        + f'Redstone: {stack(redstone)[0]} stacks and {stack(redstone)[1]}.'
    print(powered_rail_resources)

    sticks, redstone = redstone_torches(distance)
    redstone_torches_resources = 'Redstone torches resources required:\n' \
        + f'Sticks: {stack(sticks)[0]} stacks and {stack(sticks)[1]}.\n' \
        + f'Redstone: {stack(redstone)[0]} stacks and {stack(redstone)[1]}.'
    print(redstone_torches_resources)

    total_resources = '------------\n' \
        + 'Total resources required:\n' \
        + f'Iron Ingots: {stack(total_iron_ingots)[0]} stacks and {stack(total_iron_ingots)[1]}.\n' \
        + f'Gold Ingots: {stack(total_gold_ingots)[0]} stacks and {stack(total_gold_ingots)[1]}.\n' \
        + f'Sticks: {stack(total_sticks)[0]} stacks and {stack(total_sticks)[1]}.\n' \
        + f'Redstone: {stack(total_redstone)[0]} stacks and {stack(total_redstone)[1]}.\n'
    print(total_resources)


