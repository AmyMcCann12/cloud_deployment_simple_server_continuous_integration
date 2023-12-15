import os
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_home():
    return render_template('website.html')

if __name__ == '__main__':
    app.run(
      debug=True,
      host="0.0.0.0",
      port=int(os.environ.get('PORT', 5001)) # Listen for connections _to_ any server
    )
