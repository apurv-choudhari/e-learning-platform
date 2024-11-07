# E-Learning Platform

This is an E-Learning Platform project built using Python and MySQL designed to manage users and execute queries.

## Note for devs
Please check the README before starting out. If there's anything in progress or needs to be done, just search `TODO` in the codebase. That section indicates incomplete/in-progress work.

## Prerequisites

1. **Python Installation**:
   - Ensure you have Python 3 installed. If Python is not installed, follow the steps below:
     - **Windows**: Download the installer from [python.org](https://www.python.org/downloads/) and run it. During installation, check the box that says "Add Python to PATH."
     - **macOS**: Install Python via [Homebrew](https://brew.sh/) (if you use it) by running:
       ```bash
       brew install python
       ```
     - **Linux**: Install Python via your package manager. For Debian/Ubuntu-based distributions:
       ```bash
       sudo apt update
       sudo apt install python3 python3-pip
       ```

2. **Clone the Repository**:
   ```bash
   git clone https://github.com/apurv-choudhari/e-learning-platform.git
   cd e-learning-platform

## Installation

### Set up a Virtual Environment (optional but recommended):

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### Install Dependencies

Install all necessary dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Running the Application

To start the application, change working directory to src and run the following command:

```bash
cd src
python app.py
```

This will launch the main application window where you can log in and access the query execution interface.

## File Structure

- **README.md:** The project documentation, explaining the purpose, usage, and structure of the project.

- **requirements.txt:** Lists all Python packages and dependencies required for the project. Install with pip install -r requirements.txt.

- **flow/:** Houses role-specific program flows for different user types, including admin, faculty, student, and TA flows. Each file implements workflows and logic tailored to the corresponding user role.

- **sql/:** This directory holds SQL scripts for managing the database:
  - db_setup.sql and populate_data.sql are for initial database schema creation and data population. Other SQL files define procedures and role-specific SQL commands for each type of user (e.g., admin.sql, faculty.sql).

- **src/:** Contains the main Python source files, including:
  - app.py: Main application entry script, which orchestrates other modules.
  - main.py: Core functions and high-level program logic.
  - db_utils.py: Helper functions for database operations, such as table creation, data population, and deletion.

### Important Files

- **`main.py`**: The entry point to the application. Running this file starts the main application interface.

## License

This project is licensed under the MIT License.
