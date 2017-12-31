# Advent of Code 2017 - Day 3
The puzzle today didn't really need any code - I only used Python as a calculator. I also took a handy shortcut for part 2 - turns out the sequence is already stored in an online database, so there's no need to calculate it out again. I may come back and rewrite my code to actually generate the aforementioned sequence, however.

## Part 1
Math to solve part 1:
1. Take the square root of the input, round up. Round up again if you get an even number. This gives you the *width of the ring* that your input resides in, aka the diameter.
2. Square this number to get the perfect square of the ring, which resides at the bottom right corner.
3. Integer-divide the ring width in half to get the radius of the ring. We're looking for the Manhattan distance from the origin to the input, so this will be a portion of the distance.
4. To compute the second part of the distance, we have to find the nearest midpoint. The first one is `ring_square - ring_radius`, then calculate the other three by repeatedly subtracting the diameter of the ring.
5. Find the midpoint closest to the input by taking the `abs()` of the difference. The smallest of the distances calculated by `abs()` is the other part of the distance; add that to the radius and you're done!

## Part 2
Sequence is on https://oeis.org/A141481; download the table and find the first entry bigger than your input. I downloaded the first 150 terms into a text file and looped through them.
