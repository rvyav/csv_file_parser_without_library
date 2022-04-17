# WELCOME TO CSV PARSER WITHOUT LIBRARY

## GOAL

Build an alternative way to parse CSV files without the need of a third-party library, framework or python prebuilt module.

## HOW TO RUN THIS APPLICATION

The default CSV file to select when asked for the user input is `team_orko.csv` CSV file key.

(You can always select the other CSV file if you want to...)

## DOCKER SETUP

Please download `docker` desktop here: https://www.docker.com/products/docker-desktop/

## LAUNCH THE APPLICATION

To run this is application in a single line of code from the root folder, run: 

`docker build -t <CONTAINER NAME> . && docker run -it <CONTAINER NAME>`

Eg.: `docker build -t csv_parser . && docker run -it csv_parser`

After the application is terminated, you can re-run it via: `docker run -it <CONTAINER NAME>`

## EXTRA COMMANDS

List all images: `docker images`

List all containers: `docker container ls -a`

Stop a specific container: `docker rm -f <CONTAINER ID>`

If you are unable to stop the container, please run : `docker rm -f $(docker ps -a -q)` to remove stop all containers

Remove all images and containers: `docker system prune -a` to stop all containers and all unused images

## TO DO: some EDGE CASES to consider to improve the CSV parsing functionality

- Check for trailing spaces at the beginning and end of the file
- Check the delimiter
- Possible duplicate file names in the file directory
- A generator can be used while parsing the CSV file for memory efficiency instead of the for loop
...

## GHERKIN ISSUE

Something is wrong with the `GHERKIN` package, the import is failing therefore can't be used.
