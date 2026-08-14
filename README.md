# IRONCORE Fitness — Django Frontend Website

A complete, professional, modern fitness website built with **Django templates**
for routing/rendering only — no database, no models, no authentication, no APIs.
All "backend" logic is pure Django view functions that render HTML templates.

## Tech Stack
- Django (URL routing + template rendering only)
- HTML5 / CSS3 / Vanilla JavaScript
- Bootstrap 5 (CDN)
- Font Awesome 6 (CDN)
- Google Fonts — Poppins + Bebas Neue (CDN)
- AOS — Animate On Scroll (CDN)

## Project Structure
```
fitness_website/
├── manage.py
├── requirements.txt
├── fitness_website/          # Project config
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── fitness/                  # App
    ├── views.py               # Renders templates only
    ├── urls.py                # All page routes
    ├── data.py                # Static demo content (NOT a database)
    ├── templates/fitness/
    │   ├── base.html
    │   ├── includes/
    │   │   ├── navbar.html
    │   │   └── footer.html
    │   └── *.html              # All 18 pages
    └── static/fitness/
        ├── css/style.css
        ├── js/main.js           # Global site features
        ├── js/bmi.js            # BMI calculator logic
        ├── js/calorie.js        # Calorie calculator logic
        ├── js/timer.js          # Workout timer logic
        ├── images/
        └── icons/
```

## Pages Included
Home · About · Services · Workout Plans · Diet Plans · Trainers ·
BMI Calculator · Calorie Calculator · Workout Timer · Gallery ·
Pricing · Testimonials · FAQ · Blog · Contact · Login (UI) ·
Register (UI) · Custom 404

## Step-by-Step: Run in VS Code

1. **Open the folder**
   - Extract/copy the `fitness_website` folder anywhere on your machine.
   - Open VS Code → `File > Open Folder` → select `fitness_website`.

2. **Open a terminal in VS Code**
   - Menu: `Terminal > New Terminal`.

3. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   ```
   Activate it:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`

4. **Install Django**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```
   (No `migrate` needed — this project uses no database.)

6. **Open the site**
   - Visit **http://127.0.0.1:8000/** in your browser.
   - Try an invalid URL (e.g. `/random-page/`) to see the custom 404 page.

7. **Recommended VS Code extensions**
   - Python (Microsoft)
   - Django (by Baptiste Darthenay) — for template syntax highlighting

## Notes
- No `python manage.py migrate` is required — `DATABASES` uses Django's
  built-in dummy backend purely to satisfy internal framework checks;
  no models or queries exist anywhere in the project.
- All page content (trainers, plans, blog posts, testimonials, etc.) lives
  in `fitness/data.py` as plain Python lists/dicts — edit this file to
  change site content without touching templates.
- All images are loaded from Unsplash CDN URLs for demo purposes. Replace
  them with your own images in `fitness/static/fitness/images/` and update
  the `img` paths in `fitness/data.py` / templates as needed.
- Dark/Light mode preference is saved in the browser's `localStorage`.
