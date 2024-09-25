# Import Flask
from flask import Flask

# Main
app = Flask(__name__)

# Set route untuk /


@app.route("/")
# Function index
def index():
    return ("HALLO REK")


# debug, update server otomatis
if __name__ == "__main__":
    app.run(debug=True)
