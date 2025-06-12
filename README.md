# mesh-card-schema
A repository for prototyping Mesh Cards as a potential new standard from the Cloud WS.

## JSON Validator

This project validates a `BioData Catalyst` mesh card JSON file against a predefined JSON Schema.

## 📦 Files

- `schema.json` – JSON Schema defining the required structure
- `sample.json` – Sample mesh card JSON
- `validate.py` – Script to validate `sample.json` against `schema.json`

---

## 🧪 Requirements

This project uses:

- Python 3.8+
- `jsonschema` Python package

We recommend using Conda to manage dependencies.

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone git@github.com:ga4gh/mesh-card-schema.git
cd mesh-card-schema
```

### 2. Create Conda Env

```bash
conda create -n mesh-card-schema python=3.10
conda activate mesh-card-schema
```

### 3. Install Deps

```bash
pip install jsonschema
```

### 4. Run Validator

```bash
python validate.py
```
If valid, you’ll see:

  ✅ JSON is valid.

If there are validation errors, the script will print an error message and exit with code 1.
