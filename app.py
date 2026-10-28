from flask import Flask

app = Flask(__name__)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

@app.route("/")
def home():
    # Hardcoded values for demonstration
    a = 10
    b = 5
    
    add_result = add(a, b)
    sub_result = subtract(a, b)
    
    # Returns simple text directly to the browser screen
    return f"""
    <h1>Menu-Driven Calculator</h1>
    <p>Addition of {a} and {b} is: <b>{add_result}</b></p>
    <p>Subtraction of {a} and {b} is: <b>{sub_result}</b></p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)