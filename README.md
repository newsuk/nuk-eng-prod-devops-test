## Technical Test for News UK Platform Engineers

Prerequisites: IDE of your choice, Docker

We want to create an app and deploy it using Docker.
Your job is to create a Javascript application that has the following paths:

- `/` - Homepage, should display some text.
- `/version` - Displays the current version of the application.
- `/next-version` - Increment the current version of the application and show both new and old versions. Increment version every time you load the page.

Once the application is ready you need to dockerize it.
Unit test the application using a testing library of your choice.
Consider using the separation of concerns design principle.

## Expected Outcome

You should be able to open the application while running on Docker in your browser and have the three working paths described above.

BONUS: Get the version from a second container.
