import datetime
import hashlib


def genesis_block():
    block = Block(0, "0", 0, 0)
    block.hash = 0
    return block


class BlockChain:
    def __init__(self):
        self.chain = [genesis_block()]
        self.difficulty = 4

    # TODO: Proper way?
    def get_latest_block(self):
        return self.chain[len(self.chain) - 1]

    def add_block(self, data):
        new_block = Block(self.get_latest_block().index + 1, data, self.get_latest_block().hash, self.difficulty)
        self.chain.append(new_block)

    def display(self):
        for block in self.chain:
            block.display()


class Block:
    def __init__(self, index, data, previous_hash, difficulty):
        self.index = index
        self.data = data
        self.timestamp = datetime.datetime.now()
        self.previous_hash = previous_hash
        self.hash = None
        self.nonce = -1
        self.mine_block(difficulty)

    def calculate_hash(self):
        self.hash = hashlib.sha256((
            str(self.index) + self.data + self.timestamp.strftime("%m/%d/%Y, %H:%M:%S") + str(self.previous_hash) + str(
                self.nonce)).encode("utf-8")).hexdigest()
        print(self.hash)

    def mine_block(self, difficulty):
        while not self.valid(difficulty):
            self.nonce += 1
            self.calculate_hash()

    def valid(self, difficulty):
        return str(self.hash)[:difficulty] == "0" * difficulty

    # TODO: Format text
    def display(self):
        print(
            " Index         : " + str(self.index) + "\n",
            "Data          : " + self.data + "\n",
            "Timestamp     : " + str(self.timestamp) + "\n",
            "Hash          : " + str(self.hash) + "\n",
            "Previous hash : " + str(self.previous_hash) + "\n"
        )


p1 = BlockChain()
p1.add_block("John")
p1.add_block("Sherry")
p1.add_block("Berry")
p1.add_block("Dumbo")
p1.display()
