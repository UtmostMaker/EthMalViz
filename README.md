# EthMalViz

EthMalViz is an interactive platform for detecting and visualizing malicious Ethereum transactions in a 3D knowledge graph. It leverages deep learning (NLP + LSTM/CNN) to classify on-chain data, Neo4j to store and query transaction relationships, FastAPI as the backend, and React + Three.js for dynamic front-end visualization.

## Key Features

* Continuous ingestion of Ethereum transactions via Etherscan/Infura API  
* NLP + LSTM/CNN model for phishing, scam, and malware transaction detection  
* Neo4j knowledge graph of `Address`, `Transaction`, and `Alert` entities  
* FastAPI endpoints for `/transactions`, `/predict`, and `/graph`  
* React + Three.js front-end: 3D graph rendering with animated, color-coded suspicious flows  
* Docker support for one-command deployment

## Technology Stack

* **Language & ML**: Python 3.12, PyTorch (CPU), TensorFlow-CPU, Scikit-learn  
* **Database**: Neo4j  
* **Backend**: FastAPI, Uvicorn  
* **Frontend**: React, Three.js  
* **Dev Environment**: Fedora 42, VS Code, `venv` (`cyber-env-py312`)  
* **Version Control**: Git & GitHub

## Project Roadmap

### Milestone 0: Project Initialization (Completed)

* Created GitHub repo `UtmostMaker/EthMalViz`  
* Set up `cyber-env-py312` Python 3.12 virtual environment  
* Added `requirements.txt`, `.gitignore`, initial `README.md`

### Milestone 1: Data Collection & Labeling (Weeks 1–4)

1. Define target malicious transaction categories (phishing, scam, mixer use).  
2. Fetch labeled addresses from Etherscam DB, Ethereum scam lists.  
3. Use Etherscan/Infura API to download raw transactions for these addresses.  
4. Store raw JSON in `data/raw/`; build cleaned CSV/Parquet in `data/processed/`.  
5. Document data schema and labeling process in `notebooks/01_data_collection.ipynb`.

### Milestone 2: Model Development & Training (Weeks 5–8)

1. Extract text/binary features from transaction `input_data` (OP_RETURN, calldata).  
2. Build embeddings (Word2Vec or DistilBERT) and sequence inputs.  
3. Implement a 1D CNN + LSTM classifier in `src/ml/models.py`.  
4. Train and evaluate on CPU; target F1 score ≥ 0.85.  
5. Save best model checkpoint to `models/`; document in `notebooks/03_model_training.ipynb`.

### Milestone 3: Knowledge Graph Construction (Weeks 9–12)

1. Design Neo4j schema: nodes `Address`, `Transaction`, `Alert`; relationships `SENT`, `RECEIVED`, `FLAGGED_AS`.  
2. Write `src/graph/builder.py` to ingest processed data and model predictions into Neo4j.  
3. Create common query templates in `src/graph/queries.py`.  
4. Validate graph connectivity and indexes.

### Milestone 4: Backend & API (Weeks 13–16)

1. Scaffold FastAPI app in `src/api/main.py`.  
2. Implement `/transactions` (list recent), `/predict` (classify one tx), `/graph` (return graph JSON) endpoints.  
3. Add Pydantic schemas in `src/api/schemas.py`.  
4. Write unit tests for each endpoint in `tests/unit/`.  
5. Document API usage in `docs/api_reference.md`.

### Milestone 5: Front-End Visualization (Weeks 17–20)

1. Initialize React project in `frontend/`.  
2. Integrate Three.js and load graph data via `/graph`.  
3. Render nodes/edges in 3D; animate transaction flows as moving particles.  
4. Color-code nodes/edges by suspicion score; add UI controls (filter by score, time window).  
5. Test on sample data; record demo GIF.

### Milestone 6: Testing, Documentation & Deployment (Weeks 21–24)

1. Complete integration tests and end-to-end tests.  
2. Finalize user and developer documentation in `docs/`.  
3. Add a `Dockerfile` and `docker-compose.yml` for full-stack deployment.  
4. Polish README with screenshots and badges.  
5. Produce a demo video and share on your portfolio.

## Setup & Installation

1. Clone the repo and enter it:  

```
git clone https://github.com/UtmostMaker/EthMalViz.git
cd EthMalViz
```

2. Create & activate the venv:  

```
python3.12 -m venv cyber-env-py312
source cyber-env-py312/bin/activate
```
3. Install Python dependencies:  

```
pip install -r requirements.txt
```

4. Start Neo4j (desktop or Docker).  
5. Launch the backend:  

```
uvicorn src.api.main:app --reload
```
6. Start the frontend:  

```
cd frontend
npm install
npm start
```

```
EthMalViz/
├── .gitignore
├── data/
│   ├── raw/
│   ├── processed/
│   └── external/
├── notebooks/
│   ├── 01_data_collection.ipynb
│   ├── 02_data_preparation.ipynb
│   └── 03_model_training.ipynb
├── src/
│   ├── __init__.py
│   ├── data/
│   │   ├── collectors.py
│   │   └── preprocess.py
│   ├── ml/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── train.py
│   │   └── predict.py
│   ├── graph/
│   │   ├── __init__.py
│   │   ├── builder.py
│   │   └── queries.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   └── endpoints/
│   │       ├── transactions.py
│   │       └── graph.py
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
├── frontend/
│   ├── public/
│   └── src/
│       ├── App.js
│       └── components/
├── models/
├── requirements.txt
├── README.md
├── LICENSE
└── Dockerfile
```
