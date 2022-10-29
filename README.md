# Overview

This project involves setting up a Continuous Delivery pipeline for a python based machine learning application built
using Flask framework. The application is deployed to Azure App Service using the Azure Devops pipeline.
A github repo is bootstrapped with a basic project content with a Makefile, requirements.txt, python and tests for it.
Later Continuous Integration for this code was enabled and tested using GitHub Actions. Finally using Azure Devops pipeline
on a self-hosted agent Continuous Delivery was set up to automate deployment of the application to the Azure Web App.
https://github.com/sumanbgl/shell-de-azure-devops.git is the github repo with the code for this project.

## Project Plan

* https://trello.com/b/cgVCU8Uq/azure-devops-for-shell
* https://github.com/sumanbgl/shell-de-azure-devops/blob/master/Project%20Plan.xlsx

## Instructions

* Architectural Diagram 
![architecture diagram](https://github.com/sumanbgl/shell-de-azure-devops/blob/master/screenshots/06_arch_diagram.JPG)

# Instructions for running the Python project.  

* Project running on Azure App Service
  * command to create and run web app
     `az webapp up --name suman-flask-ml-service --resource-group DefaultResourceGroup-CAU --runtime "PYTHON:3.7"`

* Project cloned into Azure Cloud Shell
  * Launch Azure Portal.
  * Activate cloud shell.
  * Clone the project using `git clone https://github.com/sumanbgl/shell-de-azure-devops.git`
  * Change directory to `shell-de-azure-devops/flask-ml-project` using command `cd shell-de-azure-devops/flask-ml-project`

* Passing tests that are displayed after running the `make all` command from the `Makefile`
  * Run `make all` command to verify the code compiles and test run successfully.

* Output of a test run
  * ![test run output](https://github.com/sumanbgl/shell-de-azure-devops/blob/master/screenshots/02_make_all_output.JPG)

* Successful deploy of the project in Azure Pipelines. 
  * Set up the Azure DevOps account
    * Create the Azure DevOps Account
      -Log into the https://portal.azure.com/ using your Azure credentials.
      -Log into the https://dev.azure.com/ in a separate browser tab using the same Azure account. It will prompt you to give a name to your DevOps org and choose a nearby location.
    * Create a new DevOps project in the newly created DevOps org. The project should be public.
    * Set up a Service connection
      - Go to the project settings >> Service connection settings, and ensure you set up a new service connection via Azure Resource Manager and Service principal (Automatic). This step will connect your DevOps account with your Azure account.
  * Create a Pipeline
    * Go back to the DevOps project, select Pipeline and create a new one.
    * Connect
      * Choose the Github repository as the source code location.
    * Select
      * Select the Github repository containing the this code.
    * Configure
      * Choose the Existing Azure Pipelines YAML file option
      * Edit and Review the azure-pipelines-for-self-hosted-agent.yml file
        * Update the agent pool name, service connection name, and the web app name as applicable to you.
    * Run
      * Click on the Run button, provide a commit message and finish creating and running the pipeline. If everything goes well, you will see success status in the agent logs

* Running Azure App Service from Azure Pipelines automatic deployment
  * Edit azure-pipelines-for-self-hosted-agent.yml to add the deploy step that will install and start the Azure App Service.

* Successful prediction from deployed flask app in Azure Cloud Shell. 
  * Edit make_predict_azure_app.sh to include your web appp name. Run `sh make_predict_azure_app.sh`
  * The output should look similar to one shown below:

```bash
udacity@Azure:~$ ./make_predict_azure_app.sh
Port: 443
{"prediction":[20.35373177134412]}
```

* Output of streamed log files from deployed application
  * Execute the command `az webapp log tail --name <web app name>` from azure shell. The output should be similar to one below:
```
2022-10-29T18:08:14  Welcome, you are now connected to log-streaming service.

Starting Log Tail -n 10 of existing logs ----

/home/LogFiles/__lastCheckTime.txt  (https://suman-flask-ml-service.scm.azurewebsites.net/api/vfs/LogFiles/__lastCheckTime.txt)
10/29/2022 18:07:58


/home/LogFiles/kudu/trace/2bce0b9e3397-4bee1d1e-bf09-4409-963f-f7cd40b9f94f.txt  (https://suman-flask-ml-service.scm.azurewebsites.net/api/vfs/LogFiles/kudu/trace/2bce0b9e3397-4bee1d1e-bf09-4409-963f-f7cd40b9f94f.txt)

2022-10-26T12:23:32    Outgoing response, type: response, statusCode: 404, statusText: NotFound

/home/LogFiles/kudu/trace/2bce0b9e3397-bd51c6c0-b136-4652-93b2-cf87cb2c80d3.txt  (https://suman-flask-ml-service.scm.azurewebsites.net/api/vfs/LogFiles/kudu/trace/2bce0b9e3397-bd51c6c0-b136-4652-93b2-cf87cb2c80d3.txt)
2022-10-26T12:23:17  Startup Request, url: /api/deployments/latest, method: GET, type: request, pid: 77,1,6, ScmType: VSTSRM, SCM_DO_BUILD_DURING_DEPLOYMENT: True

/home/LogFiles/kudu/trace/744fb7f819e3-7b8e9331-2635-419e-886c-d2e5e0996f86.txt  (https://suman-flask-ml-service.scm.azurewebsites.net/api/vfs/LogFiles/kudu/trace/744fb7f819e3-7b8e9331-2635-419e-886c-d2e5e0996f86.txt)
....
....
....
2022-10-29T18:14:16.751247145Z [2022-10-29 18:14:16,750] INFO in app: JSON payload: %s json_payload

2022-10-29T18:14:16.756076169Z [2022-10-29 18:14:16,755] INFO in app: inference payload DataFrame: %s inference_payload

2022-10-29T18:14:16.756616572Z [2022-10-29 18:14:16,756] INFO in app: Scaling Payload: %s payload

2022-10-29T18:14:16.795669472Z 172.16.0.1 - - [29/Oct/2022:18:14:16 +0000] "POST /predict HTTP/1.1" 200 36 "-" "curl/7.84.0"
```

> 

## Enhancements

  - Setup a test bed to do the complete integration testing involving all the components of the application.
  - Modify the rule to trigger pipeline run for every pull request created so that feature branch code is validated well
before it is merged to the main stream.

## Demo 
![https://youtu.be/JXshz9fG-cA](Demo)


## Continuous Integration Status Badge
[![Python application test with Github Actions](https://github.com/sumanbgl/shell-de-azure-devops/actions/workflows/pythonapp.yml/badge.svg?branch=master&event=push)](https://github.com/sumanbgl/shell-de-azure-devops/actions/workflows/pythonapp.yml)

