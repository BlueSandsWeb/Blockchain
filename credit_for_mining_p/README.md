# Credit for mining

We've forgotten something important!  Miners want credit for the electricity they spend to mine a new block.  Right now, the server is simply recording a `0` as the sender.  We need to fix this to appropriately give credit where credit is due. 


# Task List

*Client*
Modify the client we created to:

[X] - Otherwise, create a UUID ID, removing `-`s and save it to a the file
    [X] - Use code from blockchain.py on line 238 to create UUID
    [X] - if no ID create a file called 'my_id'
    [X] - then add id in file called 'my_id'

[X] - Check for a file called `my_id`, open it if found, and load the ID
    [X] - open and read file
    [X] - check if line 1 is id or None 

[X] - When a solution is found, send the ID in the POST as `id`



*Server*
Modify the server we created to:

[X] - Receive an `id` from a `mine` request.
    [ ] - pull id out of json data in the request

Don't do this part:
[ ] - Record that ID as the `sender` in the transaction that creates the coin.

Instead do this
[X] - Record server ID as the `sender` in the transaction that creates the coin.
[X] - Record that ID as the `Recipient` in the transaction that creates the coin.


