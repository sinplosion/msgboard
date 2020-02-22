# MSG Board

### Description
A basic message board type forum. In the forum users can create accounts with unique nicknames and logged in users can create threads and comment on threads and edit their posts. Accounts can have admin status to delete and edit regular users posts.

All the threads are listed on the front page by activity. First one being the one with the newest comment in the thread. Comments in threads are listed by date. Oldest comment being at the top and newest at the bottom.

#### Demo

[Heroku](https://msgboard-tsoha.herokuapp.com/comment)


Test accounts: (every new user gets the role 'USER')

|**Username**   |**Password**   |**Role**   |
|---------------|---------------|-----------|
|admin          |admin          |ADMIN      |
|user           | user          |USER       |


The heroku index page has a query that for some reason doesn't work on heroku but works on linux. Please note that when logging in the application sends you to the index page, which as of now gives an error.


#### Installing on linux

Commands to run on terminal:
```
$ git clone https://github.com/sinplosion/msgboard.git
$ cd msgboard/
~/msgboard$ python3 -m venv venv
~/msgboard$ source venv/bin/activate
~/msgboard$ pip install -r requirements.txt
~/msgboard$ python run.py
```
After running the 'run.py' the application will run in [http://localhost:5000](http://localhost:5000) alternative link for localhost is also [127.0.0.1:5000](http://127.0.0.1:5000)


#### User stories

User

* User can create an account.
* User can login.
* User can create a thread and comment on it.
* User can edit their threads.
* User can delete their threads.
* User can comment on threads.
* User can edit their comments.
* User can delete their comments.

Moderator

* Moderator can do everything an User can aside from creating their account.
* Moderator can edit other Users comments and threads.
* Moderator can delete other Users comments and threads.

Admin

* Admin can do everything a Moderator can.
* Admin can delete other Users accounts.
* Admin can grant and remove Moderator role from Users.


#### Restrictions & Missing functionalities

* Commenting doesn't work. It requires to be attatched to a thread, but on creation it's missing the attatchement to the thread.
* User cannot edit their threads
* User cannot delete their threads
* All admin functionalities are missing
* All moderator functionalities are missing



#### SQL

```
CREATE TABLE role (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(10) NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE user_role (
	account_id INTEGER NOT NULL, 
	role_id INTEGER NOT NULL, 
	PRIMARY KEY (account_id, role_id), 
	FOREIGN KEY(account_id) REFERENCES account (id), 
	FOREIGN KEY(role_id) REFERENCES role (id)
);
CREATE TABLE comment (
	id INTEGER NOT NULL, 
	created DATETIME, 
	edited DATETIME, 
	content VARCHAR(8192) NOT NULL, 
	account_id INTEGER NOT NULL, 
	thread_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id), 
	FOREIGN KEY(thread_id) REFERENCES account (id)
);
CREATE TABLE thread (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	title VARCHAR(144) NOT NULL, 
	content VARCHAR(8192) NOT NULL, 
	created DATETIME, 
	account_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id)
);
```

#### Initial plan for database:
![database diagram](https://github.com/sinplosion/msgboard/blob/master/documentation/database_diagram.jpg)