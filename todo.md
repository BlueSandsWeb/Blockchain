# Todo:

### Server Side

[X] - Remove proof of work function from the server
[X] - Change valid_proof to require 6 leading zeroes
[X] - Add an endpoint called last_proof that returns the proof of the last block in the chain
[X] - Modify the mine endpoint to instead receive and validate or reject a new proof sent by a client
[X] - Return a message indicating success or failure. Remember a valid proof should fail for all senders except the first
[X] - Add new block to blockchain if success
[X] - grant a coin if added block to blockchain is successful



### Client Side

[X] - Request the latest proof from the last_proof endpoint on the server
[X] - Run the proof_of_work function until a valid proof is found, validating or rejecting each attempt
[X] - Print messages indicating that this has started and finished. (Stretch: Add a timer)
[X] - Modify it to generate proofs with 6 leading zeroes.
[X] - When a valid proof is found, send it to the mine endpoint.
[X] - Print a message indicating the success or failure response from the server
[X] - Add any coins granted to a simple integer total, and print the amount of coins the client has earned
[X] - Continue mining until the app is interrupted.