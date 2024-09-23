import numpy as np
import joblib
from model.preProcessador import PreProcessador


class Model:

    @staticmethod
    def carrega_modelo(path_model, path_scaler):
        """Carrega o modelo e o scaler usando joblib"""
        modelo = joblib.load(path_model)
        scaler = joblib.load(path_scaler)
        return modelo, scaler

    @staticmethod
    def preditor(modelo, scaler, X_input):
        """Aplica o scaler e realiza a predição"""
        # Garantindo que X_input seja um array 2D
        if len(X_input.shape) == 1:
            X_input = X_input.reshape(1, -1)
        
        # Aplicar o scaler nos dados de entrada
        X_input_scaled = scaler.transform(X_input)

        # Realizar a predição
        diagnosis = modelo.predict(X_input_scaled)
        return diagnosis