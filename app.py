import datetime
import hashlib
from flask import Flask
app = Flask(__name__)


class BlockChain:
    def __init__(self):
        self.chain = [self.genesis_block()]
        self.difficulty = 1

    @staticmethod
    def genesis_block():
        block = Block(0, "0", 0, 0)
        block.hash = 0
        return block

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        new_block = Block(self.get_latest_block().index_no + 1, data, self.get_latest_block().hash, self.difficulty)
        self.chain.append(new_block)

    def display(self):
        for block in self.chain:
            block.display()


class Block:
    def __init__(self, index_no, data, previous_hash, difficulty):
        self.index_no = index_no
        self.data = data
        self.timestamp = datetime.datetime.now()
        self.previous_hash = previous_hash
        self.hash = None
        self.nonce = -1
        self.mine_block(difficulty)

    def calculate_hash(self):
        self.hash = hashlib.sha256((
            str(self.index_no) + self.data + self.timestamp.strftime("%m/%d/%Y, %H:%M:%S") + str(self.previous_hash) + str(
                self.nonce)).encode("utf-8")).hexdigest()
        print(self.hash)

    def mine_block(self, difficulty):
        while not self.valid(difficulty):
            self.nonce += 1
            self.calculate_hash()

    def valid(self, difficulty):
        return str(self.hash)[:difficulty] == "0" * difficulty

    def display(self):
        print(
            "\nIndex         : " + str(self.index_no),
            "\nData          : " + self.data,
            "\nTimestamp     : " + str(self.timestamp),
            "\nHash          : " + str(self.hash),
            "\nPrevious hash : " + str(self.previous_hash)
        )


@app.route('/')
def index():
    return 'Index Page'


p1 = BlockChain()
p1.add_block("John")
p1.add_block("Sherry")
p1.add_block("Berry")
p1.add_block("Dumbo")
p1.display()
