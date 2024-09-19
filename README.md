# Borrowing System - Django Project

By Team Lainakoodarit

### Team Members

- [Aleksi Helgren](https://github.com/AleksiHel)
- [Saku Karttunen](https://github.com/sakuexe)
- [Wais Atifi](https://github.com/Waisatifi)

## Project description

This was part of web programming with Django course in HAMK UAS by teacher Petri Kuittinen.

The goal was to create fully functional and modern web application with Django. The assignment was to create library like borrowing system where users can loan and return items easily. The admin of the website should likewise be able to manage the application easily with the admin panel.

[Project video showcase](https://www.youtube.com/watch?v=boFScMuRa4A)

## Features

- Easy to use and reactive frontend
- Search feature with parameters such as name, author, genre, language, availability, media format
- Filter products by tags
- Register, log in and user history
- Secure
- Product pages with all relevant information
- Admin interface with tweaks for easy management of the application
- Product creation from the admin panel

## Instructions

You can use the virtual enviroment created for the project.

```bash
pip3 install virtualenv
virtualenv venv
source venv/bin/activate
# venv/venv/activate.bat  -- for windows
# Deactivate the virtual enviroment
deactivate
# add installed pip packages to requirements.txt
pip3 freeze > requirements.txt
```

Or you can install the packages locally to your user with the following

```bash
pip3 install -r requirements.txt
```
-----------------------------------------------------------------
## Full assignment description

_Create web application with Django._

_The web application should be implemented so that it is reasonably secure and it works ok on all the most popular browsers, including both desktop browsers (Chrome, Firefox) and mobile browsers (Android Chrome, iOS Safari). Implement the user interface so that it works with the most popular screen resolutions and does not rely solely on keyboard, mouse or touch screen events, i.e. so that it works both on a touch screen device, e.g. a smartphone, and also on a traditional desktop computer._

_Each of the web applications must include at the following functionality:_

_- login_

_- create new user (not using administration interface)_

_- logout_

#### _Borrowing system_

_The user can browse and search for loanable works. He can see for each work whether the work is on loan or not. You can return your borrowed works. Each work can have one or more authors, name and year of publication. Naturally, one author can be behind several works. The borrowing period can be specified in advance, e.g. 2 weeks. The loan period and the last return time are determined automatically._

_The maintenance user interface should easily reveal which works each user has on loan. Is there possibility to attach tags and images (e.g. cover photo) to borrowed items?_

