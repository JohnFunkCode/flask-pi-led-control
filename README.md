# flask-pi-led-control
Simple Flask app to control LEDs on a Raspberry Pi

At this stage we have setup the basics of the flask UI components.  This includes the following tasks:
- Setup a base flask app by copying the structure of our previous flask examples
    - Setup a libraries directory for our code and templates
    - create a driver app called run_app.py in the root of the project
    - added requirements.txt to make sure the environment include Flask
- Moved the static html into the templates directory
- Create a file called flask_pi_led_controll_app.py with all the routes for the app.
- Moved the stylesheet into /library/static/styles and changed all the html files to refer to it.

### Final Step
As the final step we'll add our class that represents our Raspberry Pi LED contraption and wire it up to the flask application.  

To make things easier to test outside the Raspberry Pi, we simply copied our contraption class to create a mock interface and ripped out anything to do with GPIO processing.