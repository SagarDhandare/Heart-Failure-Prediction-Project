from flask import Flask, render_template, request
import jsonify
import requests
import pickle
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model = pickle.load(open('LogisReg.pickle', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

stdscale = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        age = float(request.form['age'])
        anaemia = int(request.form['anaemia'])
        creatinine_phosphokinase = int(request.form['creatinine_phosphokinase'])
        diabetes = int(request.form['diabetes'])
        ejection_fraction = int(request.form['ejection_fraction'])
        high_blood_pressure = int(request.form['high_blood_pressure'])
        platelets = float(request.form['platelets'])
        serum_creatinine = float(request.form['serum_creatinine'])
        serum_sodium = int(request.form['serum_sodium'])
        sex = int(request.form['sex'])
        smoking = int(request.form['smoking'])
        
        lst1 = [[age, anaemia, creatinine_phosphokinase, diabetes, ejection_fraction, high_blood_pressure, platelets, serum_creatinine, serum_sodium, sex, smoking]]
        lst2 = stdscale.fit_transform(lst1)
        prediction = model.predict(lst2)
        prediction = int(prediction)

        
        if prediction == 1:
            return render_template('result.html', prediction_text='Your chances of getting heart failure is high, we kindly request you to take good care of your health')
        else:
            return render_template('result.html', prediction_text='You are robust, nothing to worry')

    else:
        return render_template('result.html')

if __name__=="__main__":
    app.run(debug=True)
