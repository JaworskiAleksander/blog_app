# Info
+ blog - first step to building social network application
+ multi-user behavior

## tech stack
+ css
+ js
+ html
+ python
+ django
+ VS Code with a bunch of plugins

## workflow
+ models
+ forms
+ views
+ urls
+ admin

## log
+ not needed et, as it's all v0.1
+ git commit history is where you'll find complete log of how this app was built

## troubleshooting
+ 'no module module_name' error
	+ pip install module_name
+ how to run server
	+ python manage.py runserver

## Additional info
+ personal project = personal responsibility to find out how to do it
+ code does not lie, what you see here is what I am 100% confident in
	+ everything else is just a matter of RTFM and using google/stack overflow/slack/et c.
+ best practice is to create new conda env for each project
	+ this fits nicely with devops rule of immutability of working environment for each project separately
+ when using CBV, setting up models first will dictate how every other component will be build
	+ you should pay close attention to your initial app design, to m
	+ codebase flexibility should be a built-in feature of your work, as refactoring is the norm
	+ additional BASIC reading on writing readable and flexible code / this is just the tip of an iceberg!
		+ DP GoF - learn design patterns
		+ Head First: Design Patterns - in case you had problems with out-dated examples in GoF
		+ Clean Code by Uncle Bob - learn how to write design patterns clearly
		+ Refactoring by Fowley - learn how to refactor stuff to design patterns
		+ Refactoring by J. Kerievsky - improve your refactoring skills
	+ models are reflected into database sqlite3
+ it's a design to allow only one user to create posts, which is reflected in class Post design
+ timezone settings are specified in settings.py file
+ reverse - after user created new object of that type, where should be they taken then
+ widgets dictionary in forms.py
	+ that's how you connect forms and css styling, using a dictionary
	+ syntax is as follow
		'fieldName' : forms.fieldType(attrs={'class':'className'})
+ once a person is logged in, it gets redirected to home page
+ get_queryset
	+ python version of sql
		published_date__lte - grab a field 'published_date' and filter it ('__') by Less Than or Equal (lte)
		'-' - means we're sorting them in descending, from the greatest value (newest) to the lowest (oldest)


+ how to add empty folders to git ?


WARNINGS:
blog.Post.create_date: (fields.W161) Fixed default value provided.
        HINT: It seems you set a fixed date / time / datetime value as default for this field. This may not be what you want. If you want to have the current date as default, use `django.utils.timezone.now`
