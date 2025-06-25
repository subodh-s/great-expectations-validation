import great_expectations as gx
from great_expectations.checkpoint import (
    SlackNotificationAction
)

context = gx.get_context()
data_source = context.data_sources.add_pandas_filesystem(
    name="csvnparquet",
    base_directory="./bulk_csv"
)

data_asset_csv = data_source.add_csv_asset(name="csv_asset", glob_directive="*.csv")
data_asset_parquet = data_source.add_parquet_asset(name="parquet_asset", glob_directive="*.parquet")

batch_definition = data_asset_parquet.add_batch_definition("parquet_batch")
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


# Create a list of Actions for the Checkpoint to perform
action_list = [
    # This Action sends a Slack Notification if an Expectation fails.
    SlackNotificationAction(
        name="send_slack_notification_on_failed_expectations",
        slack_token="${validation_notification_slack_webhook}",
        slack_channel="${validation_notification_slack_channel}",
        notify_on="failure",
        show_failed_expectations=True,
    )]

# Create the Checkpoint
checkpoint_name = "my_checkpoint"
checkpoint = gx.Checkpoint(
    name=checkpoint_name,
    validation_definition_names=[
        "my_validation_definition_parquet",
        "csv_validation"
    ],
    actions=action_list,
    result_format={"result_format": "COMPLETE"},
)


# Save the Checkpoint to the Data Context
context.checkpoints.add(checkpoint)
results = checkpoint.run()
print(results)