1. Select all the male drivers fname and lname whose vehicle type is SUV.

	Select driver.fname From driver, vehicle Where vehicle.dssn = driver.ssn and vehicle.type = ‘SUV’  

2. Find the number of drivers who were born after “12-01-2000”.

	select fname, count(*) from driver where driver.bdate > '12-01-2000' group by fname

3. Find the average overall scores of the rides for customers were born after “12-01-2010”

s	elect cost, avg(feedback.overall) from feedback, ride, customer where feedback.ride_id = ride.rid and ride.c_mail = customer.email_id  and customer.bdate > '12-01-2010' group by  cost


4. Retrieve the customers who apply more than 10 coupons to rides  

	select fname, count(*) from customer, coupon, applies_on where coupon.customer_email = customer.email_id and applies_on.coupon_id = coupon.cid and customer_email in (select customer_email from 	coupon group by customer_email having count(*) > 1) group by fname 


5. Retrieve locations of vehicles, whose luggage_count > 4

	select lat, longitude from vehicle_tracker, vehicle where vehicle_tracker.vehicle_id = vehicle.vid and vehicle. luggage_count > 4
