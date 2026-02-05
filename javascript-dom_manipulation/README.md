**JavaScript DOM Manipulation**

Description
This repository contains small example scripts that demonstrate common DOM manipulation techniques using modern JavaScript (ES6). Each script is self-contained and intended to be loaded into a simple HTML page to observe the behavior in the browser.

Learning objectives
- Select elements using `querySelector` and `getElementById`
- Handle user events with `addEventListener`
- Modify element classes and inline styles
- Update element content with `textContent` and `innerHTML`
- Create and append new DOM elements
- Use the `fetch` API to request and display data from remote services

Technologies
- Language: JavaScript (ES6)
- APIs used: SWAPI (Star Wars API), Hello Salut API
- Environment: Web browser (tested on Chrome 78+)

Project files
- `0-script.js`: Sets the `<header>` text color to red.
- `1-script.js`: Changes the header color to red when the element with id `red_header` is clicked.
- `2-script.js`: Adds the `.red` class to the header on click.
- `3-script.js`: Toggles between `.red` and `.green` classes on click.
- `4-script.js`: Appends a new `<li>` element to a list each click.
- `5-script.js`: Updates the header text to "New Header!!!".
- `6-script.js`: Fetches a character name from SWAPI and displays it in the page.
- `7-script.js`: Fetches and lists movie titles from SWAPI.
- `8-script.js`: Fetches a "Hello" translation from Hello Salut API based on a selected language.

Requirements
- Use modern Chrome (78+) or any up-to-date browser.
- Follow semistandard rules for JavaScript style.
- Avoid `var`; use `const` and `let` only.

Setup & usage
1. Clone this repository.
2. Open the provided HTML file for the example you want to run (or serve the folder from a local web server).

Quick local server (recommended to avoid CORS issues):
```bash
python3 -m http.server 8000
# then open http://localhost:8000/javascript-dom_manipulation/<your_html_file>.html
```

Include the script you want to test in the HTML (example):
```html
<script src="0-script.js"></script>
```

Author
Your OWAYS-WORK

Next steps
- Add small HTML examples demonstrating each script (if not present).
- Add automated linting or a `package.json` with lint scripts for semistandard.
