# Generate database

import sys, random
from datetime import timedelta

from faker import Faker
import geopy
from geopy.distance import VincentyDistance

numDrivers = 100
numVehicles = numDrivers
numCustomers = 500
numRides = 2000
numCoupons = 50
appliedCoupons = 20

print("drop database if exists pdb1;")
print("create database pdb1;")
print("use pdb1;\n")

print("create table driver (\n" \
      "  ssn numeric(9) not null,\n" \
      "  fname char(15) not null,\n" \
      "  lname char(30) not null,\n" \
      "  gender char(1) not null,\n" \
      "  bdate date not null,\n" \
      "  primary key(ssn)\n" \
      ");\n")

print("create table vehicle (\n" \
      "  vid numeric(9) not null,\n" \
      "  type char(5) not null,\n" \
      "  passenger_count numeric(1) not null,\n" \
      "  luggage_count numeric(1) not null,\n" \
      "  dssn numeric(9) not null,\n"
      "  primary key (vid),\n" \
      "  foreign key (dssn) references driver(ssn)\n" \
      ");\n")

print("create table customer (\n" \
      "  email_id char(200) not null,\n"
      "  fname char(15) not null,\n" \
      "  lname char(30) not null,\n" \
      "  gender char(1) not null,\n" \
      "  bdate date not null,\n" \
      "  primary key (email_id)\n" \
      ");\n")

print("create table vehicle_tracker (\n" \
      "  vehicle_id numeric(9) not null,\n"
      "  lat decimal(18, 9) not null,\n"
      "  longitude decimal(18, 9) not null,\n"
      "  foreign key (vehicle_id) references vehicle(vid)\n"
      ");\n")

print("create table customer_tracker (\n" \
      "  customer_email char(200) not null,\n"
      "  lat decimal(18, 9) not null,\n"
      "  longitude decimal(18, 9) not null,\n"
      "  foreign key (customer_email) references customer(email_id)\n"
      ");\n")

print("create table ride (\n" \
      "  rid numeric(9) not null,\n"
      "  start_time datetime not null,\n"
      "  end_time datetime not null,\n"
      "  src_lat decimal(18, 9) not null,\n"
      "  src_long decimal(18, 9) not null,\n"
      "  dst_lat decimal(18, 9) not null,\n"
      "  dst_long decimal(18, 9) not null,\n"
      "  cost numeric(5) not null,\n"
      "  c_mail char(200) not null,\n"
      "  v_id numeric(9) not null,\n"
      "  primary key (rid),\n"
      "  foreign key (c_mail) references customer(email_id),\n"
      "  foreign key (v_id) references vehicle(vid)\n"
      ");\n")

print("create table feedback (\n" \
      "  ride_id numeric(9) not null, \n"
      "  overall numeric(1) not null,\n"
      "  customer_service numeric(1) not null,\n"
      "  safety numeric(1) not null,\n"
      "  cleanliness numeric(1) not null,\n"
      "  vehicle_condition numeric(1) not null,\n"
      "  foreign key (ride_id) references ride(rid) \n"
      ");\n")

print("create table coupon (\n" \
      "  cid numeric(9) not null, \n"
      "  value numeric(2) not null,\n"
      "  customer_email char(200) not null,\n"
      "  primary key (cid), \n"
      "  foreign key (customer_email) references customer(email_id) \n"
      ");\n")

print("create table applies_on (\n" \
      "  coupon_id numeric(9) not null, \n"
      "  ride_id numeric(9) not null,\n"
      "  foreign key (coupon_id) references coupon(cid),\n"
      "  foreign key (ride_id) references ride(rid)\n"
      ");\n")

fake = Faker()

driverSSN = {}
print("insert into driver values")
for i in range(numDrivers):
    profile = fake.profile(sex=None)
    ssn = profile['ssn'].replace("-", "")
    name = profile['name']
    fname = name.split(" ")[0]
    lname = name.split(" ")[1]
    gender = profile['sex']
    dob = profile['birthdate']

    driverSSN[i] = ssn

    frmtStr = "({},'{}','{}','{}','{}'),"
    if i == numDrivers - 1:
        frmtStr = "({},'{}','{}','{}','{}');"
    record = frmtStr.format(ssn, fname, lname, gender, dob)
    print(record)

