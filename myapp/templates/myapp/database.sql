CREATE DATABASE IF NOT EXISTS MWJ;
USE MWJ;
-- You can input Date using current_date, Time using current_time;

CREATE TABLE IF NOT EXISTS products(
    productID varchar(100),
    productName varchar(100),
    productShortDescription varchar(100),
    productbFullDescription text,
    supplierID varchar(100),
    categoryID varchar(100),
    old_price varchar(20) default 0,
    new_price varchar(20) default 0,
    availableSizes varchar(100),
    availableColors varchar(100),
    discount varchar(20)  default 0,
    wight varchar(100),
    instock varchar(100)  default 0,
    unitsOnOrder int(10),
    picture varchar(200),
    ranking int(10),
    note text
    );

CREATE TABLE IF NOT EXISTS users(
    userID varchar(100),
    firstName varchar(100),
    lastName varchar(100),
    city varchar(100),
    state varchar(100),
    phoneCalls varchar(100),
    phoneWhatsapp varchar(100),
    email varchar(100),
    password varchar(100),
    repeatpassword varchar(100),
    emailVerified TinyInt(1),
    registrationDate date,
    verificationCode varchar(100),
    ip varchar(100),
    is_supplier int(1) default 0
    );

CREATE TABLE IF NOT EXISTS suppliers(
    supplierID varchar(100),
    companyName varchar(100),
    contactFName varchar(100),
    contactLName varchar(100),
    contactTitle varchar(5),
    address1 varchar(100),
    address2 varchar(100),
    address3 varchar(100),
    city varchar(100),
    state varchar(100),
    phoneCalls varchar(100),
    phoneWhatsapp varchar(100),
    email varchar(100),
    url varchar(100),
    paymentMethodsRTGS varchar(10),
    paymentMethodsUSD varchar(10),
    paymentMethodsVISA varchar(10),
    discount float,
    categoryID varchar(100),
    notes text,
    currentOrder varchar(100),
    customerID varchar(100)
    );

CREATE TABLE IF NOT EXISTS categories(
    categoryID int NOT NULL AUTO_INCREMENT KEY,
    categoryName varchar(100),
    descriprion text,
    pricture varchar(200)
    );

CREATE TABLE IF NOT EXISTS orders(
    orderID varchar(100),
    customerID varchar(100),
    orderNumber varchar(100),
    paymentID varchar(100),
    orderDate date,
    shipDate date,
    requiredDate date,
    fullFilled TinyInt(1),
    paid TinyInt(1),
    paymentDueDate date,
    total varchar(100),
    discount float,
    numItems int(10),
    productID varchar(100)
);

CREATE TABLE IF NOT EXISTS payment(
    paymentID varchar(100),
    paymentMethods varchar(100)
    );


-- INSERTS-----------------------
insert into categories(categoryName)
     values("Arts and Craft"),
     ("Automotive"),
     ("Baby"),
     ("Beauty Products"),
     ("Books"),
     ("Computers"),
     ("Electronics"),
     ("Women"),
     ("Men"),
     ("Girl"),
     ("Boy"),
     ("Health Products"),
     ("Home Products"),
     ("Industrial"),
     ("Agro Products"),
     ("Food"),
     ("Animals"),
     ("Services"),
     ("school"),
     ("cars"),
     ("games");





insert into categories(category_name, slug)
     values("Arts and Craft", "Arts-and-Craft"),
     ("Automotive", 'Automotive'),
     ("Baby", 'Baby'),
     ("Beauty Products", 'Beauty-Products'),
     ("Books", 'Books'),
     ("Computers", "Computers"),
     ("Electronics", "Electronics"),
     ("Women", "Women"),
     ("Men", "Men"),
     ("Girls", "Girls"),
     ("Boys", "Boys"),
     ("Health Products", "Health-Products"),
     ("Home Products", "Home-Products"),
     ("Industrial", "Industrial"),
     ("Agro Products", "Agro-Products"),
     ("Food", "Food"),
     ("Animals", "Animals"),
     ("Services", "Services"),
     ("School", "School"),
     ("Cars", "Cars"),
     ("Games", "Games");

