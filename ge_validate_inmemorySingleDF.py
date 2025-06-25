# This code is used run expectation suite / validations against a single INMEMORY csv/parquet file
# using Pandas

import great_expectations as gx
import pandas

context = gx.get_context(mode="ephemeral")

# Creating Data Source
data_source = context.data_sources.add_pandas(name="my_data_source")

#Creating Data Asset
data_asset = data_source.add_dataframe_asset(name="my_dataframe_data_asset")

#Creating batch definition
batch_definition = data_asset.add_batch_definition_whole_dataframe("my_batch_definition")

csv_path = "./csv/test.csv"
dataframe = pandas.read_csv(csv_path)
batch_parameters = {"dataframe": dataframe}
batch = batch_definition.get_batch(batch_parameters=batch_parameters)


# Create an Expectation Suite
suite = gx.ExpectationSuite(name="my_expectation_suite")
context.suites.add(suite)

# Define the Expectations
suite.add_expectation(gx.expectations.ExpectColumnValuesToNotBeNull(column="ID"))
suite.add_expectation(gx.expectations.ExpectColumnValueLengthsToBeBetween(column="Name", min_value=3))
suite.add_expectation(gx.expectations.ExpectColumnValuesToBeOfType(column="Salary", type_="NUMBER"))
suite.add_expectation(gx.expectations.ExpectColumnValuesToNotBeNull(column="DepartmentName"))

# Test the Expectation:
validation_results = batch.validate(suite)

# Print the Validation Results:
print(validation_results)