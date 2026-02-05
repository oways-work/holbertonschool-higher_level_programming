# Python - Server-Side Rendering

## Description
This project explores the concepts of Server-Side Rendering (SSR) using Python and the Flask web framework. Unlike client-side rendering where the browser builds the page, SSR generates full HTML on the server and sends it to the client. This approach improves performance, initial load times, and SEO.

## Learning Objectives
* Understand the difference between SSR and Client-Side Rendering (CSR).
* Implement SSR using Flask and the Jinja2 templating engine.
* Work with various data sources: JSON, CSV, and SQLite.
* Handle dynamic content, loops, and conditional logic in HTML templates.
* Create reusable components with template inheritance and inclusion.

## Technologies Used
* Language: Python 3.x
* Web Framework: Flask
* Templating Engine: Jinja2
* Database: SQLite3
* Data Formats: JSON, CSV

---

## File Overview

| File | Description |
| :--- | :--- |
| task_00_intro.py | Python script to generate personalized invitation files from a template. |
| task_01_jinja.py | Basic Flask application demonstrating routes and rendering templates. |
| task_02_logic.py | Flask app using Jinja loops/conditions to display items from JSON. |
| task_03_files.py | Product display app fetching data from JSON or CSV based on parameters. |
| task_04_db.py | Extended application using SQLite as a data source for products. |
| templates/ | Directory containing all Jinja HTML templates (index, about, contact, etc.). |

---

## Setup and Usage

1. **Install Flask:**
   pip install Flask

2. **Initialize the Database (Task 4):**
   Run the database creation script to generate products.db.

3. **Run an Application:**
   python3 task_04_db.py

4. **Access the Routes:**
   - Home: http://localhost:5000/
   - Items: http://localhost:5000/items
   - Products (JSON): http://localhost:5000/products?source=json
   - Products (SQL): http://localhost:5000/products?source=sql

---

## Author
* Oways - (https://github.com/oways-work)