# IMDB Movie Scraper

This project demonstrates an implementation of a web scraper that fetches movie data from the IMDB top movies chart and 
writes the results to a CSV file. The project adheres to the SOLID principles to improve code maintainability,
extensibility, and readability.

## SOLID Principles

### Single Responsibility Principle (SRP)

- The `Movie` class is responsible only for storing movie information and does not handle any other responsibilities 
fetching or writing data.
- The `main` function is responsible for orchestrating the fetching and writing of movies, keeping the code modular and
easier to maintain.

### Open/Closed Principle (OCP)

- The `IMDBMovieFetcher` and `CSVMovieWriter` classes implement their respective abstract base classes (`MovieFetcher` 
and `MovieWriter`) and can be extended or replaced without modifying the rest of the code.

### Liskov Substitution Principle (LSP)

- The `MovieFetcher` and `MovieWriter` abstract base classes define common interfaces for fetching and writing movies, 
ensuring that derived classes can be used interchangeably without affecting the correctness of the program.

### Interface Segregation Principle (ISP)

- The `MovieFetcher` and `MovieWriter` abstract base classes define minimal and specific interfaces, making it easier
for concrete classes to implement them without being forced to depend on methods they do not need.

### Dependency Inversion Principle (DIP)

- The `IMDBMovieFetcher` and `CSVMovieWriter` classes implement the `MovieFetcher` and `MovieWriter` interfaces, 
decoupling the high-level `main` function from the details of fetching and writing movies. This makes it easier to
swap out these classes for alternative implementations if needed.

# Building project locally
Install VirtualEnvironment (one time)

    >python -m pip install virtualenv

Create virtual environment

    >virtualenv virtual_project

1. This will create a virtual environment project folder and install python there.
2. This step can be skipped if you already have the folder locally.

Open virtual environment (Unix type OS)

    >source virtual_project/bin/activate

1. This will activate the virtual environment.  Yous should see `(virtual_project)` to the left of the terminal prompt.
2. This step will be needed each time.

Install requirements
    
    >python -m pip install -r requirements.txt

Install local src/ folder

    >python -m pip install -e src 
