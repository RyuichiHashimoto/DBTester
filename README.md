# DBTester
A Testing Environment for Database Behavior

DBTester is a repository designed to provide a testing environment for studying database behavior, particularly focusing on web security.
This repository includes environments for various databases and a login-enabled web application.

**Table of Contents**
- [1.  Prerequisites](#1--prerequisites)
- [2. Repository Contents](#2-repository-contents)
  - [2.1. mysql](#21-mysql)
  - [2.2. mongo](#22-mongo)
  - [2.3. web-server](#23-web-server)
  - [2.3.1. Accessing the Web Server](#231-accessing-the-web-server)
  - [2.3.2. Pages](#232-pages)
    - [2.3.3. Implemented Web APIs](#233-implemented-web-apis)
  - [2.4. client](#24-client)
- [3. How to Use](#3-how-to-use)
- [4. Notes](#4-notes)
- [Disclaimer](#disclaimer)


## 1.  Prerequisites
- docker: version 26.1.4, build 5650f9b
- docker-compose: version v2.27.1

## 2. Repository Contents
This repository provides four main services (databases and web server) at present.
- Hostnames for each service can be found in docker-compose.yaml.
- Database configuration is specified in the .env file.

### 2.1. mysql
A widely-used relational database management system (RDBMS).

### 2.2. mongo
A popular NoSQL database.

### 2.3. web-server
A simple website prepared to interact with the databases.

Built with Apache, PHP, and HTML.
2.3.1. Accessing the Web Server
Open a browser and navigate to http://localhost:4200.



### 2.3.1. Accessing the Web Server
Open a browser and navigate to http://localhost:4200.

![alt text](/assets/web-server-top-page.png)


### 2.3.2. Pages
The pages can be found under the web-server/html directory.


#### 2.3.3. Implemented Web APIs
1. login.php
   - Method: POST
   - Parameters:
     - username (string)
     - password (string)
   - Functionality:
     - queries the database to check if the provided username and password exist.
     - returns success if the combination exists; otherwise, returns a failure message.
  

### 2.4. client
A container for testing hacking tools such as sqlmap.
Includes tools (planned) for adding, deleting, and modifying records in MongoDB and MySQL databases, as well as displaying database contents.


## 3. How to Use
1. Clone the repository:
   
   ```git clone https://github.com/RyuichiHashimoto/DBTester.git```

2. Build and run the containers using Docker Compose:

    ```cd DBTester```
    ```docker compose up -d --build```


3. Access the MySQL database and initialize records:
   ```docker exec -it mysql-db /bin/bash```
   ```mysql -u {user} -p{password} users < init.sql```

## 4. Notes
Each Docker container has ```ctf-network``` docker-network, and connected to the network. You can connect other repositories' container(s) to this network to access the services provided by this repository.

## Disclaimer
This repository is intentionally designed as a vulnerable website for the purpose of learning web security.

- Do not use this repository for anything other than personal educational purposes.
- Avoid storing or handling sensitive information using this repository.