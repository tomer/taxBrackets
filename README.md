# Tax Brackets example

This repository provides an example code for tax brackets with five levels: 
* 0    - 3000 with 0% tax
* 3001 - 5000 with 10% tax
* 5001 - 8000 with 20% tax
* 8001 - 10,000 with 30% tax
* 10,001 and above with 40% tax

The repository contains Python code, as well as a sample test file. The code can run interactively or as a test suite (pytest).


# Installation
Project should be bootstrapped using `pipenv`, but it is completely optional, as the only external dependency is `pytest` at the moment. 

A **Visual Studio Code** workspace is included, which will configure the workspace with the tests.

# Usage
The code can run in interactive mode by executing the main file or as a module that can be imported.

# Example
```bash
$ pipenv run ./taxes.py
Please enter salary: 8500
DEBUG:    0 -  3000   0% => 0.0
DEBUG: 3000 -  5000  10% => 200.0
DEBUG: 5000 -  8000  20% => 600.0
DEBUG: 8000 - 10000  30% => 150.0
You should pay 950.0 in tax.
```
