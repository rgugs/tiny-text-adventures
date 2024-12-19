# Tiny Text Adventures Notes

## Needs

1. Use Pyodide to convert python into WASM to run in browser window
   1. <https://pyodide.org/en/stable/>
2. Game loop
   1. Able to enter a time to play as a designated break time?
3. Player
4. NPCs
5. Rooms
6. Non Fighting things to do
   1. Gardening
   2. Making potions
   3. Escape Room style riddles
7. Fighting
   1. Training
   2. NPCs
      1. Pour a potion on a plant to make it grow has a small chance of making it grow legs and become mobile and attack
8. Different worlds
   1. Dungeon
      1. Train to fight dummies
      2. Fight rats
      3. Fight
   2. Forest (What kind?)
      1. Explore forest
      2. Identify plants/animals
      3. Check off finds in your Nature journal
   3. Tower
   4. Plains
      1. Praire dog town
         1. Larger world
         2. Can dig to open new rooms/exits
         3. Above and below ground rooms
         4. Fight snakes, hawks, coyotes
         5. Must go above ground to eat grass
   5. Garden
      1. Grow plants
      2. Harvest plants
      3. Mix potions
      4. Fight bugs invading garden
      5. Fight occasional sentient plant
   6. Dinosaurs
      1. Players - Predator or prey
      2. Eat
      3. Survive
   
## Movement

To use a grid system or not? It would make movement and tracking location in the game easier. The Garden world doesn't have up or down, but it seems like it would be simple to add in a dimension or level attribute to track that and then continue to maintain the grid system since they wouldn't move sideways when going up or down.
