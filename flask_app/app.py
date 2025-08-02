from flask import Flask, render_template

# Initialize the Flask app
app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def home():
    # Render the index.html file from the 'templates' folder
    return render_template('index.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)