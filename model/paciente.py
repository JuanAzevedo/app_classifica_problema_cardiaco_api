from sqlalchemy import Column, String, Integer, DateTime, Float, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union
from  model import Base


class Paciente(Base):
    __tablename__ = 'pacientes'
    
    id = Column(Integer, primary_key=True)
    name = Column("Name", String(60), nullable=False)
    age = Column("Age", Integer, nullable=False)
    sex = Column("Sex", Boolean, nullable=False)
    BP = Column("BP", Integer, nullable=False)
    cholesterol = Column("Cholesterol", Integer, nullable=False)
    chest_pain_type = Column("chest_pain_type", Integer, nullable=False)  
    ST_depression = Column("ST_depression", Float, nullable=False)        
    heart_disease = Column("heart_disease", String, nullable=False)       
    data_insercao = Column(DateTime, default=datetime.now(), nullable=False)

    
    def __init__(self, name: str, age: int, sex: bool, BP: int, 
                 cholesterol: int, chest_pain_type: int, ST_depression: float, 
                 heart_disease: str, data_insercao: Union[datetime, None] = None):
        """
        Cria um Paciente com informações para previsão de doenças cardíacas.

        Argumentos:
            name: nome do paciente
            age: idade do paciente
            sex: sexo (True para masculino, False para feminino)
            BP: pressão arterial
            cholesterol: nível de colesterol
            chest_pain_type: tipo de dor no peito (De 1 a 4)
            ST_depression: depressão do segmento ST
            heart_disease: diagnóstico de doença cardíaca
            data_insercao: data de quando o paciente foi inserido à base
        """
        self.name = name
        self.age = age
        self.sex = sex
        self.BP = BP
        self.cholesterol = cholesterol
        self.chest_pain_type = chest_pain_type
        self.ST_depression = ST_depression
        self.heart_disease = heart_disease

        # Se a data de inserção não for informada, será definida como a data atual
        if data_insercao:
            self.data_insercao = data_insercao
        else:
            self.data_insercao = datetime.now()
