from flask import Flask, render_template, request
import pickle
import numpy as np



clf = pickle.load(open('diabetes_model.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('1.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        preg = int(request.form['pregnancies'])
        glucose = int(request.form['glucose'])
        bp = int(request.form['bloodpressure'])
        st = int(request.form['skinthickness'])
        insulin = int(request.form['insulin'])
        bmi = float(request.form['bmi'])
        dpf = float(request.form['dpf'])
        age = int(request.form['age'])
        
        inp = np.array([[preg, glucose, bp, st, insulin, bmi, dpf, age]])
    
        
        return render_template('2.html', prediction=clf.predict(inp))

if __name__ == '__main__':
	app.run(debug=False)