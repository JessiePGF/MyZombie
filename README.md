# Quant Zombie
A zombie build for Zombie Dice game, designed to make rational stop/roll decisions using Monte Carlo simulation.

# Strategy
- Rolls until 2 shotguns appear.
- If only 1 shotgun, simulate 1000 rounds using remaining dice.
- If ≥ 45% of simulations result in 2 or more shotguns, stop rolling.
- Otherwise, continue rolling for brains.

# How to install Zombie Dice
pip install zombiedice

# This zombie was built for:
- Trying my best to beat the Shotgun Zombie.
- Practicing simulation and Risk analysis.

# Result
- Quant Zombie wins around 320+ games out of 1000.
- Failed to defeat Shotgun Zombie.
