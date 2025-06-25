# ✅ Great Expectations Validation – CSV & Parquet Quality Checks

This repository provides step-by-step, ready-to-run Python examples demonstrating how to use **[Great Expectations (GX)](https://greatexpectations.io/)** to validate **CSV**, **Parquet**, and in-memory **Pandas DataFrames** before ingestion into a data pipeline.

These scripts illustrate both basic and advanced validation flows, including checkpoints and Slack notifications.

---

## 📁 Repository Structure

```bash
.
├── ge_single_file.py                         # Scenario 1: Validate a single CSV file
├── ge_single_file_expectationsuite.py       # Scenario 2: CSV validation with Expectation Suite
├── ge_ephemeral.py                          # Scenario 3: Validate files using EphemeralContext
├── ge_ephemeral_multifiles.py               # Scenario 4: In-memory Pandas DataFrame validation
├── ge_multifiles.py                         # Scenario 5: Validate both CSV & Parquet files
├── ge_bulk_checkpoint.py                    # Scenario 6: Checkpoint with Slack alerts
├── bulk_csv/                                # Test data folder (.csv and .parquet files)
└── README.md
```

---

## ✅ Prerequisites

- Python 3.8+
- Access to your terminal (Windows/Linux/Mac)

---

## 🛠️ Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/subodh-s/great-expectations-validation.git
cd great-expectations-validation
```

2. **Create and activate a virtual environment**

```bash
python -m venv ge-env
ge-env\Scripts\activate     # For Windows
# OR
source ge-env/bin/activate  # For Mac/Linux
```

3. **Install required libraries**

```bash
pip install -r requirements.txt
```

If no `requirements.txt`, run:

```bash
pip install great_expectations pandas pyarrow fastparquet lxml html5lib
```

---

## 🚀 How to Execute

Each script is independent and demonstrates a real-world validation scenario.

### 🔹 Scenario 1: Validate a Single CSV File

```bash
python ge_single_file.py
```

### 🔹 Scenario 2: CSV Validation with Expectation Suite

```bash
python ge_single_file_expectationsuite.py
```

### 🔹 Scenario 3: Validate CSV Files Using EphemeralContext (No GX folder)

```bash
python ge_ephemeral.py
```

### 🔹 Scenario 4: In-Memory Pandas DataFrame Validation

```bash
python ge_ephemeral_multifiles.py
```

### 🔹 Scenario 5: Validate CSV & Parquet Together

Make sure `bulk_csv/` folder has both `.csv` and `.parquet` files.

```bash
python ge_multifiles.py
```

### 🔹 Scenario 6: Run Checkpoint with Slack Alerts

Configure environment variables first:

```bash
export validation_notification_slack_webhook="https://hooks.slack.com/services/..."
export validation_notification_slack_channel="#your-channel"
```

Then run:

```bash
python ge_bulk_checkpoint.py
```

---

## 📚 Learn More

- 🔍 [All Available Expectations](https://greatexpectations.io/expectations/)
- 📘 [GX Core Concepts](https://docs.greatexpectations.io/docs/core/concepts/overview/)
- 🖼️ [Architecture Diagram](https://docs.greatexpectations.io/docs/core/introduction/gx_overview)

---

## ✍️ Related Medium Article

Read the detailed walkthrough with visuals and explanations on Medium:  
📖 [Validating CSV and Parquet Files Using Great Expectations Before Ingestion](https://medium.com/@subodh.shetty87)

---

## 🙌 Author

**Subodh Shetty**  
🔗 [GitHub](https://github.com/subodh-s) | [Medium](https://medium.com/@subodh.shetty87)

---

## 🛡️ License

This project is licensed under the MIT License.
