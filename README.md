# roomsh_crawler
This project is simply parsing websites and get shops and their products info,
then store this data consistently with main project inside small redis db, so that main project can grab it and store this inside main database

Few notes about this project:
 - redis choosen as main DB beacause there is no need in long-term data storage, all data flushes once a day
 - no dependecy injector lib/framework, because it's so simple and light that we can inject anything here easy with just local file acting 
     as dependency container
 - settings and dependency container stored separately beacause this more clean
 - settings should store in TOML file
 - project in development
 - after project will be done, o would change it beacuse there is need to make core-app for whole project 
    (for example redis and models from this would migrate to core) 
