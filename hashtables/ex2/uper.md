## Input
- source: "NONE" is our start
- destination: "NONE" is our end
- we have ten tickets
    - each ticket has two key value pairs: source: loc, destination: loc


## Output
- array of strings with entire route of our trip

## Relationship
- hash each ticket so that starting location is key & destination is value
- ex. "PIT": "ORD"
- when doing route, use i-1th location

## Tools
- insert
- retrieve


## Pseudocode
**First attempt** <br>
~~1. traverse tickets~~ <br>
~~2. use hash_table_insert - inputs for ht, source, and destination)~~ <br>
~~3. Create empty route dictionary (i commented out route = [None] * length)~~ <br>
~~4. Origin will have 'NONE' value,~~ <br>
~~5. use retrieve function on that to pull 'NONE' on source~~ <br>
~~6. Append destinations~~ <br>
~~7. As long as destination is not 'NONE'~~ <br>
~~8. Traverse through tickets~~ <br>

**Second attempt** <br>
1. Traverse tickets
2. User hash insert
3. Make 0th index of route same as hash retrieve(ht, 'NONE')
4. Traverse - starting at `1`th indexed item, to length of index
5. iterate through route using hash retrieve, next destination uses previous key
6. Remove last 'NONE' value once done traversing