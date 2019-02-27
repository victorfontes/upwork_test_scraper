# Scraper Coding Exercise:

I tried to keep things functional and simple, so I skipped stuff like logging, retry system, etc. 

Some comments:
- I'm using records instead of psycopg2 directly, its a handy wrapper that makes things easier for small projects.
- There is a command line to run the scraper and see the results of some querys.
- Probably a Fight would be separate entity in real world because it has more attributes.

## Usage:

```
export DATABASE_URI="postgres://... credentials provided over chat"

pipenv install
pipenv shell

./main.py scrape-event
./main.py show-abc-fighters
./main.py show-fights
./main.py --help
  
```


