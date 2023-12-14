from flask import Flask, request, jsonify
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import csv
import secrets
import hashlib
import time
import json
import os

app = Flask(__name__)

def encrypt_data(key, iv, data):
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    ct_bytes = cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))
    return ct_bytes.hex()

def build_index_and_csv_rows(key, iv, csv_file):
    index = {}
    csv_rows = []
    with open(csv_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row_id, row in enumerate(reader):
            encrypted_row = [encrypt_data(key, iv, word) for word in row]
            csv_rows.append(encrypted_row)
            for encrypted_word in encrypted_row:
                if encrypted_word not in index:
                    index[encrypted_word] = []
                index[encrypted_word].append(row_id)
    return index, csv_rows

def compute_hash(row):
    row_str = ' '.join(row).encode('utf-8')
    hash_obj = hashlib.sha256()
    hash_obj.update(row_str)
    return hash_obj.hexdigest()

def save_data(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file)

def load_data(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    return None

@app.route('/')
def home():
    return 'Welcome to the Searchable Symmetric Encryption Service!'

@app.route('/search', methods=['POST'])
def search():
    keyword = request.form['keyword']
    start_time = time.time()
    row_ids = index.get(encrypt_data(key, iv, keyword), [])
    result_rows = []
    result_hashes = []

    unique_row_ids = set()

    for row_id in row_ids:
        if row_id not in unique_row_ids:
            row = csv_rows[row_id]
            result_rows.append(row)
            unique_row_ids.add(row_id)
            result_hashes.append(compute_hash(row))

    end_time = time.time()
    search_time = end_time - start_time

    return jsonify({"result": result_rows, "hashes": result_hashes, "search_time": search_time})

@app.route('/web')
def web_interface():
 return '''
    <html>
    <head>
        <title>SSE Search</title>
        <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    </head>
    <body>
        <h1>Searchable Symmetric Encryption Service</h1>
        <input type="text" id="keyword" placeholder="Enter keyword">
        <button onclick="search()">Search</button>
        <div id="result"></div>
        <div id="searchTime"></div>

        <script>
            function search() {
                var keyword = $('#keyword').val();
                var startTime = Date.now();
                $.post("/search", { keyword: keyword }, function(data) {
                    var result = data.result;
                    var hashes = data.hashes;
                    if (result.length > 0) {
                        var htmlResult = '<table>';
                        for (var i = 0; i < result.length; i++) {
                            var row = result[i];
                            var hash = hashes[i];
                            htmlResult += '<tr>';
                            for (var j = 0; j < row.length; j++) {
                                htmlResult += '<td>' + row[j] + '</td>';
                            }
                            htmlResult += '<td>' + hash + '</td>';
                            htmlResult += '</tr>';
                        }
                        htmlResult += '</table>';
                        $('#result').html(htmlResult);
                    } else {
                        $('#result').html("No result found");
                    }
                    var endTime = Date.now();
                    var searchTime = endTime - startTime;
                    $('#searchTime').html("Search time: " + searchTime + " ms");
                });
            }
        </script>
    </body>
</html>
'''

if __name__ == '__main__':
    key = secrets.token_bytes(16)
    iv = secrets.token_bytes(16)

    # Define the paths where the index and CSV rows will be stored
    storage_path = 'C:\\Users\\PRITHVI\\Downloads\\Project Database\\'  # Replace with your desired path
    index_file = os.path.join(storage_path, 'encrypted_index.json')
    csv_rows_file = os.path.join(storage_path, 'encrypted_csv_rows.json')

    # Check if the index and CSV rows have already been saved
    index = load_data(index_file)
    csv_rows = load_data(csv_rows_file)

    # If not, build and save them
    if index is None or csv_rows is None:
        csv_file = 'C:\\Users\\PRITHVI\\Downloads\\Project Database\\enronThread2001.csv'  # Replace with your CSV file path
        index, csv_rows = build_index_and_csv_rows(key, iv, csv_file)
        save_data(index_file, index)
        save_data(csv_rows_file, csv_rows)

    app.run(port=5000)