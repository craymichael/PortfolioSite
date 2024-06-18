# Welcome to PortfolioSite
This repository contains the source of my portfolio website, which you can feel free
to explore and use. All files are included, with the exception of database-related
files and `settings.py`. The site is powered by the Django framework and is under
the [GPL-3.0 license](https://opensource.org/licenses/GPL-3.0).

# Installation and Requirements
To install all requirements for this project, view the requirements.txt file for the
packages, which can all be installed via `pip install -r requirements.txt` (you'll
also need Python and Pip, of course).

# Running
For the development server, with the hardened `settings.py`, you will need to run
the server with insecure settings in order to serve static content (unless you set
`DEBUG` to false in `settings.py`:

```shell script
PORTFOLIO_WEBSITE_DJANGO_DEBUG=1 python manage.py runserver --insecure
```

Setting `PORTFOLIO_WEBSITE_DJANGO_DEBUG=1` enables debug mode in `settings.py`.

# Development Notes

Javascript and CSS minimization:

```shell script
sudo npm install uglify-es -g
uglifyjs --compress --mangle -- dark-mode-switch-init.js > dark-mode-switch-init.min.js
```

Before deploying, ensure to update static content:
```shell script
python manage.py collectstatic
```

# Deployment

- firewalld
- certbot (+services)
- apache (https, virtualhost, mod_wsgi [express, python path/home], mod_ssl [+reinstall])
- DNS configuration
- Apache ownership
- pipenv (+--three option)
- ocamlfuse (headless drive mount)
- settings.py and config.py file creation