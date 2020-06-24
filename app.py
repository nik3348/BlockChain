import pymongo as pymongo
import pprint
from entities.BlockChain import BlockChain
from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return 'Index Page'


p1 = BlockChain()
p1.add_block("John")
p1.add_block("Sherry")
p1.add_block("Berry")
p1.add_block("Dumbo")
p1.display()

client = pymongo.MongoClient(
    "mongodb+srv://root:root@cluster0-nde0z.gcp.mongodb.net/blockchain?retryWrites=true&w=majority"
)

db = client.blockchain
block = db.blocks

block.insert_one(p1.get_latest_block().__dict__)
pprint.pprint(block.find_one())
