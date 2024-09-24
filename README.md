
# Heart Disease Prediction API

Este projeto é uma API desenvolvida para prever a presença de doenças cardíacas com base nos dados fornecidos por pacientes. A aplicação usa um modelo de machine learning treinado com um [dataset de doenças cardíacas](https://www.kaggle.com/datasets/rishidamarla/heart-disease-prediction?resource=download) e oferece endpoints para adicionar, visualizar, remover pacientes e realizar predições.

### Sobre o Dataset

- **Contexto**: A principal causa de morte no mundo desenvolvido é a doença cardíaca. Portanto, há a necessidade de esforços para prevenir os riscos de ataque cardíaco ou derrame.
  
- **Conteúdo**: Este dataset permite prever quais pacientes têm maior probabilidade de desenvolver doenças cardíacas no futuro próximo, usando os recursos fornecidos.

- **Reconhecimento**: Este dataset foi originado do Repositório de Aprendizado de Máquina da Universidade da Califórnia Irvine, disponível em [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Heart+Disease).


## Funcionalidades

- **Adicionar pacientes**: Registro de novos pacientes e predição automática de doenças cardíacas.
- **Listar pacientes**: Visualização de todos os pacientes cadastrados no banco de dados.
- **Buscar por nome**: Permite buscar um paciente pelo nome.
- **Remover pacientes**: Exclui pacientes cadastrados usando seu nome.
- **Predição**: Utiliza um modelo de machine learning para prever a presença ou ausência de doenças cardíacas.
- **Avaliação de Desempenho**: Avalia a acurácia do modelo de machine learning.
- **Testes automatizados**: Valida a funcionalidade do sistema e o desempenho do modelo.

## Tecnologias Utilizadas

- **Flask**: Framework web para construção da API.
- **SQLAlchemy**: ORM para interagir com o banco de dados SQLite.
- **Scikit-learn**: Biblioteca para aprendizado de máquina utilizada no carregamento e predição do modelo.
- **Pandas**: Utilizada para manipulação e análise dos dados dos pacientes.
- **NumPy**: Suporte à manipulação de arrays numéricos para entrada de dados.
- **Joblib**: Usada para carregar o modelo de machine learning serializado.
- **Pydantic**: Validação de dados e definição de esquemas de API.
- **Flask-CORS**: Suporte a CORS (Cross-Origin Resource Sharing) na API.

## Instalação e Configuração

### Pré-requisitos

- Python 3.8 ou superior.
- pip (gerenciador de pacotes do Python).

### Passos para Instalação

1. Clone o repositório:

git clone https://github.com/usuario/seu-repositorio.git

2. Acesse o diretório do projeto:

cd seu-repositorio

3. Instale as dependências listadas no `requirements.txt`:

pip install -r requirements.txt

4. Inicie a aplicação:

python app.py

5. A API estará disponível em `http://127.0.0.1:5000`.

## Como Usar

### Adicionar um novo paciente

Envie os dados do paciente por meio de um formulário (`form-data`):

| Campo            | Tipo   | Descrição                               |
|------------------|--------|-----------------------------------------|
| name             | string | Nome do paciente                        |
| age              | int    | Idade do paciente                       |
| sex              | bool   | Sexo (T == masculino, F == feminino)    |
| BP               | int    | Pressão arterial                        |
| cholesterol      | int    | Nível de colesterol                     |
| chest_pain_type  | int    | Tipo de dor no peito (1 a 4)            |
| ST_depression    | float  | Depressão do segmento ST                |

Exemplo de envio:
```bash
curl -X POST http://127.0.0.1:5000/paciente -F "name=João" -F "age=45" -F "sex=true" -F "BP=140" -F "cholesterol=250" -F "chest_pain_type=3" -F "ST_depression=2.3"
```
**Resposta** (em JSON):

```json
{
  "id": 1,
  "name": "João",
  "age": 45,
  "sex": true,
  "BP": 140,
  "cholesterol": 250,
  "chest_pain_type": 3,
  "ST_depression": 2.3,
  "heart_disease": "Presença"
}
```

### Buscar todos os pacientes

**Endpoint**: `GET /pacientes`

**Resposta**:

```json
[
  {
    "id": 1,
    "name": "João",
    "age": 45,
    "sex": true,
    "BP": 140,
    "cholesterol": 250,
    "chest_pain_type": 3,
    "ST_depression": 2.3,
    "heart_disease": "Presença"
  }
]
```

### Deletar um paciente

**Endpoint**: `DELETE /paciente`

Envie o nome do paciente por meio de um formulário:

```bash
curl -X DELETE http://127.0.0.1:5000/paciente -F "name=João"
```

**Resposta** (em JSON):

```json
{
  "message": "Paciente João removido com sucesso!"
}
```

## Estrutura do Projeto

```bash
.
├── machineLearning/
│   ├── model/                 
│   │   └── knn_model.pkl       
│   ├── scaler/
│   │   └── scaler.pkl          
├── model/                     
│   ├── __init__.py
│   ├── base.py                
│   ├── paciente.py            
│   ├── modelo.py             
│   ├── avaliador.py           
│   ├── preProcessador.py      
│   └── carregador.py          
├── schemas/                   
│   ├── __init__.py
│   ├── pacienteSchema.py      
│   └── erroSchema.py    
├── app.py      
├── test_app.py                
├── requirements.txt           
├── README.md                  
└── log/                       
```

## Testes

Para rodar os testes automatizados, utilize o comando:

pytest

Os testes cobrem:

- Carregamento dos dados.
- Predição do modelo.
- Avaliação do modelo.