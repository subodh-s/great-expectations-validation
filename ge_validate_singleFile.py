# This code is used run expectation suite / validations against a single local csv/parquet file

import great_expectations as gx
context = gx.get_context()

# Use the `pandas_default` Data Source to read the file:
sample_batch = context.data_sources.pandas_default.read_csv("./csv/test.csv")

# Create an Expectation Suite
suite = gx.ExpectationSuite(name="my_expectation_suite")
context.suites.add(suite)

# Define the Expectations
suite.add_expectation(gx.expectations.ExpectColumnValuesToNotBeNull(column="ID"))
suite.add_expectation(gx.expectations.ExpectColumnValueLengthsToBeBetween(column="Name", min_value=3))
suite.add_expectation(gx.expectations.ExpectColumnValuesToBeOfType(column="Salary", type_="NUMBER"))
suite.add_expectation(gx.expectations.ExpectColumnValuesToNotBeNull(column="DepartmentName"))

# Test the Expectation:
validation_results = sample_batch.validate(suite)

# Print the Validation Results:
print(validation_results)