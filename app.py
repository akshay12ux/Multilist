from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('ngo.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS beneficiary (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT,
                 age INTEGER,
                 gender TEXT,
                 contact TEXT
                 )''')
    c.execute('''CREATE TABLE IF NOT EXISTS program (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT,
                 description TEXT
                 )''')
    c.execute('''CREATE TABLE IF NOT EXISTS enrollment (
                 beneficiary_id INTEGER,
                 program_id INTEGER,
                 FOREIGN KEY(beneficiary_id) REFERENCES beneficiary(id),
                 FOREIGN KEY(program_id) REFERENCES program(id)
                 )''')
    conn.commit()
    conn.close()

@app.route('/add_beneficiary', methods=['POST'])
def add_beneficiary():
    data = request.get_json()
    name = data['name']
    age = data['age']
    gender = data['gender']
    contact = data['contact']
    conn = sqlite3.connect('ngo.db')
    c = conn.cursor()
    c.execute("INSERT INTO beneficiary (name, age, gender, contact) VALUES (?, ?, ?, ?)", (name, age, gender, contact))
    conn.commit()
    conn.close()
    return jsonify({'message':'Beneficiary added successfully'})

@app.route('/add_program', methods=['POST'])
def add_program():
    data = request.get_json()
    name = data['name']
    description = data['description']
    conn = sqlite3.connect('ngo.db')
    c = conn.cursor()
    c.execute("INSERT INTO program (name, description) VALUES (?, ?)", (name, description))
    conn.commit()
    conn.close()
    return jsonify({'message':'Program added successfully'})

@app.route('/enroll', methods=['POST'])
def enroll():
    data = request.get_json()
    beneficiary_id = data['beneficiary_id']
    program_id = data['program_id']
    conn = sqlite3.connect('ngo.db')
    c = conn.cursor()
    c.execute("INSERT INTO enrollment (beneficiary_id, program_id) VALUES (?, ?)", (beneficiary_id, program_id))
    conn.commit()
    conn.close()
    return jsonify({'message':'Beneficiary enrolled successfully'})

@app.route('/beneficiaries', methods=['GET'])
def list_beneficiaries():
    conn = sqlite3.connect('ngo
