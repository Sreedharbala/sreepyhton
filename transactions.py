from flask import Blueprint, jsonify, request
import json
import os

transaction_blueprint = Blueprint('transactions', __name__)

TRANSACTIONS_FILE = 'transactions.json'

def save_transactions(transactions):
    with open('C://Users//Lenovo//Desktop//requirements.txt', 'w') as f:
        json.dump(transactions, f)

def load_transactions():
    if os.path.exists('C://Users//Lenovo//Desktop//requirements.txt'):
        with open('C://Users//Lenovo//Desktop//requirements.txt') as f:
            return json.load(f)
    else:
        return {}

@transaction_blueprint.route('/transaction/<id>', methods=['GET'])
def get_transaction(id):
    with open('transactions.json') as data_file:
        transactions_data = json.load(data_file)
        transaction = transactions_data.get(id, None)
        return jsonify(transaction), 200

@transaction_blueprint.route('/transaction', methods=['POST'])
def add_transaction():
        # TODO
    return

@transaction_blueprint.route('/transaction/<id>', methods=['PUT'])
def update_transaction(id):
        # TODO
    return

@transaction_blueprint.route('/transaction/<id>', methods=['DELETE'])
def delete_transaction(id):
        # TODO
    return
# TODO : ADD A GET ALL TRANSACTIONS ENDPOINT ASWELL
