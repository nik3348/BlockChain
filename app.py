import os

import pymongo
from dotenv import load_dotenv
from flask import Flask, request

from entities.blockchain import BlockChain, Block

load_dotenv()
app = Flask(__name__)

db_connection = os.getenv("DBCONN")

client = pymongo.MongoClient(db_connection)
db = client.blockchain
col = db.blocks

chain = BlockChain()
for blocks in col.find():
    block = Block(blocks.get('nonce'), blocks.get('data'), blocks.get('previous_hash'), )
    block.index_no = blocks.get('_id')
    block.hash = blocks.get('hash')
    block.timestamp = blocks.get('timestamp')
    block.nonce = blocks.get('nonce')
    chain.add(block)

chain.display()


@app.route('/', methods=['GET'])
def index():
    return 'Index Page'


@app.route('/mine', methods=['POST'])
def mine():
    request_json = request.get_json()
    new_block = chain.add_block(request_json.get('data')).__dict__
    col.insert_one(new_block)
    return "Success"
