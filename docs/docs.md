# Nickel Family Interactive Chemistry Project — Documentation

Welcome to the documentation for the **Nickel Family Interactive Chemistry Project**. This document provides a technical and conceptual overview of the project, its architecture, usage, and customization guidelines.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Architecture](#architecture)
3. [Frontend](#frontend)
4. [Backend (Flask)](#backend-flask)
5. [Java/JEP Integration](#javajep-integration)
6. [Data Model](#data-model)
7. [Endpoints & Routing](#endpoints--routing)
8. [Development & Build](#development--build)
9. [Testing](#testing)
10. [Customization](#customization)
11. [License](#license)
12. [Credits](#credits)

---

## Project Overview

The Nickel Family Interactive Chemistry Project is a web application designed to make learning about the Group 10 elements of the periodic table (Nickel, Palladium, Platinum, Darmstadtium) engaging and interactive. It features:

- Interactive visualizations of atomic structure and quantum numbers.
- Modular backend with RESTful endpoints.
- Responsive, animated frontend using modern web technologies.
- Optional Java integration via JEP for advanced use cases.

---

## Architecture

The project is structured as a modular Flask application, with a clear separation between backend logic, frontend assets, and data. The main components are:

- **Flask Backend:** Handles routing, API endpoints, and serves HTML templates.
- **Views:** Each element/page has its own view module for maintainability.
- **Static Assets:** JavaScript, CSS, images, and videos for the frontend.
- **Templates:** Jinja2 templates for each page.
- **Java/JEP Layer:** (Optional) Allows the backend to be started and controlled from Java.

**Directory Structure:**

```sh
TrabalhoDeQuimica/
├── app/
│   ├── main.py
│   ├── views/
│   ├── static/
│   └── templates/
├── src/
│   └── Main.java
├── requirements.txt
├── Makefile
└── README.md
```

---

## Frontend

### Technologies

- **Tailwind CSS:** For rapid, responsive UI development.
- **Three.js:** For 3D atomic visualizations.
- **AOS (Animate On Scroll):** For smooth animations.
- **Vanilla JavaScript:** For dynamic content and navigation.

### Features

- **Sidebar Navigation:** Persistent sidebar for switching between elements.
- **Animated Backgrounds:** Video and animated effects for immersion.
- **Dynamic Content:** JavaScript fetches data from the backend and renders it on the fly.
- **Responsive Design:** Works on both desktop and mobile devices.

### Main Files

- `app/static/js/global/jungle.bundle.js`: Main JavaScript bundle for dynamic rendering.
- `app/static/css/global/global.css`: Global styles.
- `app/templates/`: Jinja2 HTML templates for each page.

---

## Backend (Flask)

### Structure

- **`main.py`:** Entry point, app factory, and route configuration.
- **Views:** Each element/page (nickel, palladium, platinum, darmstadtium, about, docs, etc.) has its own module in `app/views/`.
- **Data:** All element data is centralized in `app/views/data/data.py`.

### Key Classes

- **`Config`:** Handles view registration and response formatting (JSON/HTML).
- **`TotalViews`:** (If implemented) Tracks page views.
- **`SetViews`:** (If implemented) Registers all views with the Flask app.
- **`StreamToLogger`:** Redirects stdout/stderr to Python logging for debugging.

### Data Endpoint Example

```python
@app.route('/data/', methods=['POST'])
def data():
    # Receives JSON with 'element' and 'page', returns data dict or error
```

### Running

- **Development:** `python -m app.main`
- **Production:** Use a WSGI server (e.g., Gunicorn) or Java/JEP integration.

---

## Java/JEP Integration

- **Purpose:** Allows starting and controlling the Flask backend from Java, useful for embedding Python logic in Java applications or for advanced deployment scenarios.
- **Main File:** `src/main/java/Main.java`
- **How it Works:**
  - Uses JEP (`jep.SharedInterpreter`) to start the Python interpreter.
  - Configures the Python `sys.path` to include the project root.
  - Imports and calls the Flask app's `start()` method.

**To run via Java:**

```sh
make run
```

---

## Data Model

All element data is stored in the `DataView` class in `app/views/data/data.py`. The structure is:

```python
self.nickel = {
    "pagina1": { ... },
    "pagina2": { ... },
    "pagina3": { ... }
}
# Same for palladium, platinum, darmstadtium
```

- Each element has three pages: general info, electronic configuration, and specific facts.
- The `/data/` endpoint expects `element` (index) and `page` (1-3) in the POST body.

---

## Endpoints & Routing

### Main Endpoints

- `/` — Home page
- `/about/` — About the author
- `/docs/` — Project documentation
- `/nickel/`, `/palladium/`, `/platinum/`, `/darmstadtium/` — Element pages
- `/data/` — POST endpoint for fetching element data (used by frontend JS)

### Example Data Request

```json
POST /data/
{
  "element": 0,
  "page": 2
}
```

Returns a JSON object with the requested data.

---

## Development & Build

### Makefile Commands

- `make venv` — Create Python virtual environment and install dependencies.
- `make js` — Bundle JavaScript with esbuild.
- `make run` — Build and run the Java/JEP backend.
- `make test` — Run tests (if implemented).

### Manual Steps

- To run only the Python backend: `python -m app.main`
- To run with Java/JEP: `make run`

---

## Testing

- Tests can be added to the `tests/` directory.
- The default test script is `tests/tests.sh`, which runs the app in test mode.
- Run tests with: `make test`

---

## Customization

- **Add Elements:** Create a new view in `app/views/` and update `main.py` and `data.py`.
- **Change Styles:** Edit CSS in `app/static/css/`.
- **Update Content:** Edit the dictionaries in `app/views/data/data.py`.
- **Add Pages:** Add new templates and views, then register them in `main.py`.

---

## License

This project is licensed under the [GNU GPL v3](LICENSE.txt).

---

## Credits

### Author

- **Bruno RNS** — Development, design, and documentation.

### Contribuitors

- **[TylorSwift2](https://github.com/TylorSwift2)** — Developed the electronic distribution animation.

### Tecnologies

- Technologies: [Flask](https://flask.palletsprojects.com/), [JEP](https://github.com/ninia/jep), [Tailwind CSS](https://tailwindcss.com/), [Three.js](https://threejs.org/)

---

## Educational Purpose

This project was developed as a chemistry assignment to demonstrate the power of interactive, visual learning for complex scientific concepts.

---

## Repository

[https://github.com/BrunoRNS/elementJungle](https://github.com/BrunoRNS/elementJungle)
