Feature: Parse a CSV file

    Scenario: Run a CSV file test
        Given we have multiple CSV files found in a working directory
        When the user provides an input and select a CSV file to work with
        Then the CSV file is parsed and the application ask for the column to order in string descending order
