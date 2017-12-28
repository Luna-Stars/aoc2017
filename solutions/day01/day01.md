# Advent of Code 2017 - Day 01
For the first problem of the year, we had to solve a caption to prove that we *weren't* human. Both of the parts involved jumping around the digits of a number, and we were given a very long number. For part 1, summed the digits that matched their following digits; for part 2, we summed those that matched the one halfway around the list. Overall, this was a pretty easy start to AoC 2017.

## Input handling
I just threw the input number on a single line in `input.txt`. In my file, I loaded the line in, but I *didn't* convert it to an `int`, as it's easier to index through the digits in string form.

## Solving the problems
Both of these were pretty straightforward - loop through the digits of the input, compute the index of the next digit, compare the digits, and add to the sum if they match. Easy to compute, fast to run.

Below is an overview of my logic for computing the next index (which is the only thing that's different between parts 1 and 2):

### Part 1
To compute the next index, add 1 to the current one, and if the result is out of bounds, just use 0. You could do this as an if statement to make it clearer than my code:

```Python
if i == len(intxt):
  next_i = 0
else:
  next_i = i + 1
```

That's the expanded version of my handy one-liner.

```Python
comp = intxt[0] if i == len(intxt) - 1 else intxt[i + 1]
```

## Part 2
For part 2, we either add or subtract half the input length, depending on the position of the current index.

My one-liner:
```Python
comp = intxt[i - half] if i >= half else intxt[i + half]
```

The expanded version:
```Python
if i >= half:
  next_i = i - half
else:
  next_i = i + half
```

And that's a wrap for day 1! Two gold stars closer to debugging the printer.
