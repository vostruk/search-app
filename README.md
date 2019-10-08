# search-app
Application that periodically fetches 'technology' related articles/news from the internet.


Application have REST api based search interface and is contenarized using docker. The dockerized solution could be found in DockerHub at:

```

```

To run application clone repository and run:

```
docker-compose up
```

If you want to use pure image from DockerHub run:

```
docker run ...
```

To see awailable endpoint with description go to root endpoint /

System supports search with technology names. 

##App Architecture
App is composed of two logical components: 
1. news source provider which gives the links of main pages of the websited where technology articles could be found
    Examples: GoogleUrlProvider class or DuckDuckGoUrlProvider class

2. articles scraper which downloads the articles from the page

3. articles estimator which looks at the downloaded Text and see if it has proper topic and if it is interesting for us

4. articles saver which saves downloaded articles to database (Mongo)

App bind those modules together in main app.py script

