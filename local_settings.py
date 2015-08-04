DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "72f1e044-76d9-4c8b-94c4-938c7326883a349a3baa-9cef-431a-91eb-394db13f721c628e9645-0b5b-40eb-bea9-9967d03766cd"
NEVERCACHE_KEY = "da5c4960-b87f-43dc-ae68-031da35ca9197ff89720-d18a-454b-b640-e3f2c5c44f0d5b683953-cc2f-40da-b3ba-0f97373133a8"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}
