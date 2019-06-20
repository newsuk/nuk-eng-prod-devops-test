# Technical Test for News UK Devops Engineers

We want to deploy and check for a successful deployment of our `server.py` script. It needs to be
deployed on the cloud platform of your choice, and must be easily ported to a different platform or tool.

Your job is to dockerize the server, write the necessary config to deploy the server and check that
the correct version was deployed.

We have included a `Makefile` to install the dependencies. This is not a test of your Python
knowledge so you shouldn't need to edit the Python script. It will always spit out version `0.21.3`
but your script should be re-usable.

## Expected Outcome

You should deliver a Docker image, the necessary Terraform files, and the script (in whatever
programming language you choose) to check that the correct version has been deployed. You should
also include instructions on how we can run your pipeline.
