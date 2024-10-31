# E-Learning Platform

This is an E-Learning Platform project built using Python and MySQL designed to manage users and execute queries via a Tkinter-based GUI.

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
python main.py
```

This will launch the main application window where you can log in and access the query execution interface.

## File Structure

### Folder Descriptions

- **`config/`**: Contains scripts for initializing and configuring the database.
- **`queries/`**: Contains SQL files for database schema creation and data population.

### File/Folders Prefixes & Suffixes

- **Files starting with `ui_`**: These files manage the user interface (UI) aspects of the application, such as the login screen and query execution interface.
- **Files ending with `populate_data` are sql files for inserting initial values to the database. the string before the prefix represents the data being populated.
- **Folder starting with `flow_`**: These separate the flows according to roles. These contain two files:
    - An SQL file for the procedures for the role that comes after the `flow_` prefix.
    - A `flow.py` file which takes care of the UI and the application logic for that role.

### Important Files

- **`main.py`**: The entry point to the application. Running this file starts the main application interface.

## Troubleshooting

### `tkinter` Missing
If you encounter an error related to `tkinter` missing, install it as follows:

- **Linux (Debian/Ubuntu)**:
  ```bash
  sudo apt install python3-tk
  ```

- **Linux (Red Hat-based)**:
  ```bash
  sudo yum install python3-tkinter
  ```

- **macOS and Windows**: `tkinter` usually comes pre-installed with Python. Ensure you downloaded Python from [python.org](https://www.python.org/downloads/).


## License

This project is licensed under the MIT License.
