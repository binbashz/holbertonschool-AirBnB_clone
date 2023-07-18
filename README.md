## AirBnB clone - The console




![abnb](https://github.com/binbashz/holbertonschool-AirBnB_clone/assets/124454895/de1041e6-7c3d-41bb-8e5a-1c4272dc9c42)

The AirBnB clone goal of the project is to deploy on your server a simple copy of the AirBnB website. After 4 projects, you will have a complete web application composed by:

* A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
* A website (the front-end) that shows the final product to everybody: static and dynamic
* A database or files that store data (data = objects)
* An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)




## What’s a command interpreter?

We want to be able to manage the objects of our project:

-   Create a new object (ex: a new User or a new Place)
-   Retrieve an object from a file, a database etc…
-   Do operations on objects (count, compute stats, etc…)
-   Update attributes of an object
-   Destroy an object

## [](https://github.com/AngeiraT/holbertonschool-AirBnB_clone#resources)Resources

Read or watch:

-   cmd module
-   packages concept page
-   uuid module
-   datetime
-   unittest module
-   args/kwargs
-   Python test cheatsheet

## [](https://github.com/AngeiraT/holbertonschool-AirBnB_clone#learning-objectives)Learning Objectives

-   How to create a Python package
-   How to create a command interpreter in Python using the `cmd` module
-   What is Unit testing and how to implement it in a large project
-   How to serialize and deserialize a Class
-   How to write and read a JSON file
-   How to manage `datetime`
-   What is an `UUID`
-   What is `*args` and how to use it
-   What is `**kwargs` and how to use it
-   How to handle named arguments in a function

## [](https://github.com/AngeiraT/holbertonschool-AirBnB_clone#execution)Execution

The hbnb command interpreter should work like this in interactive mode:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

But also in non-interactive mode: (like the Shell project in C):

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

All tests should also pass in non-interactive mode: `$ echo "python3 -m unittest discover tests" | bash`



--------------------------------------------------------------------------------------------------------

#### The command interpreter, also known as the console, allows users to interact with classes using several commands.




##### Project Structure
The project follows the following structure:

* console.py: The main entry point of the console application.
* models/: Contains the classes representing AirBnB objects.
* models/base_model.py: Defines the BaseModel class, from which other classes inherit.
* models/state.py: Defines the State class.
* models/place.py: Defines the Place class
* models/city.py: Defines the City class.
* models/review.py: Defines the Review class.
* models/user.py: Defines the User class.
* models/amenity.py: Defines the Amenity class.
* models/engine/: Contains the storage engine for persisting data.
* models/engine/file_storage.py: Implements the FileStorage class for storing data in JSON files.
* tests/: Contains unit tests for the project.

#### How to use it

Run the command interpreter with ./console.py

These commands include 
* `create` for creating and saving new instances, 
* `show` for displaying instance details,
* `destroy` for deleting instances, 
* `all` for listing instances, and
* `update` for modifying instance attributes and saving changes.
The console provides the ability to manage objects, view their information, and perform actions on them, enhancing the functionality and control over the program.

To quit the console, the quit command does just fine. Ctrl+D (EOF) is supported as well.


### Examples
![image](https://github.com/binbashz/holbertonschool-AirBnB_clone/assets/113607320/1d609b93-1931-49ae-8d31-d068a8dd8515)

At first we open the file ´console.py´. Then we show there's no object created previously, so we create a ´User´ and two ´Place´. After that we use the ´all´ command to see that everything is all right and those objects were succesfuly created.
´update´ command is used to add or change something to an object, and in this example we add an email to the ´User´
To finish the example we ´destroy´ a ´Place´, then show all the objects again and finally get out of ´console.py´ executing ´quit´ command.
