

chain of thought:

part 1 is trivial

part 2:
endless loops can be detected if position was already visited with the _same_ direction.
In the code this check is done using the set() `path_and_dir`.

then bruteforce setting '#' to every possible position on the original
path.

Takes approx 5 seconds for the big input.
