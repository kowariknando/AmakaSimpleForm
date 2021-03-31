# AmakaSimpleForm
Project of automate a simple form website. Task requested by Amaka as part of the interview process

Website with the simple form: https://single-form.vercel.app/


Tests are written in Python 3.8 using the libraries Pytest and Selenium and also Pytest-html to generate the HTML reports.

The list of tests with all the description can be found in the following excel file: https://docs.google.com/spreadsheets/d/1z-icdzNzD_i6xkIJlJM1gPT4JXBz99ndwZWVne1OPJg/edit?usp=sharing


The tests must be execute through the terminal using the command "pytest -v -s nameofthetest.py"

To generate a report and run multiple tests you must navigate through the terminal to the directory where the package with the test is located and execute the following comand:

pytest -v -s --html=C:\Users\kowar\PycharmProjects\AmakaSimpleForm\reports\TESTdemo.html --self-contained-html C:\Users\kowar\PycharmProjects\AmakaSimpleForm\TestNamePackage

Note that C:\Users\kowar\PycharmProjects\AmakaSimpleForm\reports\TESTdemo.html is the directory were you would like to save the html report and "TESTdemo.html" the name of the report.
Note also that C:\Users\kowar\PycharmProjects\AmakaSimpleForm\TestNamePackage is the directory where you should have saved the package with all the test python files, on this example the TestNamePackage which includes the tests related for the name field.


You will find each package with all the tests for each field from the form (Name, Surname, Phone, Website and Age). 
Also a separate file called data.py where are all the XPATHs used on the tests, so in case any location is change we will have to modify just the data.py file.
