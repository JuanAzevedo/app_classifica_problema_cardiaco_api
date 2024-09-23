from pydantic import BaseModel
from typing import Optional, List
from model.paciente import Paciente
import json
import numpy as np

class PacienteSchema(BaseModel):
    """Define como um novo paciente a ser inserido deve ser representado
    """

    name: str = "João"
    age: int = 40
    sex: bool = True
    BP: int = 130
    cholesterol: int = 260
    chest_pain_type: int = 2
    ST_depression: float = 2.4


class PacienteViewSchema(BaseModel):
    """Define como um paciente será retornado
    """
    id: int = 1
    name: str = "João"
    age: int = 40
    sex: bool = True
    BP: int = 130
    cholesterol: int = 260
    chest_pain_type: int = 2
    ST_depression: float = 2.4
    heart_disease: str = "Presença"  # Presença ou Ausência
    
class PacienteBuscaSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca.
    Ela será feita com base no nome do paciente.
    """
    name: str = "João"

class ListaPacientesSchema(BaseModel):
    """Define como uma lista de pacientes será representada
    """
    pacientes: List[PacienteSchema]

    
class PacienteDelSchema(BaseModel):
    """Define como um paciente para deleção será representado
    """
    name: str = "João"
    
# Apresenta apenas os dados de um paciente    
def apresenta_paciente(paciente):
    """Retorna uma representação do paciente."""
    return {
        "id": paciente.id,
        "name": paciente.name,
        "age": paciente.age,
        "sex": paciente.sex,
        "BP": paciente.BP,
        "cholesterol": paciente.cholesterol,
        "chest_pain_type": paciente.chest_pain_type,
        "ST_depression": paciente.ST_depression,
        "heart_disease": paciente.heart_disease # Presença ou Ausência
    }
    
# Apresenta uma lista de pacientes
def apresenta_pacientes(pacientes: List[Paciente]):
    """ Retorna uma representação do paciente seguindo o schema definido em
        PacienteViewSchema, adaptado para os atributos de diagnóstico de doença cardíaca.
    """
    result = []
    for paciente in pacientes:
        result.append({
            "id": paciente.id,
            "name": paciente.name,
            "age": paciente.age,
            "sex": paciente.sex,
            "BP": paciente.BP,
            "cholesterol": paciente.cholesterol,
            "chest_pain_type": paciente.chest_pain_type,
            "ST_depression": paciente.ST_depression,
            "heart_disease": paciente.heart_disease # Presença ou Ausência
        })

    return {"pacientes": result}
