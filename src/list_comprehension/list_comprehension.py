from utilities import *

"""
The most traditional way to build an array in any language would
be to declare an empty array and then have some kind of loop that
populates it by pushing elements into it one by one. In not very
distant history, depending on which programming language we are
using, this was really the only way to do things.
"""

tiles = []
for x in range(2):
    tiles.append(build_tile_1d(x))

print("\n=== Build 1 dimensional array in traditional iterative style. ===\n")
print(tiles)

"""
Most languages nowadays have tools that let you build such an array 
in a single statement, some way or another. This is better because 
it's simpler, and because it's declarative. Python has list 
comprehensions, which are designed for this specific use case.
"""

tiles = [build_tile_1d(x) for x in range(2)]

print("\n=== Build 1 dimensional array with a list comprehension. ===\n")
print(tiles)

"""
All a list comprehension is is a special syntax that smooshes the 
3 lines in the first example together.

Making a two dimensional array in the traditional style requires a 
bit more consideration. We want tiles to be an array of arrays in 
the end so that we can access it via the tiles[x][y] syntax. To 
create such a structure, we have to loop over one dimension and 
create a new array in each iteration of that first dimension. That 
sub-array will then be populated by looping over the second 
dimension. Then we append that sub-array to tiles and move onto the
next iteration of that outer dimension.
"""

tiles = []
for x in range(2):
  thisRow = []
  for y in range(2):
    thisRow.append(build_tile_2d(x, y))
  tiles.append(thisRow)

print("\n=== Build 2 dimensional array in traditional iterative style. ===\n")
print(tiles)

"""
The structure of this code is kind of complicated and finicky so 
it's not really obvious that this is the case, but the interesting 
thing about this code actually just two instances of the same 
"declare a list and then push stuff into it" pattern from our first
example.

The outer layer is just "declare tiles as an empty list and push 
some new lists into it" just like in the first example we had "declare 
tiles as an empty list and push some new strings into it". So that's 
the same, even if it takes several lines to make one "new list" as 
opposed to the single line it took to make one "new string".

The inner layer is "declare thisRow as an empty list and push some 
new strings into it" which we should notice is actually just the 
same as what we are doing in the first code snippet I have here. 
The variable has a different name, and the string we create is 
different, but the structure of what we are doing is the same.

Given that fact, we should be able to imagine a hybrid approach, 
where we use a list comprehension at least to build that sub-list 
on each iteration of the outer dimension.
"""

tiles = []
for x in range(2):
  thisRow = [build_tile_2d(x, y) for y in range(2)]
  tiles.append(thisRow)

print("\n=== Build 2 dimensional array in traditional iterative style / list comprehension hybrid. ===\n")
print(tiles)

"""
This can further be simplified by skipping the declaration of the 
thisRow variable.
"""

tiles = []
for x in range(2):
  tiles.append([build_tile_2d(x, y) for y in range(2)])

print("\n=== Build 2 dimensional array in traditional iterative style / list comprehension hybrid again. ===\n")
print(tiles)

"""
Now our code should look very similar to the first example here. The
x in tiles.append(x) is different, but other than that the shape is the
same. Just like with the first example, we can shift our 3 lines around
into a list comprehension.
"""

tiles = [[build_tile_2d(x, y) for y in range(2)] for x in range(2)]

print("\n=== Build 2 dimensional array with nested list comprehensions. ===\n")
print(tiles)

"""
So we have now an array of arrays built in a single statement.

An important note. Python doesn't actually have arrays. Python only has 
lists. So although I have been talking about arrays, these are 
called lists.
"""
