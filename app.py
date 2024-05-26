from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the form
    sentence = request.form['sentence']

    # Perform sentiment analysis (simulated here)
    sentiment = 'positive' if len(sentence.split()) > 3 else 'negative'

    # Redirect to the appropriate result page
    return redirect(url_for(sentiment))

@app.route('/positive')
def positive():
    return render_template('positive.html')

@app.route('/negative')
def negative():
    return render_template('negative.html')

if __name__ == '__main__':
    app.run(debug=True)
