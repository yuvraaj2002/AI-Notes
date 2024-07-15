This page is actually dedicated towards understanding everything related to databases from the placement perspective and also from the real world concepts. Currently by the time I am actually starting this to be from the placement perspective but after that with time I will making it from the real world perspective as well.

The main playlist I am following right now is basically this [DBMS Playlist](https://www.youtube.com/playlist?list=PLDzeHZWIZsTpukecmA2p5rhHM14bl2dHU)


- What is the difference between the data and information

	Data can simply be defined as the collection of raw facts and figures, whereas information is just the processed form of data.

	One practical example of this could be let say we are scraping the some website for data analysis, but initially after doing web scraping we will be having everything like HTML tags and other irrelevant content. Now upto this point this will be called as data but once we will parse it properly and remove the irrelevant things from that data, do feature engineering then that processed form will be called information from which we can derive insights.
- What do you mean by database and database management system

	Database is simply collection of data stored electronically on some computer device whereas database management system is a software that acts as an intermediate between the user/application and the database. In short DBMS helps us to perform CRUD operation on the database.
- What are the different databases present ? 

	- Relational database : MySQL, Oracle, PostgreSQL
	- Non relational database : MongoDB
	- Graph database : Neo4j
	- Vector database : Pinecone, Weviate
	- Caching based database : Redis
- What are some points of difference between file system and database management system
- From the broader perspective tell if we already had file system then why we moved to the database management system 
- Is file system completely useless and if not why it is still used till date ? 


### Data Models in DBMS

- What do you mean by Abstraction in DBMS and what are the various layers of abstraction used in context of DBMS?
- What do you mean by database instance, schema ?
	The state of the database at some particular moment is called database instance and schema is used for defining logical structure of the database like what are the entities and how they are related with each other etc. 
- What do you mean by data models and what are the various data models
- What are the various database languages ? 
- In case our application is built using python, JAVA or C++ then how can we communicate with the DBMS to get the things done ? 

	By using database-specific libraries, frameworks, that acts as an interface. Here’s how you can communicate with a DBMS in each of these programming languages:
	- SQLAlchemy for Python
	- JDBC for Java
	- ODBC for C++
- What are the various database architectures ? 

	- Tier 1 : Combines the user interface, application logic, and database on a single system.
	- Tier 2 architecture separates the client-side (UI and application logic) from the server-side (database). Example: Old websites
	- Tier 3 architecture have intermediate application layer between UI (client side) and database (server side). This intermediate layer is added for handling the application logic and data processing part to make everything faster as the application logic code is not running on the client side machine. Example: Modern day website
- What do you mean by entity, what are the types of entities ? 

	Entity is basically a distinct object about which some data could be stored. Example: Student could be an entity as about the student we can store his name, class, course, degree, id etc. Similarly car could also be an entity.
	
	- Strong entity : Entities which can be uniquely identified and can exist independently. Example : Student
	- Weak entity : Entities which are dependent on the strong entities. Example : Course enrollment
- What do you mean by entity relationship model and what are the types of relationship entities can have in ER model? 
- Very light things about the types of attributes ?



