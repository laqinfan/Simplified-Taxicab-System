# Generate database file similar to employeedb.txt

import sys, random
from faker import Faker

numDrivers = 10
numVehicles = numDrivers
numCustomers = 10

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
    long = location[1]

    frmtStr = "({},{},{}),"
    if i == numVehicles - 1:
        frmtStr = "({},{},{});"
    record = frmtStr.format(i, lat, long)
    print(record)

print("\ninsert into customer_tracker values")
for i in range(numCustomers):
    profile = fake.profile(sex=None)
    location = profile['current_location']
    lat = location[0]
    long = location[1]

    frmtStr = "('{}',{},{}),"
    if i == numCustomers - 1:
        frmtStr = "('{}',{},{});"
    record = frmtStr.format(customerEmail[i], lat, long)
    print(record)

