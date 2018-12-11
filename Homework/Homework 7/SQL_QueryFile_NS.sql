use sakila;

-- 1a
select first_name,last_name
from actor;
-- 1b
select first_name,last_name,
concat(first_name, " " ,last_name) as 'Actor Name'
from actor;

-- 2a
select actor_id,first_name,last_name
from actor
where first_name = "Joe";

-- 2b
select actor_id,first_name,last_name
from actor
where last_name like "%GEN%";

-- 2c
select actor_id,first_name,last_name
from actor
where last_name like "%LI%"
order by last_name, first_name;

-- 2d Using `IN`, display the `country_id` and `country` columns of the following countries: Afghanistan, Bangladesh, and China:

select country_id, country
from country
where country in ('Afghanistan', 'Bangladesh','China');

-- 3a 

alter table actor
add description blob;

-- 3b

alter table actor
drop description;

-- 4a
select last_name, count(last_name)
from actor
group by last_name;

-- 4b
select last_name, count(last_name)
from actor
group by last_name
having count(last_name) > 2;



select first_name, last_name 
from actor
where last_name = 'williams';

-- 4c

update actor
set first_name = 'HARPO'
where first_name = 'GROUCHO';

-- 4d
update actor
set first_name = 'GROUCHO'
where first_name = 'HARPO';

-- 5a
create table address (
	address_id smallint(5),
    address varchar(50),
    address2 varchar(50) not null,
    district varchar(20),
    city_id smallint(5),
    postal_code varchar(10) not null,
    phone varchar(20),
    location geometry,
    last_update timestamp
);

-- 6a
select staff.first_name, staff.last_name, address.address
from staff
join address
on staff.address_id = address.address_id
group by first_name,last_name;

-- 6b
select staff.first_name, staff.last_name, sum(payment.amount)
from staff
join payment
on staff.staff_id = payment.staff_id
where payment.payment_date >= '2005-08-01'
group by first_name,last_name;

-- 6c

-- question about relating back to actor names from actor table

select film_actor.actor_id, film_actor.film_id, film.film_id, film.title
from film_actor
inner join film
on film_actor.film_id = film.film_id;

-- 6d

select film.title, count(inventory.inventory_id) Copies
from film
join inventory
on film.film_id = inventory.film_id
where title like 'Hunchback Impossible'
group by film.title;

-- 6e

select customer.first_name, customer.last_name , sum(amount)
from customer
join payment
on customer.customer_id = payment.customer_id
group by customer.first_name, customer.last_name
order by customer.last_name asc;

-- 7a 
select film.title
from film
where title like 'Q%' or title like 'K%' AND 
language_id = (select language_id from language where name = 'English');
 
-- 7b find all the actors in the movie and show first and last name
select first_name, last_name
from actor
where actor_id in 
	(
	select actor_id
	from film_actor
	where film_id in
	(
		select film_id
		from film
		where title = 'Alone Trip'
		)
	)
	;


-- 7c store 1 is canada store, show all name and email
select first_name, last_name, email
from customer
where store_id = 1;




-- 7d display all movies categoried as family
select title
from film
where film_id in 
	(
	select film_id
	from film_category
	where category_id in
		(
		select category_id 
		from category 
		where name = 'Family'
        )
	)
    ;

-- 7e rental count ordered by the count in desc order
select inventory.film_id, film.title, count(rental.rental_id) 'count'
from inventory
join rental
on inventory.inventory_id = rental.inventory_id
join film
on film.film_id = inventory.inventory_id
group by inventory.film_id
order by count(rental.rental_id) desc; 


-- 7f - Store 1 and 2, total income for year
select customer.store_id , sum(payment.amount) 'Income'
from customer
join payment
on customer.customer_id = payment.customer_id
group by customer.store_id;


-- 7g, join store, address, city, and country to get the information

select store.store_id, address.address, city.city, city.country_id, country.country
from store
join address
on store.address_id = address.address_id
join city
on address.city_id = city.city_id
join country
on city.country_id = country.country_id;

-- 7h find the gross income by category for films

select category.name,sum(payment.amount) Earnings
from film_category
join category
on film_category.category_id = category.category_id
join inventory
on inventory.film_id = film_category.film_id
join rental
on rental.inventory_id = inventory.inventory_id
join payment
on rental.rental_id = payment.rental_id
group by category.name
order by sum(payment.amount) desc;


-- 8a create a view of the previously generated result
create view top_5_gross as
select category.name,sum(payment.amount) Earnings
from film_category
join category
on film_category.category_id = category.category_id
join inventory
on inventory.film_id = film_category.film_id
join rental
on rental.inventory_id = inventory.inventory_id
join payment
on rental.rental_id = payment.rental_id
group by category.name
order by sum(payment.amount) desc;


-- 8b acess the view just like a table
select * from top_5_gross;

-- 8c.  Delete view created called top_5_gross

drop view top_5_gross;