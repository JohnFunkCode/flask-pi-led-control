from flask import Flask
from flask import render_template
from flask import request
#from library.mocpi import pi_led_contraption as pc
from library.raspi import pi_led_contraption as pc

app = Flask(__name__)
aPC =pc.PiLedContraption()

@app.route('/')
@app.route('/index.html')
def main_page():
    return render_template('index.html')

@app.route('/individual.html',methods=['POST','GET'])
def individual_page():
    if request.method == 'POST':
        led_number=request.form['led-number']
        led_state=request.form['led-state']
        if(led_state == 'on'):
            aPC.led_on(int(led_number))
        else:
            aPC.led_off(int(led_number))
    return render_template('individual.html')

@app.route('/group.html',methods=['POST','GET'])
def group_page():
    if request.method == 'POST':
        print("group got a post")
        print(request.form)

        if "on" == request.form["led1-state"]:
            aPC.led_on(0)
        else:
            aPC.led_off(0)

        if "on" == request.form["led2-state"]:
            aPC.led_on(1)
        else:
            aPC.led_off(1)

        if "on" == request.form["led3-state"]:
            aPC.led_on(2)
        else:
            aPC.led_off(2)

        if "on" == request.form["led4-state"]:
            aPC.led_on(3)
        else:
            aPC.led_off(3)

        if "on" == request.form["led5-state"]:
            aPC.led_on(4)
        else:
            aPC.led_off(4)

        if request.form['led6-state'] == 'on':
            aPC.led_on(5)
        else:
            aPC.led_off(5)

        if request.form['led7-state'] == 'on':
            aPC.led_on(6)
        else:
            aPC.led_off(6)

        if request.form['led8-state'] == 'on':
            aPC.led_on(7)
        else:
            aPC.led_off(7)
    return render_template('group.html')


@app.route('/patterns.html',methods=['POST','GET'])
def patterns_page():
    if request.method == 'POST':
        print("patterns got a post")
        print(request.form)

    if'race-up' in request.form:
        aPC.race_up()
    elif 'race-down' in request.form:
        aPC.race_down()
    elif 'dance' in request.form:
        aPC.dance_randomly()

    return render_template('patterns.html')
