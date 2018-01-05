# Advent of Code 2017 - Day 4
Another nice and easy day. For part 1, we check for the uniqueness of each word, and for part 2, we check the same thing but with anagrams.
I found the easiest way to do this was to create a python list and use the `in` keyword.

## General Strategy
My strategy for problems of this sort is the following:
```Python
seen = []
valid = True
for word in phrase:
    if word in seen:
        valid = False
    else:
        seen.append(word)
```
At the end, `valid` will be the expected value.

## Part 1
Wrap the above strategy in `for phrase in phrases`, make a running counter `count`, then at the end of the outer loop
increment the counter if the phrase is valid. I do this in one line:
```Python
count += 1 if valid else 0
```

## Part 2
The general structure of part 2 is the same; however, instead of comparing the raw words, I instead
generate a string in which all the letters are the letters of the original word but sorted.
This is really easy to accomplish in Python: `"".join(sorted(x))` does the job nicely. I put this
in a function and ran the almost the same code as part 1 to get my answer.

And that wraps up day 4! See you at day 5.