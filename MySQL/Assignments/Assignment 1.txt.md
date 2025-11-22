**Question 1: 1. Login to MySQL and view all databases already present. You should get following result:**



Answer:

mysql> show databases;

+--------------------+

| Database           |

+--------------------+

| fbs                |

| firstbit           |

| information\_schema |

| mysql              |

| performance\_schema |

| sakila             |

| sys                |

| world              |

+--------------------+

8 rows in set (0.00 sec)



mysql>





**Question 2: Write an SQL statement to create a simple table countries including columns country\_id,country\_name and region id. After this display the structure of**

**table as below.**



Answer:

mysql> use firstbit

Database changed

mysql> create table countries

    -> (country\_id int(11), country\_name varchar(20), region\_id int(11));

Query OK, 0 rows affected, 2 warnings (0.02 sec)



mysql> desc countries;

+--------------+-------------+------+-----+---------+-------+

| Field        | Type        | Null | Key | Default | Extra |

+--------------+-------------+------+-----+---------+-------+

| country\_id   | int         | YES  |     | NULL    |       |

| country\_name | varchar(20) | YES  |     | NULL    |       |

| region\_id    | int         | YES  |     | NULL    |       |

+--------------+-------------+------+-----+---------+-------+

3 rows in set (0.01 sec)



mysql>







**Question 3. . Write an SQL statement to create a table named jobs including columns job id, job title, min salary, max salary and check whether the max salary amount exceeding the upper limit 25000. Also set job id as primary key and entering null values for job title is not allowed**



Answer:



mysql> create table jobs

    -> (job\_id int primary key,

    -> job\_title varchar(20) not null,

    -> min\_salary float(10,3),

    -> max\_salary float(10,3),

    -> check (max\_salary <= 25000));

Query OK, 0 rows affected, 2 warnings (0.03 sec)



mysql> desc jobs;

+------------+-------------+------+-----+---------+-------+

| Field      | Type        | Null | Key | Default | Extra |

+------------+-------------+------+-----+---------+-------+

| job\_id     | int         | NO   | PRI | NULL    |       |

| job\_title  | varchar(20) | NO   |     | NULL    |       |

| min\_salary | float(10,3) | YES  |     | NULL    |       |

| max\_salary | float(10,3) | YES  |     | NULL    |       |

+------------+-------------+------+-----+---------+-------+

4 rows in set (0.00 sec)



mysql>



**Question 4: Write a SQL statement to create a table named job history including columns employee id, start date, end date, job id and department id.**

Answer:

mysql> create table job\_history

    -> (employee\_id int, start\_date date, end\_date date, job\_id int, department\_id int);

Query OK, 0 rows affected (0.02 sec)



mysql> desc job\_history;

+---------------+------+------+-----+---------+-------+

| Field         | Type | Null | Key | Default | Extra |

+---------------+------+------+-----+---------+-------+

| employee\_id   | int  | YES  |     | NULL    |       |

| start\_date    | date | YES  |     | NULL    |       |

| end\_date      | date | YES  |     | NULL    |       |

| job\_id        | int  | YES  |     | NULL    |       |

| department\_id | int  | YES  |     | NULL    |       |

+---------------+------+------+-----+---------+-------+

5 rows in set (0.00 sec)



mysql>



**Question 5: Write an SQL statement to after a table named countries to make sure that no duplicate data against column country id will be allowed at the time of insertion.**

Answer :

mysql> desc countries;

+--------------+-------------+------+-----+---------+-------+

| Field        | Type        | Null | Key | Default | Extra |

+--------------+-------------+------+-----+---------+-------+

| country\_id   | int         | YES  |     | NULL    |       |

| country\_name | varchar(20) | YES  |     | NULL    |       |

| region\_id    | int         | YES  |     | NULL    |       |

+--------------+-------------+------+-----+---------+-------+

3 rows in set (0.00 sec)



mysql> alter table countries

    -> modify column country\_id int unique;

Query OK, 0 rows affected (0.03 sec)

Records: 0  Duplicates: 0  Warnings: 0



mysql> desc countries;

+--------------+-------------+------+-----+---------+-------+

| Field        | Type        | Null | Key | Default | Extra |

+--------------+-------------+------+-----+---------+-------+

| country\_id   | int         | YES  | UNI | NULL    |       |

| country\_name | varchar(20) | YES  |     | NULL    |       |

| region\_id    | int         | YES  |     | NULL    |       |

+--------------+-------------+------+-----+---------+-------+

3 rows in set (0.00 sec)



mysql>





**Question 6:Write an SQL statement to create a table named jobs including columns job\_id, job title, min salary and max salary, and make sure that, the default value for job title is blank and min salary is 8000 and max salary is NULL will be entered automatically at the time of insertion if no value assigned for the specified columns**.

Answer:

mysql> alter table jobs

    -> modify job\_title varchar(20) default '';

Query OK, 0 rows affected (0.04 sec)

Records: 0  Duplicates: 0  Warnings: 0



mysql> alter table jobs

    -> modify min\_salary float(10,2) default 8000;

Query OK, 0 rows affected, 1 warning (0.01 sec)

Records: 0  Duplicates: 0  Warnings: 1



mysql> alter table jobs

    -> modify max\_salary float(10,2) default null;

Query OK, 0 rows affected, 1 warning (0.01 sec)

Records: 0  Duplicates: 0  Warnings: 1



mysql> desc jobs;

+------------+-------------+------+-----+---------+-------+

| Field      | Type        | Null | Key | Default | Extra |

+------------+-------------+------+-----+---------+-------+

| job\_id     | int         | NO   | PRI | NULL    |       |

| job\_title  | varchar(20) | YES  |     |         |       |

