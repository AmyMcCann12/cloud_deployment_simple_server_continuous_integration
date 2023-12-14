import os
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_home():
    return "I am a CI-CD hero"

if __name__ == '__main__':
    app.run(
      debug=True,
      host="0.0.0.0" # Listen for connections _to_ any server
    )
