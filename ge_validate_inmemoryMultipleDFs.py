# This code is used run expectation suite against multiple local csv / parquet files via dataframe

import great_expectations as gx
import pandas
import os



context = gx.get_context(mode="ephemeral")

data_source_name = "my_data_source"


# Add the Data Source to the Data Context
data_source = context.data_sources.add_pandas(name=data_source_name)

# Define the Data Asset name
# A dataframe Data Asset is used to group your Validation Results. For instance, if you have a data pipeline with three stages and you wanted the Validation Results for each stage to be grouped together, you would create a Data Asset with a unique name representing each stage.
data_asset_name = "my_dataframe_data_asset"

# Add a Data Asset to the Data Source
data_asset = data_source.add_dataframe_asset(name=data_asset_name)

# Define the Batch Definition name
batch_definition_name = "my_batch_definition"

# Add a Batch Definition to the Data Asset
batch_definition = data_asset.add_batch_definition_whole_dataframe(
    batch_definition_name
)

# List all CSV files in the folder
csv_path = "./bulk_csv"

csv_files = [f for f in os.listdir(csv_path) if f.endswith(".csv")]

# Read and combine all CSVs
all_dfs = []
for file in csv_files:
    file_path = os.path.join(csv_path, file)
    df = pandas.read_csv(file_path)
    all_dfs.append(df)

# Concatenate into one DataFrame
combined_df = pandas.concat(all_dfs, ignore_index=True)


batch_parameters = {"dataframe": combined_df}


# Get the dataframe as a Batch
batch = batch_definition.get_batch(batch_parameters=batch_parameters)

# Create an Expectation Suite
suite_name = "my_expectation_suite"
suite = gx.ExpectationSuite(name=suite_name)

# Add the Expectation Suite to the Data Context
suite = context.suites.add(suite)

# Define the Expectation to test:
expectation_1 = gx.expectations.ExpectColumnValuesToNotBeNull(
    column="ID"
)

# Define the Expectation to test:
expectation_2 = gx.expectations.ExpectColumnValueLengthsToBeBetween(
    column="Name",
    min_value=3
)


# Add the previously created Expectation to the Expectation Suite
suite.add_expectation(expectation_1)
suite.add_expectation(expectation_2)

# Test the Expectation
validation_results = batch.validate(suite)
print(validation_results)
