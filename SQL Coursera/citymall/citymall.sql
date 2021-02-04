select * from citymall;

-- 1. Customers who ordered: Number of customers who ordered in the month of July

select count(distinct(user_id)) No_of_customers from citymall
where month(processing_at)=7;

-- 2. Acquired customers: Number of customers who ordered in July for the first time, i.e. they did not place an order before July

select count(distinct(user_id)) No_of_customers from citymall
where month(processing_at) = 7 and user_id not in (select distinct(user_id) from citymall where month(processing_at)<7  );


-- 3. Resurrected customers: Number of customers who ordered in July, but did not place an order in June, but had placed orders before June
select count(distinct(user_id)) No_of_customers from citymall
where month(processing_at) in (select distinct(month(processing_at)) from citymall where month(processing_at) <> 6 and month(processing_at) <= 7 ) 
and user_id not in (select distinct(user_id) from citymall where month(processing_at)=6) ;


-- 4. Churned customers: Number of customers who had ordered in June but did not order in July.
select count(distinct(user_id)) No_of_customers from citymall
where month(processing_at) = 6 and user_id not in (select distinct(user_id) from citymall where month(processing_at) = 7) ;


-- 5. First order date in July: List of customers with their first order date in July month (not lifetime first order), who has already ordered in June.

select distinct(user_id) user_id, min(date(processing_at)) date from citymall 
where month(processing_at)= 7 and user_id in (select user_id from citymall where month(processing_at)=6 ) 
group by user_id ;



			