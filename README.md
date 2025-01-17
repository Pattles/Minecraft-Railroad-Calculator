# Minecraft Railroad Calculator
A (concept) tool to determine the required amount of normal rails, powered rails, and redstone torches to travel from one coordinate to another (e.g. (1000, 1000) to (0, 0)).

## Formulas
The quick formula for **iron ingots** required for a rail (normal/powered) craft is $0.375b$, where $b$ is the distance. Here's how I got to that formula:
<p align="center">
  <img width="503" alt="Screenshot 2025-01-15 at 11 17 32 PM" src="https://github.com/user-attachments/assets/95c45c78-4c92-444f-90d7-2b11da708de0" />
</p>

So if we plug in 1000 blocks for the distance, we would need 375 ingots.
**TODO: Round to the nearest multiple of 6.**


However, for optimal resource collection, you should place 1 powered rail per 32 normal rails placed, to maintain max minecart speed in vanilla Minecraft (as of 1.19). This means the distance would be divided by 32, so in the case of the distance being 1024 blocks, the "real blocks" would be only 32, meaning you'd need 32 powered rails–or just 2 crafts.

*Note: Technically it's 1 powered rail per 33 blocks, but I can't be bothered so I just rounded down.*

So the formula would be:
*There should be a picture here...*

For **redstone torches/sticks** required for a rail craft is $0.0675b$. It's literally the same as the iron ingot formula, but $*1$ stick per craft instead of $*6$ ingots. Or in other words, just:
<p align="center">
  <img width="309" alt="Screenshot 2025-01-15 at 11 13 38 PM" src="https://github.com/user-attachments/assets/ae0591a5-49fc-4a4e-aebf-6390fd692545" />
</p>

## My vision/TODO
**TODO: Round up crafting recipes to multiples of six, where needed. For example, if you're only travelling 12 blocks, you still need 6 ingots to craft 16 rails, not 4 ingots.**
**TODO: Fix docstrings.**

My vision for the output includes the amount of normal rails, powered rails, and redstone torches, along with the necessary resources required to craft them.

The process would look something like this:
```py
Enter the starting x & z coords (without commas):
Enter the destination x & z coords (without commas):
...
REQUIRED COMPONENTS:
Normal rails: 992
Powered rails: 32
Redstone torches: 32
--
REQUIRED MATERIALS:
Normal rails:
   Iron ingots: 384
   Sticks: 64
Powered rails:
   Gold ingots: 12
   Sticks: 2
   Redstone dust: 2
Redstone torches:
   Sticks: 32
   Redstone dust: 32
Total:
   Iron ingots: 384
   Gold ingots: 12
   Sticks: 98
   Redstone dust: 34
```