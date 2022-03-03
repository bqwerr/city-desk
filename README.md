# city-desk
This is a simple project created to learn Django

# Functionalities
- Citizen can raise Compliants, NOC Requests, Appointment Requests
- Police can view latest requests in the dashboard
- Custom User model has been implemented for citizen
- Decorators are used for role based views
- Used django built-in authentication system for login, logout, sign-up and password reset

# Installation
Clone the repository and follow below steps...

```sh
cd city-desk
virtualenv ENV
ENV\Scripts\activate
pip install -r requirements.txt
py manage.py makemigrations
py manage.py migrate
py manage.py runserver
```
