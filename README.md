# forest_fire_skin_resistence
python mesa example forest_fire modified

## summary

The forest fire model is a simple, cellular automaton simulation of a fire spreading through a forest. The forest is a grid of cells, each of which can either be empty or contain a tree. Trees can be unburned (fine), on fire (on fire), or burned(burned out). The fire spreads from every on-fire tree to unburned neighbors if it can surpass the neighbor's skin resistence (random number greater or equal to skin resistence); the on-fire tree then becomes burned. This continues until the fire dies out.
