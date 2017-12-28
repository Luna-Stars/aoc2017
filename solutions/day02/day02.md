# Advent of Code 2017 - Day 2
Another nice and easy puzzle! In this one we have to calculate a simple checksum for a given array and then find two entries that evenly divide in each row.

## Input
I have a pretty nice one-liner using list comprehension to load input, but it might be a little unclear.
```Python
lines = [list(map(int, line.strip("\n").split("\t"))) for line in infile]
```
For each line, I strip whitespace and then break up the input using tabs as dividers. Then I convert each element to an integer using `map()` (which is amazing, by the way - use it) and create a list out of the whole thing. It makes a nice 2-dimensional list which is quite easy to iterate over.

## Part 1
Very simple - just use builtin `max()` and `min()` on each row, subtract the two, and add them to a running variable.

## Part 2
A little bit trickier, but still not too bad. For each row, we need to find the unique pair of entries that evenly divide each other. The brute force way would be as follows:
```Python
for item1 in line:
  for item2 in line:
    # check for:
    # a) not the same entry
    # b) dividing each other
```
However, in my solution I sacrifice conciseness for a bit of added efficiency. You don't have to loop through `O(n**2)` times - if you check `item1 % item2` *and* `item2 % item1`, you can just loop through all the items after `item1` in the smaller list. Then, to make sure I don't count duplicates (which would only happen in the case of an input error anyway), I `break` and go to the next row. This gives us this loop condition:
```Python
for i in range(len(line)):
      for j in range(i + 1, len(line)):
```
To reduce duplicate code, I made a check after computing the quotient instead of `break`ing/adding the quotient twice:
```Python
quotient = -1
# set quotient if the elements divide
if quotient != -1:
  divsum += quotient
  break
```

And that's day 2! Two more nice stars for our collection. See you at day 3!
