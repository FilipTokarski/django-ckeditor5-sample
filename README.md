# CKEditor 5 Classic build sample in Django
Adding CKeditor 5 to Django app is very simple - you can just load it into your template as a static asset. In this example, you can find a separate app called `editor`, which uses CKEditor 5 build created with [Online Builder](https://ckeditor.com/ckeditor-5/online-builder/).  
If you would like to use your static assets in production, please refer to Django docs on [deploying static files](https://docs.djangoproject.com/en/3.1/howto/static-files/deployment/).

      
## Installation
Provided that you are familliar with installing Python, creating virtual environments and installing packages with `pip` now you need to:  
- install packages listed in `requirements.txt`:  
`pip install -r requirements.txt`
  
- `cd ck_app`
  
- add your `SECRET_KEY` in `ck_app/settings.py`
  
- run `python manage.py makemigrations`
  
- run `python manage.py migrate`
  
- run `python manage.py runserver`
  
- go to `localhost:8000/editor` and enjoy
  
## Using CKEditor 5
This sample uses [classic editor build](https://ckeditor.com/docs/ckeditor5/latest/examples/builds/classic-editor.html). The template is located in `editor/templates/editor.html`. You can also change the toolbar configuration there. If you want to use another type or customize the editor, you'll need to create and build it first. You can find those information in CKEditor docs on [installing plugins](https://ckeditor.com/docs/ckeditor5/latest/builds/guides/integration/installing-plugins.html) and [creating custom builds](https://ckeditor.com/docs/ckeditor5/latest/builds/guides/development/custom-builds.html). You can also ( like in this sample ) get your custom editor from [Online Builder](https://ckeditor.com/ckeditor-5/online-builder/). When youre done with customizing the editor, just use it in your Django app as a static asset in `editor/static/editor/`.  