(c) EBE

This only works using python lists.

First part finds all the regions. The regions are found using a DFS with a
todo-list which stores additional paths we have to check when there is more
than one way.

Then does for every region: check how many outside borders are for every point
in the region.


The second part reuses the region finding from the first part.

But then we have to count sides instead. To find contiguous lines a rather
simple approach was taken:

* For ever line in region: Only count side if previous point on line was an
  outside border and if previous point on line was not also an outside border. Do
  this for the top and the bottom line.
* For ever row in region: Same as above but with left and right borders.


```
get_sides explanation:

To check if its a top ^ new line segment:
* the top ^ must not be in the region, and
* the left < must not be in the region or not(the left < must be in the region and the left-top a must not be in the region)
   a^    
   <A
   
The last binary expression can then be simplified like so:
(left not in region) or not(left in region and top-left not in region)
first apply de-morgan on the right-side or sub-expression:
(left not in region) or (left not in region or top-left in region)
now apply associativity of or:
left not in region or left not in region or top-left in region
now apply commutativity of or:
left not in region or top-left in region

The same can be done for all other directions!
```
