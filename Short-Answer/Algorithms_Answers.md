# Please add your answers to the **_Analysis of Algorithms_** exercises here

## Exercise I

a) This is O(n) because it loops based upon n

b) This is O(n^2) because of the use of the nested loop

c) This call is merely O(n) because recurisve calls just call upon themselves

## Exercise II

-   I would use a binary search method to obtain the answer for this question. This will provided a runtime complexity of O(log(n)).
-   Essentially, the building floors are already "sorted" from smallest floor to largest so I would just need to find a target where the egg would not break where dropped.

### Steps to Completion

1. Take the length of of floors and divide by two to get the middle floor that will be used for the pivot: `current_floor = len(building) // 2`
2. Drop the egg
3. If the egg breaks, take the lower half of the buildings and repeat the drop on the new pivot: `lower_half = current_floor // 2`
4. If the egg does not break, take the upper half of the building's floors and repeatt he drop on the new pivot: `building = upper_half = current_floor // 2`
5. Continue to repeat until the egg does not break and return whatever that new `current_floor` is while running a recurisve function on the `upper_half` and the `lower_half`
