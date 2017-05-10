====================================================================================
I have created this task using Django and Django rest framework

Setup project environment
--------------------------
- run $ pyvenv <your-env-name>
- activate environment using $ source <your-env-name>/bin/activate


Install required packages
------------------------
- keeping your environment activated from the root directory of the project run $ pip install -r requirements/base.txt

Set Environment Variables
------------------------
- cd into feedback_survey folder and from here run $ export DJANGO_SETTINGS_MODULE=‘project.settings.local'

Manually create secrets.json file
---------------------------------


Run the server
---------------
- Now you can run the server from feedback_survey folder $ python manage.py runserver

Create Student with random course allotment by Managemnet Command
---------------
- run python manage.py student_allotment_course

APIs
---------------

**Create a Course**

 - Method : POST
 - URL: http://127.0.0.1:8000/api/v1/courses/
 - headers: Content-Type: application/json
 - request_body:
     ```
     {
        "name": "BTech",
        "course_id": "NB212",
        "university": 1
     }
    `````

**Course List**

 - Method : GET
 - URL : http://127.0.0.1:8000/api/v1/courses/
 - headers : Content-Type: application/json
 - response_body:
       ```
         {
          "meta": {
             "status": 1000,
              "message": "",
              "is_error": false
          },
          "data": [
                  {
                     "name": "Btech",
                     "course_id": "BT1",
                     "university": {
                     "name": "Stanford",
                     "address": ""
                     }
                  },
                  {
                     "name": "BCom",
                     "course_id": "BC1",
                     "university": {
                     "name": "Stanford",
                      "address": ""
                      }
                  },
                  {
                     "name": "BSc",
                     "course_id": "BS1",
                     "university": {
                         "name": "Stanford",
                          "address": ""
                      }
                   }
                  ]
          }       
    `````
