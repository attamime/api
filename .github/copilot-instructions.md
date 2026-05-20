**Project Overview**

- **Type**: Django web app (single project `finaltest`, app `mazen`).
- **Entry points**: `manage.py` for CLI, `finaltest/settings.py` for configuration, `finaltest/urls.py` includes `mazen.urls` under `mazen/`.

**Key Files**

- `finaltest/settings.py`: uses SQLite (`db.sqlite3`), `TEMPLATES['DIRS']` points to `templates/`, `INSTALLED_APPS` includes `mazen`.
- `manage.py`: standard Django management entry (use `python manage.py <command>`).
- `mazen/models.py`: contains `student` model (note: class is lowercase `student`, not `Student` — search-and-fix when refactoring).
- `mazen/views.py`: CRUD views for `student` objects; `register` uses `UserCreationForm`, `login_view` is incomplete and requires implementation.
- `mazen/urls.py`: routes `'' -> home`, `edit/<int:id>/`, `delete/<int:id>/`.
- Templates: `mazen/templates/homee/home.html`, `mazen/templates/homee/edit.html`, and shared `templates/base.html`.

**Project-specific conventions & patterns**

- Templates are stored both in the project-level `templates/` (configured in `TEMPLATES['DIRS']`) and inside `mazen/templates/`.
- Views use function-based views and `get_object_or_404` for lookups — follow this pattern for new simple CRUD endpoints.
- URL names: use the `name=` values from `mazen/urls.py` (e.g. `home`, `edit`, `delete`) for redirects and `{% url %}` template tags.
- Model naming is non-standard: `student` (lowercase). Be conservative when renaming: update migrations and imports.

**Developer workflows (commands you will need)**

- Activate virtualenv (example used by repo owner): `source /Users/rais/vnn/bin/activate`.
- Install dependencies (if a `requirements.txt` is added): `pip install -r requirements.txt`.
- Create/Apply migrations: `python manage.py makemigrations` (if models change) then `python manage.py migrate`.
- Run server locally: `python manage.py runserver`.
- Create admin user: `python manage.py createsuperuser`.

**Things AI agents should watch for / avoid changing automatically**

- Do not assume conventional class names; `student` is used throughout — renaming requires coordinated migration updates.
- `login_view` in `mazen/views.py` is incomplete and currently no `register.html` template exists — avoid auto-generating auth templates without user confirmation.
- `DEBUG = True` in `settings.py`: it's fine for local dev; do not flip to `False` or alter secret key without an explicit task.

**Suggested small tasks examples (for PRs)**

- Complete `login_view` to use `AuthenticationForm` and `login()`; add a `templates/register.html` and `templates/login.html` when implementing auth flows.
- Add tests in `mazen/tests.py` for the `home`, `edit`, and `delete` views (use Django's test client to post form data and assert redirects).
- Standardize model class name to `Student` only if you also update `migrations/` and run the necessary migration operations.

**Where to look for more context**

- Start at `finaltest/settings.py` → `finaltest/urls.py` → `mazen/urls.py` → `mazen/views.py` → `mazen/templates/` to follow data flow from URL to view to template.

If anything here is unclear or you want me to expand a section (for example: add example PR text for renaming the model, or implement `login_view` and templates), tell me which piece to iterate on.
