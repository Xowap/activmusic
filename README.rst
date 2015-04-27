ActivKonnect Django Template
============================

This Django template is the standard template for ActiveKonnect's Django apps. It fits the basic
needs we usually face:

- Modular settings (dev/prod distinction, environment-based)
- Users signup/login
- Custom user model
- Bower dependencies
- JS/LESS compilation/minification
- Thumbnails
- Automatic Bootstrap forms
- Google Analytics
- Amazon S3 storage
- Sentry integration

It is tailored for Python 3, HTTPS servers and Gunicorn.

Configuration organization
--------------------------

You can find the configuration in `project_name/settings`. There is two configuration file you can
use as `DJANGO_SETTINGS_MODULE`: `dev.py` and `prod.py`. They both hold prod- or dev-specific
configuration.

Otherwise, most of the things happen in `common.py`, or other files for specific areas (bower,
auth, etc).

Dependencies management
-----------------------

Dependencies are handled in three separate files

:reqs/common.txt: prod/dev common dependencies
:reqs/dev.txt: dev-only dependencies
:reqs/prod.txt: prod-only dependencies

Additionally, `requirements.txt` is an alias for `reqs/prod.txt`.

Environment variables
---------------------

:SECRET_KEY: *(mandatory)* Django's secret key
:DATABASE_URL: *(mandatory)* URL to the database in the form `postgresql://user:pass@host/base`
:GOOGLE_ANALYTICS_UID: *(optional)* Google Analytics tracking UID
:AWS_ACCESS_KEY_ID: *(mandatory in prod)* AWS Access Key ID
:AWS_SECRET_ACCESS_KEY: *(mandatory in prod)* AWS Secret Key
:AWS_STORAGE_BUCKET_NAME: *(mandatory in prod)* AWS Bucket Name
:AWS_S3_CUSTOM_DOMAIN: *(mandatory in prod)* Domain at which you can find the files, a.k.a CDN's
                       domain
:SENTRY_DSN: *(optional)* Sentry DSN for errors logging

Users signup/login
------------------

This is handled by `Django Allauth <http://django-allauth.readthedocs.org/en/latest/>`_. A basic
integration is provided, though templates should be customized. They are provided in the
`project_name/apps/register/templates` folder.

Please refer to `project_name.apps.register.allauth_adapter.AccountAdapter` or
`project_name.apps.register.allauth_adapter.SocialAccountAdapter` to alter Allauth's behaviour. You
can refer to the documentation for more information.

Authentication in general rule is configured in `project_name/settings/auth.py`.

Custom user model
-----------------

The provided user model includes a minimal set of fields that can be extended. The main benefit from
the standard user is that there is no username field, which is easier to handle if you do social
authentication, by example. The user is then authenticated by email only.

It includes a custom manager, that allows such a username-less user to exist and integrate well with
Django's tools (like `createsuperuser`).

Bower dependencies
------------------

You can list a set of dependencies in `project_name/settings/bower.py`. Then install them with
`manage.py bower_install`.

JS/LESS compilation
-------------------

All of that is handled by `Django Pipeline <http://django-pipeline.readthedocs.org/en/latest/>`_.
However its default LESS compiler is shitty, and has been replaced with
`a custom one <https://github.com/Xowap/pylesswrap>`_.

You can configure Pipeline in the file `project_name/settings/pipeline.py`.

Thumbnails
----------

Thumbnail support is provided thanks to
`Sorl Thumbnails <https://sorl-thumbnail.readthedocs.org/en/latest/>`_, using the Pillow backend.

Automatic Bootstrap Forms
-------------------------

Bootstrap forms are generated thanks to
`Crispy Forms <http://django-crispy-forms.readthedocs.org/en/latest/index.html>`_. Take a look to
`project_name.apps.register.forms.UserSignupForm` for a working example.

Google Analytics
----------------

`Metron <http://metron.readthedocs.org/en/latest/>`_ handles this, and provides a `analytics`
template tag that is present in `base.html`. It is the stock Google Analytics code, but it can be
customized if needed.

Amazon S3 Storage
-----------------

The storage is `s3boto <https://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html>`_
stolen from `Django Storages <https://django-storages.readthedocs.org/en/latest/>`_. Django Storages
does not support Python 3, however the s3boto module was easy to port, and was vendored in the
template waiting for the PR to be merged.