vehicle_types = ['sedan', 'SUV', 'van']
print("\ninsert into vehicle values")
for i in range(numVehicles):
    type = random.choice(vehicle_types)
    passenger_count = random.randint(1, 6)
    luggage_count = random.randint(1, 6)

    frmtStr = "({},'{}',{},{},{}),"
    if i == numDrivers - 1:
        frmtStr = "({},'{}',{},{},{});"
    record = frmtStr.format(i, type, passenger_count, luggage_count, driverSSN[i])
    print(record)

customerEmail = {}
print("\ninsert into customer values")
for i in range(numCustomers):
    profile = fake.profile(sex=None)
    email = profile['mail']
    name = profile['name']
    fname = name.split(" ")[0]
    lname = name.split(" ")[1]
    gender = profile['sex']
    dob = profile['birthdate']

    customerEmail[i] = email

    frmtStr = "('{}','{}','{}','{}','{}'),"
    if i == numCustomers - 1:
        frmtStr = "('{}','{}','{}','{}','{}');"
    record = frmtStr.format(email, fname, lname, gender, dob)
    print(record)

print("\ninsert into vehicle_tracker values")
for i in range(numVehicles):
    profile = fake.profile(sex=None)
    location = profile['current_location']
    lat = location[0]
    longitude = location[1]

    frmtStr = "({},{},{}),"
    if i == numVehicles - 1:
        frmtStr = "({},{},{});"
    record = frmtStr.format(i, lat, longitude)
    print(record)

print("\ninsert into customer_tracker values")
for i in range(numCustomers):
    profile = fake.profile(sex=None)
    location = profile['current_location']
    lat = location[0]
    longitude = location[1]

    frmtStr = "('{}',{},{}),"
    if i == numCustomers - 1:
        frmtStr = "('{}',{},{});"
    record = frmtStr.format(customerEmail[i], lat, longitude)
    print(record)

print("\ninsert into ride values")
for i in range(numRides):
    start_time = fake.past_datetime(start_date="-180d")
    # Ride at least took 10 min to 3 hours
    end_time = start_time + timedelta(seconds=random.randint(600, 10800))

    # km/hour
    avgSpeedOfVechile = random.randint(30, 70)
    distanceTravelled = ((end_time - start_time).seconds * avgSpeedOfVechile) / 3600

    profile  = fake.profile(sex=None)
    location = profile['current_location']
    src_lat  = location[0]
    src_long = location[1]

    origin = geopy.Point(src_lat, src_long)
    destination = VincentyDistance(kilometers=distanceTravelled).destination(origin, random.randint(0, 180))

    dst_lat  = round(destination.latitude, 9)
    dst_long = round(destination.longitude, 9)

    # Initial cost + distanceTravveled * rate
    cost = int(distanceTravelled * 0.67 + random.randint(5, 20))

    frmtStr = "({},'{}','{}','{}','{}','{}','{}',{},'{}',{}),"
    if i == numRides - 1:
        frmtStr = "({},'{}','{}','{}','{}','{}','{}',{},'{}',{});"
    record = frmtStr.format(i, start_time, end_time,
                            src_lat, src_long,
                            dst_lat, dst_long, cost,
                            random.choice(customerEmail), random.randint(0, numVehicles-1))
    print(record)

print("\ninsert into feedback values")
for i in range(numRides):
    frmtStr = "({},{},{},{},{},{}),"
    if i == numRides - 1:
        frmtStr = "({},{},{},{},{},{});"
    record = frmtStr.format(i, random.randint(0,5), random.randint(0,5),
                            random.randint(0,5), random.randint(0,5), random.randint(0,5))
    print(record)

print("\ninsert into coupon values")
for i in range(numCoupons):
    frmtStr = "({},{},'{}'),"
    if i == numCoupons - 1:
        frmtStr = "({},{},'{}');"
    # 5-30%
    record = frmtStr.format(i, random.randint(5,30), random.choice(customerEmail))
    print(record)

print("\ninsert into applies_on values")
rideList = []
couponList = []
for i in range(appliedCoupons):
    frmtStr = "({},{}),"
    if i == appliedCoupons - 1:
        frmtStr = "({},{});"

    # One coupon can only apply to one ride

    rideid = random.randint(0, numRides-1)
    coupondid = random.randint(0, numCoupons-1)

    while (coupondid in couponList or rideid in rideList):
        rideid = random.randint(0, numRides-1)
        coupondid = random.randint(0, numCoupons-1)

    record = frmtStr.format(coupondid, rideid)
    couponList.append(coupondid)
    rideList.append(rideid)

    print(record)