| min\_salary | float(10,2) | YES  |     | 8000.00 |       |

| max\_salary | float(10,2) | YES  |     | NULL    |       |

+------------+-------------+------+-----+---------+-------+

4 rows in set (0.00 sec)



mysql>



**Quesion 7: Create a Department table with following structure**



Answer:

mysql> create table dept

    -> (department\_id int,

    -> department\_name varchar(20),

    -> manager\_id int,

    -> location\_id int,

    -> primary key (department\_id, manager\_id));

Query OK, 0 rows affected (0.02 sec)



mysql> desc dept;

+-----------------+-------------+------+-----+---------+-------+

| Field           | Type        | Null | Key | Default | Extra |

+-----------------+-------------+------+-----+---------+-------+

| department\_id   | int         | NO   | PRI | NULL    |       |

| department\_name | varchar(20) | YES  |     | NULL    |       |

| manager\_id      | int         | NO   | PRI | NULL    |       |

| location\_id     | int         | YES  |     | NULL    |       |

+-----------------+-------------+------+-----+---------+-------+

4 rows in set (0.00 sec)



mysql> alter table dept

    -> modify column department\_name varchar(20) not null;

Query OK, 0 rows affected (0.03 sec)

Records: 0  Duplicates: 0  Warnings: 0



mysql> desc dept;

+-----------------+-------------+------+-----+---------+-------+

| Field           | Type        | Null | Key | Default | Extra |

+-----------------+-------------+------+-----+---------+-------+

| department\_id   | int         | NO   | PRI | NULL    |       |

| department\_name | varchar(20) | NO   |     | NULL    |       |

| manager\_id      | int         | NO   | PRI | NULL    |       |

| location\_id     | int         | YES  |     | NULL    |       |

+-----------------+-------------+------+-----+---------+-------+

4 rows in set (0.00 sec)



mysql> alter table dept

    -> modify column department\_id int default '0';

Query OK, 0 rows affected (0.01 sec)

Records: 0  Duplicates: 0  Warnings: 0



mysql> desc dept;

+-----------------+-------------+------+-----+---------+-------+

| Field           | Type        | Null | Key | Default | Extra |

+-----------------+-------------+------+-----+---------+-------+

| department\_id   | int         | NO   | PRI | 0       |       |

| department\_name | varchar(20) | NO   |     | NULL    |       |

| manager\_id      | int         | NO   | PRI | NULL    |       |

| location\_id     | int         | YES  |     | NULL    |       |

+-----------------+-------------+------+-----+---------+-------+

4 rows in set (0.00 sec)



mysql> alter table dept

    -> modify column manager\_id int default '0';

Query OK, 0 rows affected (0.01 sec)

Records: 0  Duplicates: 0  Warnings: 0



mysql> desc dept;

+-----------------+-------------+------+-----+---------+-------+

| Field           | Type        | Null | Key | Default | Extra |

+-----------------+-------------+------+-----+---------+-------+

| department\_id   | int         | NO   | PRI | 0       |       |

| department\_name | varchar(20) | NO   |     | NULL    |       |

| manager\_id      | int         | NO   | PRI | 0       |       |

| location\_id     | int         | YES  |     | NULL    |       |

+-----------------+-------------+------+-----+---------+-------+

4 rows in set (0.00 sec)



mysql>



**Question 8:Write an SQL statement to create a table employees including columns employee\_id, first\_name, last\_name, email, phone\_number hire\_date, job\_id, salary, commission, manager id and department id and make sure that, the employee id column does not contain any duplicate value at the time of insertion and the foreign key columns combined by department id and manager id columns contain only those unique combination values, which combinations are exists in the departments table.**

Answer :



mysql> desc dept;

+-----------------+-------------+------+-----+---------+-------+

| Field           | Type        | Null | Key | Default | Extra |

+-----------------+-------------+------+-----+---------+-------+

| department\_id   | int         | NO   | PRI | 0       |       |

| department\_name | varchar(20) | NO   |     | NULL    |       |

| manager\_id      | int         | NO   | PRI | 0       |       |

| location\_id     | int         | YES  |     | NULL    |       |

+-----------------+-------------+------+-----+---------+-------+

4 rows in set (0.00 sec)



mysql> create table employees

    -> (employee\_id int primary key,

    -> first\_name varchar(20),

    -> last\_name varchar(20),

    -> email varchar(20),

    -> phone\_number int,

    -> hier\_date date not null,

    -> job\_id int not null,

    -> salary decimal(8,2),

    -> commission decimal(8,2),

    -> manager\_id int,

    -> department\_id int,

    -> foreign key (department\_id, manager\_id)

    -> references dept(department\_id, manager\_id)

    -> );

Query OK, 0 rows affected (0.01 sec)



mysql> desc employees;

+---------------+--------------+------+-----+---------+-------+

| Field         | Type         | Null | Key | Default | Extra |

+---------------+--------------+------+-----+---------+-------+

| employee\_id   | int          | NO   | PRI | NULL    |       |

| first\_name    | varchar(20)  | YES  |     | NULL    |       |

| last\_name     | varchar(20)  | YES  |     | NULL    |       |

| email         | varchar(20)  | YES  |     | NULL    |       |

| phone\_number  | int          | YES  |     | NULL    |       |

| hier\_date     | date         | NO   |     | NULL    |       |

| job\_id        | int          | NO   |     | NULL    |       |

| salary        | decimal(8,2) | YES  |     | NULL    |       |

| commission    | decimal(8,2) | YES  |     | NULL    |       |

| manager\_id    | int          | YES  |     | NULL    |       |

| department\_id | int          | YES  | MUL | NULL    |       |

+---------------+--------------+------+-----+---------+-------+

11 rows in set (0.00 sec)



mysql>

