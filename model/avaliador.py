from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
from model.modelo import Model

class Avaliador:
    @staticmethod
    def avaliar(model, X_test, Y_test):
        """ Faz uma predição e avalia o modelo. Poderia parametrizar o tipo de
        avaliação, entre outros.
        """
        # Passando o X_test como o segundo argumento
        predicoes = model.predict(X_test)
        
        return accuracy_score(Y_test, predicoes)