# CyberScape Navigator

**Project Description:** An interactive platform for modeling IT environments as knowledge graphs, simulating multi-step cyberattacks (based on MITRE ATT&CK), dynamically visualizing their progression, predicting attacker's next likely steps using Machine Learning, and allowing user-driven defensive countermeasures with real-time impact visualization.

## Key Features

*   **Knowledge Graph Representation:** Model complex IT environments (assets, vulnerabilities, connections, services) using a graph database (e.g., Neo4j).
*   **Attack Simulation Engine:** Simulate multi-stage cyberattack scenarios based on the MITRE ATT&CK framework.
*   **Real-time Interactive Visualization:** Dynamically display the IT environment, attack paths, and asset states using web technologies (e.g., React/Vue + D3.js/Cytoscape.js).
*   **Predictive ML Model:** Employ Machine Learning (e.g., GNN, RNN/LSTM) to predict an attacker's next likely moves.
*   **Interactive Defense:** Allow users to apply defensive countermeasures and see their immediate impact on the simulation.
*   **Dynamic Risk Heatmap:** Visualize vulnerability hotspots and overall risk levels across the environment.

## Technology Stack (Planned)

*   **Backend:** Python, FastAPI (or Flask)
*   **Machine Learning:** PyTorch, TensorFlow (CPU-focused for this project), Scikit-learn
*   **Graph Database:** Neo4j (or alternatives like ArangoDB, NebulaGraph if preferred)
*   **Frontend:** JavaScript/TypeScript, React or Vue.js
*   **Visualization Libraries:** D3.js, Cytoscape.js, or similar
*   **Development Environment:** Fedora 42, VS Code, Python 3.12 (in `cyber-env-py312` virtual environment)
*   **Version Control:** Git & GitHub

## Project Roadmap

This roadmap outlines the planned phases and key tasks for the development of CyberScape Navigator.

### Milestone 0: Project Setup & Initial Commit (COMPLETED)

*   **Tasks:**
    *   GitHub repository created (`UtmostMaker/CyberScape-Navigator`).
    *   Initial project directory structure established.
    *   Python 3.12 virtual environment (`cyber-env-py312`) set up.
    *   `requirements.txt` created with core dependencies.
    *   Basic `README.md` (this file!) and `.gitignore` initialized.
*   **Status:** Done.

### Milestone 1: Environment Modeling & Data Foundation (Weeks 1-4)

*   **Goal:** Establish the data model for the IT environment and integrate foundational datasets.
*   **Tasks:**
    *   Define a detailed schema for the IT environment knowledge graph.
    *   Develop Python scripts (`src/core/graph_builder.py`) to generate/import synthetic IT environment data.
    *   Download, parse, and structure MITRE ATT&CK framework data.
    *   Set up and configure a local Neo4j instance.
    *   Implement scripts to populate Neo4j with environment data and MITRE ATT&CK mappings.
*   **Deliverables:**
    *   Populated Neo4j database.
    *   Python scripts for graph generation and data ingestion.
    *   Graph schema documentation.

### Milestone 2: Core Attack Simulation Engine (Weeks 5-8)

*   **Goal:** Develop backend logic to simulate attack progression.
*   **Tasks:**
    *   Design core logic for simulating multi-step attack paths (MITRE ATT&CK based).
    *   Implement the simulation engine (`src/core/simulation_engine.py`).
    *   Develop initial API endpoints (`src/api/endpoints/simulation.py`) for simulation control.
*   **Deliverables:**
    *   Functional backend simulation engine.
    *   API endpoints for simulations.
    *   Simulation event logging.

### Milestone 3: Visualization Layer - Frontend Implementation (Weeks 9-14)

*   **Goal:** Create an interactive web interface for visualization.
*   **Tasks:**
    *   Set up frontend project (`frontend/`).
    *   Integrate a graph visualization library (e.g., Cytoscape.js).
    *   Develop components for graph display and simulation control.
    *   Implement API communication between frontend and backend.
*   **Deliverables:**
    *   Interactive web application displaying the knowledge graph and attack progression.
    *   UI for simulation control.

### Milestone 4: Predictive Analytics - Attacker's Next Step (Weeks 15-18)

*   **Goal:** Integrate an ML model to predict attacker's next actions.
*   **Tasks:**
    *   Research and select suitable ML models (GNN, RNN/LSTM).
    *   Prepare training data from simulations or public datasets.
    *   Develop, train, and evaluate the ML model (`src/ml/`).
    *   Integrate the trained model into the backend and API.
    *   Visualize predictions on the frontend.
*   **Deliverables:**
    *   Trained ML model.
    *   Integration of ML predictions into simulation and visualization.
    *   Jupyter notebooks for ML development (`notebooks/`).

### Milestone 5: Defensive Interactions & Enhancements (Weeks 19-22)

*   **Goal:** Allow user-driven defensive actions and enhance analytical views.
*   **Tasks:**
    *   Define defensive countermeasures.
    *   Implement logic for applying and reflecting countermeasures in the simulation.
    *   Develop frontend UI for applying defenses.
    *   Visualize countermeasure impact.
    *   Implement a dynamic risk/vulnerability heatmap.
*   **Deliverables:**
    *   Interactive defensive functionality.
    *   Visualization of countermeasure effectiveness.
    *   Dynamic risk heatmap.

### Milestone 6: Testing, Documentation, and Finalization (Weeks 23-24)

*   **Goal:** Ensure a robust, well-documented, and presentable final project.
*   **Tasks:**
    *   Conduct comprehensive testing (unit, integration, end-to-end).
    *   Refine UI/UX.
    *   Write comprehensive project documentation (README, code comments, `docs/`).
    *   Prepare final demonstration.
    *   (Optional) Create `Dockerfile`.
*   **Deliverables:**
    *   Stable, well-tested application.
    *   Complete project documentation.
    *   Project demo.

## Setup and Installation

(Instructions to be added once the initial setup is more concrete)

1.  Clone the repository:
    ```
    git clone https://github.com/UtmostMaker/CyberScape-Navigator.git
    cd CyberScape-Navigator
    ```
2.  Create and activate the Python virtual environment (e.g., using Python 3.12):
    ```
    python3.12 -m venv cyber-env-py312
    source cyber-env-py312/bin/activate
    ```
3.  Install dependencies:
    ```
    pip install -r requirements.txt
    # Specific instructions for PyTorch CPU if needed:
    # pip install torch --index-url https://download.pytorch.org/whl/cpu
    ```
4.  Set up Neo4j (Instructions TBD).
5.  Run the application (Instructions TBD).

## Usage

(Instructions to be added)

## Contributing

(Guidelines for contributing to be added if applicable)

## License

(To be decided - e.g., MIT License)

