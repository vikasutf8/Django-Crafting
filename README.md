# Django Framework

we create virtual evn. `﻿py3 -m venv .venv` 

`pip3 i uv. ` 

`﻿uv venv`  its create .venv folder

To activate env. --`﻿source .venv/bin/activaate`   for decativte `﻿deactivate` 

--backend part or dynamic website work on python django.

--MVC. -model view controllers

--MVT -model view template (controlller with view, view with templates)

why i choose. -- fast,components,Security,Scalability

-- install django uv pip install Django 

 `﻿django-admin startproject "projectname"`  iths create folder of projectname -->folder projectname & manag.py

`cd projectname --> python manage.py runserver 8000  bydefualt` 

as init -- manage.py is first file that render on deployment

By default its connect ot sqlite database..in folder setting.py define all env variables 

url.py -->routes define
view.py -->controller define 
model.py also 
--- 
### Flow of django always same
story of templates ::

root follder me --manage.py ke paralle me

- folder templates. --all html
- folder static -- allcss
- template engine --meant kahi par bhi enjact kar sakte ha code ko
- adding template as html and css file must config then setting.py as differenct path and load static


### Jinja2 -- defualt templating engine
varibale. {{---}}

cref toke. {%--- %}

-- app created by manage.py and server start also..

`﻿python manage.py startapp "appname"` 

now main project/root must have to know that new app present their.



### How to use tailwind in django..
`﻿uv pip install django-tailwind` 

-- If you want to use automatic page reloads during development  use the `[reload]` extras, which installs the `django-browser-reload` package in addition:  `python -m pip install 'django-tailwind[reload]'` 



**we have to face use so download pip as cmd given**

`﻿python -m ensurepip --upgrade` 

`﻿python -m pip install -- upgrade pip`  any one is validate

--Adding app 'tailwind'  in setting.py

--`python manage.py tailwind init` 

--by defualt theme app created so we have to add it in setting.py

```
TAILWIND_APP_NAME='theme'
INTERNAL_IPS =['127.0.0.1']

//later
NPM_BIN_PATH='' //how to find new terminal 'where npm'
```
[﻿chaicode.com/blogs/how-to-add-tailwind-to-your-django-project-and-django-admin](https://chaicode.com/blogs/how-to-add-tailwind-to-your-django-project-and-django-admin) 

[﻿django-tailwind.readthedocs.io/en/latest/installation.html](https://django-tailwind.readthedocs.io/en/latest/installation.html)   it is good 

### Admin panel :
higly configuer and old school like.. customizable and directly talk to model with CRUD functionlaity access..

_You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
January 02, 2025 - 09:14:07_

migration ::we can direcly connect to db , on behave of own djangoORM is used for that cmd for access of admin panel

`python manage.py migrate` 

createing superuser

`python manage.py createsuperuser` 

if reset admin password ::`python manage.py changepassord` 

### Django Modeling :::
django --image handling --db perfomance issues little bit

-- model.py always created in apps not in project.. like as microservice apps

--we can write model directly in model.py in chais app -- how and why 

-- database also changes as engine/ else  setting.py ,we cant change code .. **django ORM layer** is major interaction

```
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', 
        #all changes here form converting sqlite to postgreSQL
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
How models written in Django

Handling Pillow herer -- uv pip install Pillow

-- we want to put image in project at any app.. so  setting .py me fixed:

```
MEDIA_URL ='/media/'
MEDIA_ROOT =os.path.join(BASE_DIR,'media')
```
End of the days urls.py sureve hoga so urls  ko pata hona chaiye ki images storge hogi or setting me change huao ha .. **main project me urls.py**

`from django.conf import settings
from django.conf.urls.static import static` 

jo ye static method ha use batana hota ha ki setting.py me se media_url load karna ha

urlpattern[] static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT) 

-- Still django project doesn't know about we wrote a model so we have to till manage.py

**Migrations :: loading changes:**

`﻿python manage.py makemigration appnamethatwork(chais)`  -- its create new folder in that it wrote SQL Queries of table that we created... **Important we dont write query ..it automatically created by Django.**

`﻿python manage.py migrate`  it aviable as table

**AB kisi bhi Model ko admin se attach kar sakte ha ..view their ..**

admin.py in chais ..and theri app :;

`﻿from django.contrib import admin
from .models import ChaiVarity
# Register your models here.
admin.site.register(ChaiVarity)` 

By defualt User table is already present in Django:so how to utilize it ?



### Relationships:
- one to one
- one to many --Forigen Key
what is CASCADE in DB ??
- many to many 

### Form:
- adding a form templates.
- for adding forms using views  define a functions ->then adding urls also with name,
- Goal -- on going form getting a dropdown ,getting all chai veritys ,after selection it relative all store got that specific chai available..
using  Chai varitys ,Stores model interactions.
1. create **form.py** -- documations
- always create a  class
- existing model ke aander query karna. --`﻿forms.ModelChoiceField(queryset =ChaiVaritys.object.all()`
it give a dropdown bydefulat .. CharField--char deta bydefualt
2. views 
- form having 3 field -always check
    - form shows
    - user filled  form and submit it then how to handling  if condition handling with Method --put ws templeta rendering **csrf-token** used here --it django middleware querys
        - form having 3 field -always check
            - form shows
            - user filled form and submit it then how to handling if condition handling with Method --put querys
            - just create a form that user that fill that else case ` form =chaiVarityform()`  
    - just create a form that user that fill that   else case  `﻿form =chaiVarityform()` 
3. templeta rendering **csrf-token** used here --it django middleware 
 



