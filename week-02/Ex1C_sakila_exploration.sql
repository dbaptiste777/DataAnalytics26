/*
a) In the schema panel the "actor" tables include the actor id with their first name and last name.
b) In the schema panel, the "film" table includes a list of films and the descriptions for each film. Some of the descriptions include the release year, film title and the year it was released, and the legnth of the rental. 
c) The film_actor table also contains actor_id and film_id.
d) After right clicking on rental, this table includes the rental information for customers of this store. The information is easy to read, however it does not include exact names and has data which can be condensed. 
e) The inventory table includes what is currently in stock at this film store.
f) Based on what I learned so far, I need to use the film, rental, and inventory tables to understand the names of all films that were rented on a specific date. The tables are related to eachother because it shows when the film was rented, the name of the film, and when. 
*/


SELECT film_id FROM film;
SELECT rental_id FROM rental;
SELECT rental_date FROM rental;