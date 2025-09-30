from flask import Flask, jsonify, render_template
import json

app = Flask(__name__)

# Load the UMAP data from the JSON file
# JSON file should include 'x', 'y', 'z', 'label', 'hover', 'sequence'
with open("umap_3d_data.json", "r") as f:
    umap_data = json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def get_umap_data():
    # Ensure all required fields are present
    required_keys = ['x', 'y', 'z', 'label', 'hover', 'sequence']
    for key in required_keys:
        if key not in umap_data:
            umap_data[key] = []
    return jsonify(umap_data)

if __name__ == '__main__':
    app.run(debug=True)
