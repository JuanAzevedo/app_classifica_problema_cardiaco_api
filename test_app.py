import pytest
import numpy as np
from model.carregador import Carregador
from model.modelo import Model
from model.avaliador import Avaliador
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Teste de Carregamento de Dados
def test_carregar_dados():
    url = 'https://raw.githubusercontent.com/JuanAzevedo/dataset_heart_disease_prediction/refs/heads/main/Heart_Disease_Prediction.csv'
    atributos = ['age', 'sex', 'BP', 'cholesterol', 'chest_pain_type', 'ST_depression', 'heart_disease']
    df = Carregador.carregar_dados(url, atributos)
    
    assert df is not None, "Dataframe não deve ser None"
    assert len(df.columns) == len(atributos), "O número de colunas deve ser igual ao número de atributos fornecidos"

# Teste da Predição do Modelo
def test_model_prediction():
    # Caminhos dos modelos salvos
    model_path = './machineLearning/model/knn_model.pkl'
    scaler_path = './machineLearning/scaler/scaler.pkl'
    
    # Carrega o modelo e o scaler
    modelo, scaler = Model.carrega_modelo(model_path, scaler_path)
    
    # Simula uma entrada de paciente
    X_input = np.array([63, 1, 145, 233, 1, 2.3])  # Exemplo de entrada
    
    # Faz a predição
    predicao = Model.preditor(modelo, scaler, X_input)
    
    assert predicao is not None, "A predição não deve ser None"
    assert predicao[0] in ['Absence', 'Presence'], "A predição deve ser 'Absence' ou 'Presence'"

# Teste da Avaliação do Modelo
def test_avaliacao_modelo():
    # Gerar um dataset simulado para teste
    X, y = make_classification(n_samples=100, n_features=5, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Treina um modelo simples para fins de teste
    model = KNeighborsClassifier()
    model.fit(X_train, y_train)
    
    # Avaliar o modelo
    acc = Avaliador.avaliar(model, X_test, y_test)
    
    assert 0 <= acc <= 1, "A acurácia deve estar entre 0 e 1"
