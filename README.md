# Museum_db

Museum_db is a terminal interface application written in Python that interacts with a MySQL database. It allows users to either act as a guest or an employee, utilizing the `mysql-connector-python` package for database connectivity. Employees will need to validate the WiFi password before accessing the MySQL database as a root user.

## Features

- **Guest Mode**: Allows users to explore certain parts of the database with limited privileges.
- **Employee Mode**: Provides employees with full access to manage the museum's database after verifying the MySQL Connector password.

## Prerequisites

Before you begin, make sure you have the following installed:

- **Python 3.x**
- **MySQL Server**
- **MySQL Connector** for Python (`mysql-connector-python`)
- **VSCode** (Visual Studio Code) with the **MySQL extension** installed for database access

## Usage

### Running the Application

To start the program, run the following command in your terminal:

```bash
python museum_db.py
```
## Guest Mode

In guest mode, users will have limited access to explore the museum's database. They can view publicly available data but cannot modify any records.

## Employee Mode

To access employee mode, you will be required to:

1. **Enter your employee credentials.**
2. **Verify the WiFi password** to connect to the MySQL database as the root user. Ensure that the WiFi password provided is usable and allows connection to a MySQL user with the name `root`.

## Connecting via MySQL in VSCode

1. **Install the MySQL extension** in Visual Studio Code.
2. **Set up the database connection** using the MySQL Connector in VSCode to explore and manage the database directly.

## Technologies Used

- **Python:** For the terminal interface.
- **MySQL:** Database to store museum information.
- **MySQL Connector for Python:** To connect Python to MySQL.
- **VSCode MySQL Extension:** For managing the database in VSCode.
