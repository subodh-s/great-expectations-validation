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
