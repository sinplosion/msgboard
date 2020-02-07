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


the heroku index page has a query that for some reason doesn't work on heroku but works on linux

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

Admin

* Admin can do everything an User can aside from creating their account.
* Admin can edit other Users comments and threads.
* Admin can delete other Users comments and threads.
* Admin can delete other Users accounts.


#### Initial plan for database:
![database diagram](https://github.com/sinplosion/msgboard/blob/master/documentation/database_diagram.jpg)
