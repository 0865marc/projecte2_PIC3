# Project 2 - Programming and comunication III

In this task, i developed a simple Web Application to be able to monitor a 3D printer farm using FastAPI.


# Main page

This page contains the last value registered in the database for each printer. Every printer will have it's own table, with it's ID in the header, followed by the Date, Time, Temperature, Humidity and Status.

# Historic data

This page is similar to the main page in the way that every printer has it's own table, but, in this particular case, instead of showing only the last values, it's organized in rows containing all the historic reads.

# Files
- ## main_py

This is the main script, this is where we execute our server, listen to request, render the templates, comunicate with the database, etc..
To run the server:
> py main.py
> 
- ## printers_py
This script is used in order to simulate n number of printers, sending random data every 20s. You have to execute this script in order to make the web app more dynamic.
> py printers.py

- ## printer_log_py
This is the class that represents a log by a given printer. This class is used in the other two files in order to be able to connect and send instances to the database. You do not have to execute.
