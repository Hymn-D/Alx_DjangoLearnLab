# LibraryProject
# Django Custom Permissions Setup

## Custom Permissions

Defined in `Article` model:

- `can_view` – Can view articles
- `can_create` – Can create articles
- `can_edit` – Can edit articles
- `can_delete` – Can delete articles

## Groups and Permissions

- **Viewers**: `can_view`
- **Editors**: `can_view`, `can_create`, `can_edit`
- **Admins**: All permissions

## Setup Instructions

1. Run migrations to apply model changes:python manage.py makemigrations
python manage.py migrate


2. Use Django Admin to assign users to groups.

## Notes

Views are protected using `@permission_required`. Users without appropriate permissions will receive a 403 Forbidden error.


## Content Security Policy (CSP)

To mitigate XSS risks, CSP headers were implemented using the `django-csp` middleware.

### Configuration:
- `CSP_DEFAULT_SRC`: `'self'`
- `CSP_SCRIPT_SRC`: `'self'`, `https://trusted.cdn.com`
- `CSP_STYLE_SRC`: `'self'`, `https://fonts.googleapis.com`

### Middleware:
Added `csp.middleware.CSPMiddleware` to `MIDDLEWARE` in `settings.py`.

### Notes:
All external resources used in templates are whitelisted explicitly.
