#### Azure Functions App ####

Aim: 
Fetch weather information from Open Web APIs and Store it in Cloud storage.
It mimics the behaviour of an application recording weather readings.

Code file Path: 
rep-weather-information/az-func-apitoblob/function_app.py

Connection to BLOB Container:
System managed identity connection

Useful Links:
https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-python?pivots=python-mode-decorators


#### Raw Data to Bronze layer ####

Aim:
Replicate Data from application storage to Bronze layer of Medallion Architecture.

Functionality: 
Databricks Auto-loader

Notebook:
rep-weather-information/db-workspace/Files/bronze-autoloader.ipynb

Useful Links: 
https://learn.microsoft.com/en-us/azure/databricks/ingestion/cloud-object-storage/auto-loader/