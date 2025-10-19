Project Overview

This repository contains the solutions for Homework 04, focusing on advanced Python topics: command-line interface (CLI) development, file I/O operations, error handling, and object-oriented path manipulation.

## Repository Structure and Functionality

| File | Function/Feature | Description |
| :--- | :--- | :--- |
| `task_1_total_salary.py` | `total_salary(path)` | Reads a file with developer salaries and returns the total and average salary, handling `FileNotFoundError` gracefully. |
| `task_2_cats_info.py` | `get_cats_info(path)` | Reads a file with cat data (ID, name, age) and returns a list of dictionaries, handling file errors and incorrect line formats. |
| `task_3_visualize_dir.py` | `visualize_structure(path)` | **CLI Script:** Accepts a directory path as an argument and recursively visualizes its structure with color-coded (colorama) files and directories. |
| `task_4_assistant_bot.py` | `main()` / Handlers | **CLI Assistant Bot:** Implements a cycle to process commands (`hello`, `add`, `change`, `phone`, `all`, `close/exit`) using a dictionary for contact storage. |