
# =========================================  Client ======================================= #

import hashlib
import requests

import sys


# TODO: Implement functionality to search for a proof

# ----- PROOF OF WORK FUNCTION ----- #
def proof_of_work(last_proof):
    print("Beginning proof of work")
    # Simple Proof of Work Algorithm
    proof = 0
    while valid_proof(last_proof, proof) is False:
        proof += 1

    return proof

#  ----- PROOF OF WORK VALIDATOR ----- #
def valid_proof(last_proof, proof):
    # Validates the Proof:  Does hash(last_proof, proof) contain 4
    # leading zeroes?

    guess = f'{last_proof}{proof}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    return guess_hash[:6] == "000000"


# ==================================================== MINING LOOP ==================================================== # 

if __name__ == '__main__':
    # What node are we interacting with?
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "http://localhost:5000"

    coins_mined = 0
    # Run forever until interrupted
    while True:
        # Get the last proof from the server and look for a new one
        response = requests.get(url = f'{node}/last_proof')
        prev_proof = response.json()['proof']

        # Generate new proof
        new_proof = proof_of_work(prev_proof)
        data = {'proof': new_proof}

        print("NEW PROOF: ", new_proof)
        # TODO: When found, POST it to the server {"proof": new_proof}
        success = requests.post(url = f'{node}/mine', json = data)
        print("success: ", success)

        # TODO: If the server responds with 'New Block Forged'
        # add 1 to the number of coins mined and print it.  Otherwise,
        # print the message from the server.
        pass

