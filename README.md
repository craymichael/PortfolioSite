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
python manage.py runserver --insecure
```