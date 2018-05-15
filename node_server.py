from hashlib import sha256
import json


class Block:
    def __init__(self, index, transaction, timestamp):
        self.index = []
        self.transaction = transaction
        self.timestamp = timestamp

    def compute_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()
