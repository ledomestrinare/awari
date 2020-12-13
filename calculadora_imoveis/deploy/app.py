import numpy as np
from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)
model = pickle.load(open('modelo.pkl', 'rb'))

zona_to_onehot = {'leste': np.array([1, 0, 0, 0]),
                  'norte': np.array([0, 1, 0, 0]),
                  'oeste': np.array([0, 0, 1, 0]),
                  'sul'  : np.array([0, 0, 0, 1])
                  }

def prepare_input(zona, quartos, area):
    zona_prep = zona_to_onehot[zona.lower()]
    quartos_prep = np.log1p(int(quartos))
    area_prep = np.log1p(int(area))
    return [np.r_[zona_prep, quartos_prep, area_prep]]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [x for x in request.form.values()]
    final_features = prepare_input(*features)
    print(final_features)
    prediction = np.expm1(model.predict(final_features))
    output = round(prediction[0], 2)

    return render_template('index.html',
            prediction_text=f'Preço do Aluguel R$ {output}')

if __name__ == '__main__':
    app.run(debug=True)
