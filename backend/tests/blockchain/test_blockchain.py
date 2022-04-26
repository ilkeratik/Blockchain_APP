import pytest

from backend.blockchain.blockchain import Blockchain
from backend.blockchain.block import GENESIS_DATA

def test_blockchain_instance():
    blockchain = Blockchain()

    assert blockchain.chain[0].hash == GENESIS_DATA['hash']

def test_add_block():
    blockchain = Blockchain()
    data = 'test_data'
    blockchain.add_block(data)

    assert blockchain.chain[-1].data == data # does adding took affect on the chain?

@pytest.fixture
def blockchain_w_five_blocks():
    blockchain = Blockchain()
    for i in range(5):
        blockchain.add_block(i)
    return blockchain
def test_is_valid_chain(blockchain_w_five_blocks):
    Blockchain.is_valid_chain(blockchain_w_five_blocks.chain)

def test_is_valid_chain(blockchain_w_five_blocks):
    blockchain_w_five_blocks.chain[0].hash = 'bad_hash'
    
    with pytest.raises(Exception, match='The genesis block must be valid'):
        Blockchain.is_valid_chain(blockchain_w_five_blocks.chain)
