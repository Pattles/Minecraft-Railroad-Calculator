# Minecraft Railroad Calculator
A (concept) tool to determine the required amount of normal rails, powered rails, and redstone torches to travel from one coordinate to another (e.g. (1024, 0) to (0, 0)).

The entire project can be split into 3 key segments, which are the following:
1. Develop the back-end, which includes the formulas, logic, and pretty much everything else needed for an MVP. ✅
2. Develop the GUI and add logic that connects the back-end to the front-end.
3. Port the whole thing to my <a href="https://pserikov.com" target="_blank">website</a>.

## Segment 1: Back-end
### Formulas
The quick formula for **iron ingots** required for a rail (normal/powered) craft is $0.375b$, where $b$ is the distance. Here's how I got to that formula:

```math
\text{\# iron ingots} = \frac{\text{\# blocks}}{\text{16 rails per craft}}*\text{6 iron per craft}
```

<!-- <p align="center">
  <img width="503" alt="Screenshot 2025-01-15 at 11 17 32 PM" src="https://github.com/user-attachments/assets/95c45c78-4c92-444f-90d7-2b11da708de0" />
</p> -->

So if we plug in 1000 blocks for the distance, we would need 375 ingots. However, you can't craft 1000 rails with 375 ingots, since every recipe requires 6 ingots for 16 rails. To solve this, the minimum_craft() function rounds every recipe to the nearest multiple of 6.

In addition, for optimal resource collection, you should place 1 powered rail per 32 normal rails placed, to maintain max minecart speed in vanilla Minecraft (as of 1.19). This means the distance would be divided by 32, so in the case of the distance being 1024 blocks, the "real blocks" would be only 32, meaning you'd need 32 powered rails–or just 2 crafts.

*Note: Technically it's 1 powered rail per 33 blocks, but I can't be bothered so I just rounded down.*

So the formula would be:
<!-- <p align="center">
  <img width="582" alt="Screenshot 2025-01-19 at 2 46 46 PM" src="https://github.com/user-attachments/assets/2dd2ef3d-b175-421e-8fe3-ab7d6e68e2cb" />
</p> -->

```math
\text{real blocks} = \frac{\text{\# blocks}}{32}
```
```math
\text{\# powered rails} = \frac{\text{real blocks}}{\text{16 rails per craft}}*\text{6 ingots per craft}
```

For **redstone torches/sticks** required for a rail craft is $0.0675b$. It's literally the same as the iron ingot formula, but $*1$ stick per craft instead of $*6$ ingots. Or in other words, just:

<!-- <p align="center">
  <img width="309" alt="Screenshot 2025-01-15 at 11 13 38 PM" src="https://github.com/user-attachments/assets/ae0591a5-49fc-4a4e-aebf-6390fd692545" />
</p> -->

```math
\text{\# sticks} = \frac{\text{\# blocks}}{\text{16 rails per craft}}
```
However, I didn't use the formula since the amount of redstone torches you need is literally the amount of powered rails you use. This is the (simplified) function that handles redstone torches:
```py
self.redstone_torches = powered_rails
self.sticks = powered_rails
self.redstone = powered_rails
```

### Output
My vision for the output includes the amount of normal rails, powered rails, and redstone torches, along with the necessary resources required to craft them.

```py
Enter the starting x & z coords (without commas): 1024 0
Enter the destination x & z coords (without commas): 0 0
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

## Segment 2: Design
My vision for the design is cute and minimalistic. When searching for resource calculators online, they're all blocky and resemble Minecraft. I don't want to do that, since it's the same literally everywhere.
<p align="center">
  <img width="503" alt="Screenshot 2025-01-15 at 11 17 32 PM" src="https://github.com/user-attachments/assets/1a7847e8-dae5-4ea6-b0e6-f3c9b174643b" />
</p>

