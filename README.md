A Brief introduction to Django MTV framework

 
What is MTV (Model, Template, and View)
Django is an open source MTV (model Template view) web framework. To understand MTV, think Model as a Logical data structure. It is the middleware & data handler between database and view. The Model provides a definition of how the data formats as coming from the view so, it stores in the database and vice-versa, i.e., the retrieving information from the database transfers to the view in the displayable format.  
 

Views receive data as well as request method ("POST","GET") from client side and accordingly formats the data via model so that it can be stored in database. It also communicates to the database for retrieving data which transfer to the template for viewing.
Django needs a convenient way to generate HTML dynamically. The most common approach relies on templates. A template contains the static parts of the desired HTML output as well as some special syntax describing how dynamic content will be inserted. Template provides much more extendibility to the frontend developers than what MVC architecture was giving. One template can be used by different views to show various formats of data. It keeps all the content that is rendered by the browser. This part is what is visible to the client side. Model & views reside on the server side. 
 

Working of MTV Architecture
when we request for the website, the interface through which we use to make that request via our browser was the Template. Then that request transmits to the server for the management of view file
  “django-admin startproject projectname” creates a root folder with the project name you provided including all the basic files needed to launch your basic application. Just type “python manage.py runserver” in the terminal to runserver for your application.

projectname/
    manage.py
    projectname/
        __init__.py
        settings.py
        urls.py
        wsgi.py
        views.py
	
Django plays the crucial role of managing HTTP responses and request. So when a template request an update data on the client side, request and data is seen by views on the server side. then it transports to the correct URL. 
The URL mapping in Django is easy to map and attach template with every url.
It is actually done in regular expressions and the arguments for URL are passed in 
path(“url name/”, “function name”, name = “optional”). 
These expressions are much more understandable than IP addresses.

url patterns = [ 
path(““, views.index, name = "home"),	
path("contact/", views.contact, name = "contact"), 
path("about/", views.about, name = "about")]

Suppose “www.yourblog.com” is website’s default url, It will open the home page. When you request to navigate to “contact/” page, path will know how to handle that and you don't to specify it explicitly. In this case the path will return path will have information of the url to that page and you don't to specify it explicitly. in this case the path will return www.yourblog.com/contact.html , it calls views.contact() function defined in views.py. This function render the HTML template page for this URL path which then will be displayed on the client side. You can set a name for this url pattern, its optional but I recommend you to name each path, because for complex websites with multiple pages, the url patterns can become really messy real quick. 
For reference: https://docs.djangoproject.com/en/2.2/ref/urls/
 Now after the sending of a request to the correct URL, the app logic applies and the model initiates to correct response to the given request. Then that particular response is sent back to the View where it again examines the response and transmits it as an HTTP response or desired user format. Then, it again renders by the browser via Templates, one of the important components of Django MTV architecture. 

An easier real-life working of above functioning would be –
When you login in a website (Django based), you open the login page. It again happens without the need of the Model. It is because Views will process the request and send it to the URL of the login page. Then, it will be a response by the server, from there to the browser.
After that, you enter your credentials in the given Template, HTML form. From there the data is again sent to the view, this time this request rectifies and the model is given data. Then the Model reads and verifies the data that the user provides within the connected database.
If the user data matches it will send the relevant user data like profile image, name and (other things depending on the type of website) to the Views. It will then format the same in desired response and will transmit the same to the client.
Otherwise, the Model will send a negative result to the Views. In turn, it will rout it to the login page again alongside an error message.
That’s how the Django MTV architecture is actually working.


