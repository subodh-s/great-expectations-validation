# This code is used run expectation suite against multiple csv / parquet files stored in a directory

import great_expectations as gx



context = gx.get_context()
source_folder = "./bulk_csv"

data_source_name = "my_filesystem_data_source"
data_asset_name = "my_directory_data_asset"
data_directory = "./bulk_csv"


data_source = context.data_sources.add_pandas_filesystem(
    name=data_source_name, base_directory=source_folder
)


# Add the Data Asset to the Data Source:
file_csv_asset = data_source.add_csv_asset(name=data_asset_name)


file_data_asset = context.data_sources.get(data_source_name).get_asset(data_asset_name)

batch_definition_name = "test-batch"
batch_definition = file_csv_asset.add_batch_definition(
    name=batch_definition_name
)


batch = batch_definition.get_batch()
#print(batch.head(100))

# Create an Expectation Suite
suite_name = "my_expectation_suite"
suite = gx.ExpectationSuite(name=suite_name)

# Add the Expectation Suite to the Data Context
suite = context.suites.add(suite)

# Define the Expectation to ensure the column "ID" should not contain NULL:
expectation_1 = gx.expectations.ExpectColumnValuesToNotBeNull(
    column="ID"
)

# Define the Expectation to ensure the column "Name" should contain more than 3 chars
expectation_2 = gx.expectations.ExpectColumnValueLengthsToBeBetween(
    column="Name",
    min_value=3
)

# Define the Expectation to ensure the column "Number" should be a Number datatype
expectation_3 = gx.expectations.ExpectColumnValuesToBeOfType(
    column="Salary",
    type_="NUMBER"
)

# Define the Expectation to ensure the column "DepartmentName" should not contain NULL:
expectation_4 = gx.expectations.ExpectColumnValuesToNotBeNull(
    column="DepartmentName"
)


# Test the Expectation:
validation_results = batch.validate(suite)

# Evaluate the Validation Results:
print(validation_results)