# Technical Test for News UK Devops Engineers

**Prerequisites**: IDE of your choice, Docker, Terraform, local Kubernetes cluster

We want to deploy and check for a successful deployment of our `server.js` app. It needs to be
deployed on the cloud platform of your choice, and must be easily ported to a different platform or tool.

Your job is to dockerize the server and run it locally. Write a script to check if the correct version was deployed. It will always spit out version `0.21.3` but your script should be re-usable. Write the necessary config to deploy the server on the cloud. Run the application on your local Kubernetes cluster.

We have included a `Makefile` to install the dependencies. This is not a test of your Javascript knowledge so you shouldn't need to edit the Javascript file.

## Expected Outcome

You should deliver:

- Docker image
- Kubernetes manifest file(s)
- The necessary Terraform files
- The script (in whatever programming language you choose) to check that the correct version has been deployed.

You should be able to open the application in your browser and verify using the script that we are getting the correct version. You should also include instructions on how we can run your pipeline.
