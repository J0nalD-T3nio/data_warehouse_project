
# <center> 🚀 Data Warehousing Project </center>

##  📦 Phase 1: Establishing Architecture 

### 🛠️ Task
Create the foundational architecture for extracting, cleaning, and storing data in preparation for downstream analytics and transformations.

---

### 🎯 Objectives

#### 1. Data Sources
- **REST API**: 
  - PokemonDB.net
  - *Provides Pokemon data through RESTful endpoints*
  - **[POKEDEX](https://pokemondb.net/pokedex/all)**
- **File System**:
  - Static **CSV files** *for fixed reference data* from **[Onyx Data](https://onyxdata.co.uk/data-dna-dataset-challenge/)**
  - **Generated JSON files** using the Python `Faker` library *for synthetic testing data*

#### 2. Data Ingestion
- **dlt (Data Load Tool)**:
  - Extract data from the API and file system
  - Maintain extraction logs and versioning
- **Apache Spark (PySpark)**:
  - Perform initial data cleaning and simple transformations 
  - Handle data type correction, null values, and basic formatting
  - Efficiently process data with distributed computing capabilities

#### 3. Operational Data Store (ODS)
- Store cleaned and structured datasets in **Parquet** file format
  - *Columnar storage for efficient querying*
  - *Compression to minimize storage requirements*
- Serve as a lightweight, query-efficient interim storage layer before warehousing
  - *Temporary staging area for validated data*

#### 4. Data Warehouse
- Load **Parquet** files into **Apache Hive** tables for structured storage and analytical querying
  - *Partitioned tables for optimized performance*
  - *Metadata management for data discovery*
- Manage schema and table definitions in Hive for better query performance
  - *Consistent naming conventions*
  - *Appropriate data typing*

#### 5. Workflow Orchestration
- **Apache Airflow**:
  - Orchestrate the entire data pipeline — extraction, cleaning, storage, and loading processes
  - Use **LocalExecutor** for Phase 1 to keep orchestration simple and local during initial development
  - *DAG-based workflow management*
  - *Robust error handling and notifications*

---

### ⚙️ Notes
- **Interfaces**: Apache Spark will be used to connect and load processed data into Hive tables.
- **Best Practices**: Data schemas will be minimally defined during this phase to maintain flexibility.
- **Goal**: Establish a reliable, modular pipeline that can easily be expanded in subsequent phases.

---


### 📊 Pipeline Flow


---
### 📅 Timeline Expectations

- **Week 1-2**: Data source connection and extraction setup
- **Week 3-4**: Data cleaning and transformation implementation
- **Week 5-6**: ODS and warehouse configuration
- **Week 7-8**: Airflow orchestration and end-to-end testing
---
> **NOTE 1**: This architecture prioritizes modularity and extensibility to accommodate 
future analytics requirements and data source additions as well as maximizes learning.

> **NOTE 2**: The provided timeline expectaions is for myself for other users you could be
more lenient on yourself, the reasoning for tight deadlines is for me to develop a habit of
coding.

**<center> Always remember to have fun and do it at your own phase (੭˃ᴗ˂)੭**
