# Technical Test for News UK Devops Engineers

**Prerequisites**: IDE of your choice, Docker, Terraform

We want to deploy our `server.js` app.

Your job is to dockerize the server. It will always spit out version `0.21.3`. Modify the application so there's a new path which could increment this verison.

We have included a `Makefile` to install the dependencies.

## Expected Outcome

You should be able to open the application while running on Docker in your browser and have two working paths - one to increment the current version and one to return the current version of the application.

_BONUS_: Get the version from a second container.
