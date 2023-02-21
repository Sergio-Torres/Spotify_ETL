# Spotify_ETL
To obtain the data visit the spotify page for developers: <a href="https://developer.spotify.com/console/get-recently-played/?limit=100&after=&before=">here</a>

When we are on the page, we select get token, as shown in the image:

![Image text](https://github.com/Sergio-Torres/Spotify_ETL/blob/master/img%20readme/1.jpg)

Then we mark use-read-recently-played and to finish we click on request token, this will generate a code that we must copy

![Image text](https://github.com/Sergio-Torres/Spotify_ETL/blob/master/img%20readme/2.jpg)

In the directory we will use the `settings.ini file`

We copy the code in the TOKEN variable.

### settings.ini
```
[APP]
TOKEN = QS1C.....
```
And we add our configuration for mysql:
```
[DDBB]
HOST_NAME = l..
USER = r...
PASSWORD = 12..
DB_NAME = bdna...
```
In the `main.py` file you must add the name you want for your table, the default name is "table_name"

### main.py
```
37:     try:
38:        df.to_sql("table_name", engine)
```
After that you can run the main.py file and check in MySQL your databases with the information in the table 👍


## Aspects to consider 
The token only has a certain "useful life" time, so on occasions it will be necessary to change it, you just have to carry out the same procedure explained at the beginning.






