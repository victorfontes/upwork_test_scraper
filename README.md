# Coding Exercise Details:
We will store our data in three database tables.
One table is events, and the other table is fighters.
Fighters table should only have id and name columns.
Events table should only have id, name of event, and date of event.
The final table is a junction table, as events and fights have a many-to-many relationship.

There is much more information available on the page, but for simplicity, this is all I am asking for.

Scrape this specific event page https://www.bestfightodds.com/events/ufc-231-holloway-vs-ortega-1584 to populate the database. So after you are done, you will have one event in the events table, and something like 20-30 fighters in the fighters table.

Store in PostgreSQL cloud database. Create one. There are plenty of free options that you can spin up quickly, ElephantSQL being one, or Google Cloud, or one of your choice. Use whatever option you prefer.
I recommend using the psycopg python library to connect to the database, but use your preference.

In a separate python file, write a query that returns all fighters whose last name starts with the letters 'A','B',or 'C'.

