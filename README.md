[![Python application test with Github Actions](https://github.com/sumanbgl/shell-de-azure-devops/actions/workflows/pythonapp.yml/badge.svg?branch=master&event=push)](https://github.com/sumanbgl/shell-de-azure-devops/actions/workflows/pythonapp.yml)

# Overview

This project involves setting up a Continuous Delivery pipeline for a python based machine learning application built
using Flask framework. The application is deployed to Azure App Service using the Azure Devops pipeline.
A github repo is bootstrapped with a basic project content with a Makefile, requirements.txt, python and tests for it.
Later Continuous Integration for this code was enabled and tested using GitHub Actions. Finally using Azure Devops pipeline
on a self-hosted agent Continuous Delivery was set up to automate deployment of the application to the Azure Web App.

## Project Plan
<TODO: Project Plan

* A link to a Trello board for the project
* A link to a spreadsheet that includes the original and final project plan>

## Instructions

<TODO:  
* Architectural Diagram (Shows how key parts of the system work)>

<TODO:  Instructions for running the Python project.  How could a user with no context run this project without asking you for any help.  Include screenshots with explicit steps to create that work. Be sure to at least include the following screenshots:

* Project running on Azure App Service

* Project cloned into Azure Cloud Shell

* Passing tests that are displayed after running the `make all` command from the `Makefile`

* Output of a test run

* Successful deploy of the project in Azure Pipelines.  [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).

* Running Azure App Service from Azure Pipelines automatic deployment

* Successful prediction from deployed flask app in Azure Cloud Shell.  [Use this file as a template for the deployed prediction](https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/blob/master/C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn/make_predict_azure_app.sh).
The output should look similar to this:

```bash
udacity@Azure:~$ ./make_predict_azure_app.sh
Port: 443
{"prediction":[20.35373177134412]}
```

* Output of streamed log files from deployed application

> 

## Enhancements

<TODO: A short description of how to improve the project in the future>

## Demo 

<TODO: Add link Screencast on YouTube>



