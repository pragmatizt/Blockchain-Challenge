### Inputs
- Number of items
- Weights of items


### Outputs
- Two items, sum of 21


### Relationship between Inputs and Outputs
- Larger of two items will be in 0th index
- Smaller on the 1st


### Tools
Hash Table Functions
- Insert - ht, key, value
- Retrieve - ht, key
- Remove - ht, key
- Resize - ht, key
- Subtraction (we know the weights of each item; find difference from 21)

### Notes
- What do we store in hash tables?
* If we store each weight's list index as its value, we can then check to see if the hash table contains an entry for `limit - weight`. If it does, then we've found the two items whose weights sum up to the `limit`!