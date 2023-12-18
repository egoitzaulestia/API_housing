# from flask import Flask, request, jsonify
# import os
# import pickle
# from sklearn.model_selection import cross_val_score
# import pandas as pd
# import sqlite3


# os.chdir(os.path.dirname(__file__))

# app = Flask(__name__)
# app.config['DEBUG'] = True

# @app.route("/", methods=['GET'])
# def hello():
#     return "Bienvenido a mi API del modelo advertising"


import pandas as pd
from flask import Flask, jsonify,request
from flask_cors import CORS
import pickle


app = Flask(__name__)
cors = CORS(app)


@app.route('/')
def home():
    return jsonify({'message': 'Welcome to the housing API!'})



# Cargar la base de datos en un DataFrame
# model = pd.read_pickle('modelo.pkl')
# @app.route('/predict', methods=['POST'])
# def predict():
#     data = data_init
#     # data = request.get_json()


#     surface = request.args.get('surface', None)
#     bedrooms = request.args.get('bedrooms', None)
#     restrooms = request.args.get('restrooms', None)
#     location = request.args.get('location', None)

#     data['surface'] = surface
#     data['bedrooms'] = bedrooms
#     data['restrooms'] = restrooms
#     for column in data:
#         if column == location:
#             data[location] = 1

#     # input_data = [[surface, bedrooms, restrooms, location]]
#     prediction = model.predict(data)
#     result = prediction
#     return result

# @app.route('/predict_price', methods=['POST'])  # Cambio el nombre del endpoint para evitar conflictos
# def predict_price():

#     model = pickle.load(open('modelo.pkl','rb'))

#     data = data_init.copy()  # Crear una copia de data_init para evitar modificar el original

#     surface = request.args.get('surface', type=int)  # Asegúrate de convertir a los tipos correctos
#     bedrooms = request.args.get('bedrooms', type=int)
#     restrooms = request.args.get('restrooms', type=int)
#     location = request.args.get('location')

#     data['surface'] = surface
#     data['bedrooms'] = bedrooms
#     data['restrooms'] = restrooms

#     if 'location_' + location in data.columns:
#         data['location_' + location] = 1  # Asegúrate de que el nombre de la columna coincida

#     prediction = model.predict(data)
#     return jsonify({'prediction': float(prediction[0])})

# @app.route('/predict_price', methods=['GET'])
# def predict_price():
#     model = pickle.load(open('modelo.pkl','rb'))


#     surface = request.args.get('surface', type=int)
#     bedrooms = request.args.get('bedrooms', type=int)
#     restrooms = request.args.get('restrooms', type=int)
#     location = request.args.get('location')
    
#     # Actualizar la columna de la ubicación
#     if location and 'location_' + location in data.columns:
#         data['location_' + location] = 1

#     # Asegurar que todas las columnas son del tipo correcto
#     for col in data.columns:
#         if data[col].dtype == 'object':
#             data[col] = pd.to_numeric(data[col], errors='coerce').fillna(0)

#     prediction = model.predict(data)
#     return jsonify({'prediction': float(prediction[0])})


    # return jsonify({'prediction': float(prediction[0])})

# Cargar la base de datos en un DataFrame
# model = pd.read_pickle('modelo.pkl')
# @app.route('/predict', methods=['POST'])
# def predict():
    

#     surface = int(data['surface'])
#     bedrooms = int(data['bedrooms'])
#     restrooms = int(data['restrooms'])

#     input_data = [[surface, bedrooms, restrooms]]
#     prediction = model.predict(input_data)

#     return jsonify({'prediction': float(prediction[0])})

# Cargar la base de datos en un DataFrame
# model = pd.read_pickle('models/model.pkl')
# @app.route('/predict', methods=['GET'])
# def predict():
#     # data = request.get_json()

#     surface = request.args.get('surface', None)
#     bedrooms = request.args.get('bedrooms', None)
#     restrooms = request.args.get('restrooms', None)

#     input_data = [[surface, bedrooms, restrooms]]
#     prediction = model.predict(input_data)

#     return jsonify({'prediction': float(prediction[0])})
#     # return prediction

@app.route('/predict', methods=['GET'])
def predict():

    model = pickle.load(open('modelo.pkl','rb'))

    surface = int(request.args.get('surface', None))
    bedrooms = int(request.args.get('bedrooms', None))
    restrooms = int(request.args.get('restrooms', None))

    input_data = [[surface, bedrooms, restrooms]]
    prediction = model.predict(input_data)

    return jsonify({'prediction': float(prediction[0])})

# app.run()

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001)