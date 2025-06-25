# This code is used run expectation suite against multiple local csv & parquet files stored in a folder
import great_expectations as gx


context = gx.get_context()
data_source = context.data_sources.add_pandas_filesystem(
    name="csvnparquet",
    base_directory="./bulk_csv"
)

#Creating batch definition for parquet files
data_asset_parquet = data_source.add_parquet_asset(name="parquet_asset", glob_directive="*.parquet")
batch_definition = data_asset_parquet.add_batch_definition("parquet_batch")

#Creating batch definition for parquet files
data_asset_csv = data_source.add_csv_asset(name="csv_asset", glob_directive="*.csv")
batch_definition_csv = data_asset_csv.add_batch_definition("csv_batch")

suite = gx.ExpectationSuite(name="my_expectation_suite")
context.suites.add(suite)

suite.add_expectation(gx.expectations.ExpectColumnValuesToNotBeNull(column="ID"))
suite.add_expectation(gx.expectations.ExpectColumnValueLengthsToBeBetween(column="Name", min_value=3))
suite.add_expectation(gx.expectations.ExpectColumnValuesToBeOfType(column="Salary", type_="NUMBER"))
suite.add_expectation(gx.expectations.ExpectColumnValuesToNotBeNull(column="DepartmentName"))

validation_definition_parquet = gx.ValidationDefinition(
    data=batch_definition,
    suite=suite,
    name="my_validation_definition_parquet"
)

validation_definition_csv = gx.ValidationDefinition(
    data=batch_definition_csv,
    suite=suite,
    name="csv_validation"
)

context.validation_definitions.add(validation_definition_parquet)
context.validation_definitions.add(validation_definition_csv)

validation_results_parquet = validation_definition_parquet.run()
validation_results_csv = validation_definition_csv.run()

print(validation_results_parquet)
print(validation_results_csv)
