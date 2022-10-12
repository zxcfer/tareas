# Data Engineer Task

* Clone this repository on your local machine and push your solution into a new one in your own GitHub account
* Please consider your git history as this will be reviewed
* Commit & push code regularly
* Use the Netflix csv file as your data source
* Once complete, please send us a link to your repository

## Steps

**Step 1** : Create a database to store the data using a Dimensional Modeling Design. (MSSQL / MySQL / Postgres)

Output - SQL Scripts

**Step 2** : Create a python programme that will run the above SQL scripts and ETL the data from the csv file into the database.

Output – Python programme

**Step 3** : Enhance the data by adding the cast members' gender (Male / Female). [https://www.aminer.cn/gender/api](https://www.aminer.cn/gender/api) or any other source you want to use.

Output – Python programme

**Step 4** : Write SQL Scripts to validate the data loaded.

Output - Missing data report

Output - Invalid / strange data report

**Step 5** : Write SQL Scripts to return the following:

- What is the most common first name among actors and actresses?

- Which Movie had the longest timespan from release to appearing on Netflix?

- Which Month of the year had the most new releases historically?

- Which year had the largest increase year on year (percentage wise) for TV Shows?

- List the actresses that have appeared in a movie with Woody Harrelson more than once.

**Step 6** : Combine all the previous steps into a solid Python programme that has unit testing. Feel free to create a main file that can be ran via a Python command line.

Output – Python programme

## Data

| **Column** | **Value** | **Description** |
| --- | --- | --- |
| show\_id | String | Unique ID for every Movie / Tv Show |
| type | String | Identifier - A Movie or TV Show |
| Title | String | Title of the Movie / Tv Show |
| Director | String | Director of the Movie |
| Cast | String | Actors involved in the movie / show |
| Country | String | Country where the movie / show was produced |
| Date\_added | Date | Date it was added on Netflix |
| Release\_year | Integer | Actual Release year of the move / show |
| Rating | String | TV Rating of the movie / show |
| Duration | String | Total Duration - in minutes or number of seasons |
| Listed\_in | String | Genre |
| description | String | The summary description |
