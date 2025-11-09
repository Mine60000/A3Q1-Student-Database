# A3Q1-Student-Database

## INSTALLING REQUIRED LIBRARIES:
	python pip install --upgrade pip           
	python pip install "psycopg[binary,pool]"

## DATABASE SET UP
Part 1: Creating the "Student Database" Database

Launch pgAdmin.

The Postgres Server must be a localhost on port 5432.

In the browser panel on the left, right-click on Databases and select Create > Database.

Name the new database "Student Database" and click Save.

Part 2: Running the SQL Script

In pgAdmin, select the newly created University database by clicking on it.

Open the Query Tool by right-clicking on University and selecting Query Tool.

Click on the Open File icon (looks like a folder) in the toolbar.

Navigate to the Scripts folder and open schema.sql.

The content of schema.sql should now be displayed in the query editor.

Click on the Run button (a green triangle) to execute the SQL commands.

Part 3: Initial Data

Click on the Open File icon (looks like a folder) in the toolbar.

Navigate to the initData.sql file and open it.

The content of initData.sql should now be displayed in the query editor.

Click on the Run button (a green triangle) to execute the SQL commands.

## RUNNING THE APLICATION
Open a command prompt in the extracted folder and run:
python A3Q1.py

It will then prompt you for a user name and password use the ones associated with the super user.

## VIDEO OVERVIEW
https://youtu.be/-XLfLVnxZr8