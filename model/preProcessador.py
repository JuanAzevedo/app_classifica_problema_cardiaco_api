from sklearn.model_selection import train_test_split
import numpy as np

class PreProcessador:

    @staticmethod
    def preparar_form(form):
        """ Prepara os dados recebidos do front para serem usados no modelo.
            Assume que o form contém os atributos necessários.
        """
        X_input = np.array([form.age,
                            form.sex,
                            form.BP,
                            form.cholesterol,
                            form.chest_pain_type,
                            form.ST_depression
        ])
        # Reshape para o modelo entender que estamos passando uma amostra
        X_input = X_input.reshape(1, -1)
        return X_input