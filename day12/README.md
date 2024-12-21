
This only works using python lists.

First part finds all the regions. The regions are found using
a DFS with a todo list which stores additional paths we have
to check when there is more than one way.

Then does for every region: check how many outside borders are for every point in the region.


The second part reuses the region finding from the first
part.

But then we have to count sides instead. To find contigous
lines a rather simple approach was taken:
For ever line in region: Only count side if previous point on line was an outside border and if previous point on line was not also an outside border. Do this for the top and the bottom line.

For ever row in region: Same as above but with left and right borders.

