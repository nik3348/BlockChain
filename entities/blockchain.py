import datetime
import hashlib


class BlockChain:
    def __init__(self):
        self.chain = [self.genesis_block()]
        self.difficulty = 4

    @staticmethod
    def genesis_block():
        block = Block(0, "0", 0)
        block.hash = 0
        return block

    def get_latest_block(self):
        return self.chain[-1]

    def add(self, block):
        self.chain.append(block)

    def add_block(self, data):
        new_block = Block(self.get_latest_block().index_no + 1, data, self.get_latest_block().hash)
        self.mine_block(new_block)
        self.chain.append(new_block)
        return new_block

    def display(self):
        for block in self.chain:
            block.display()

    def mine_block(self, block):
        while not block.valid(self.difficulty):
            block.nonce += 1
            block.calculate_hash()


class Block:
    def __init__(self, index_no, data, previous_hash):
        self.index_no = index_no
        self.data = data
        self.timestamp = datetime.datetime.now()
        self.hash = None
        self.previous_hash = previous_hash
        self.nonce = -1

    def calculate_hash(self):
        self.hash = hashlib.sha256((
                                           str(self.index_no) +
                                           self.data +
                                           str(self.timestamp) +
                                           str(self.previous_hash) +
                                           str(self.nonce)
                                   ).encode("utf-8")).hexdigest()
        print(self.hash)

    def valid(self, difficulty):
        return str(self.hash)[:difficulty] == "0" * difficulty

    def display(self):
        print(
            "\nIndex         : " + str(self.index_no),
            "\nData          : " + self.data,
            "\nTimestamp     : " + str(self.timestamp),
            "\nHash          : " + str(self.hash),
            "\nPrevious hash : " + str(self.previous_hash),
            "\nNonce         : " + str(self.nonce)
        )
