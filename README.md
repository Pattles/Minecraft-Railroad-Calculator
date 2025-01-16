# Minecraft Railroad Calculator
A (concept) tool to determine the required amount of normal rails, powered rails, and redstone torches to travel from one coordinate to another (e.g. (1000, 1000) to (0, 0)).

## Formulas
The quick formula for **iron ingots** required for a rail (normal/powered) craft is $0.375b$, where $b$ is the distance. Here's how I got to that formula:
$$
\text{\# ingots}=\frac{\text{\# blocks}}{\text{16 rails per craft}}* \text{6 ingots per craft}
$$
So if we plug in 1000 blocks for the distance, we would need 375 ingots.
**TODO: Round to the nearest multiple of 6.**


However, for optimal resource collection, you should place 1 powered rail per 32 normal rails placed, to maintain max minecart speed in vanilla Minecraft (as of 1.19). This means the recipe for powered rails doesn't require the distance, but rather the amount of normal rails.

*Note: the formula in the code still uses distance since I'm an idiot and I came to this realization after I already wrote the code. In hindsight, it should use the normal rails.*
**TODO: Rework powered rails formula to use normal rails as the basis, as opposed to distance.**

*There should be a formula for powered rails somewhere here...*

For **redstone torches/sticks** required for a rail craft is $0.0675b$. It's literally the same as the iron ingot formula, but $*1$ stick per craft instead of $*6$ ingots. Or in other words, just:
$$
\text{\# sticks}=\frac{\text{\# blocks}}{\text{16 rails per craft}}
$$

