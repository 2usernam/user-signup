from flask import Flask, request, render_template


app = Flask(__name__)
app.config['DEBUG']=True

@app.route('/')
def user_sign_up():
    return render_template('form.html')



@app.route('/', methods=["POST"])
def validation():

    errors = {
        'username_error': '',
        'password_error': '',
        'verify_error': '',
        'email_error': ''
    }

    # Validate form
    if len(request.form['username']) > 20 or len(request.form['username']) < 3 or " " in request.form['username']:
        errors['username_error'] = render_template('errormessage.html', message="Your input is out of range(3-20) and/or contains a space")

    if len(request.form['password']) > 20 or len(request.form['password']) < 3 or " " in request.form['password']:
        errors['password_error'] = render_template('errormessage.html', message="Your input is out of range(3-20) and/or contains a space") 

    if not (request.form['verify-password'] == request.form['password']):
        errors['verify_error'] = render_template('errormessage.html', message='Passwords do not match')
    
    atcount = 0
    dotcount = 0
    for i in request.form['email']:
        
        if i is '@':
            atcount += 1

        if i is '.':
            dotcount += 1

    if atcount != 1 or dotcount != 1 or len(request.form['email']) <3 or len(request.form['email']) > 20:
            errors['email_error'] = render_template('errormessage.html', message = 'Email address can only have one @ and one . and within range 3-20')        
    

    # if validation did _not_ pass
    # render error messages
    # then put messages in form
    # return form to browser
    form_has_error = False
    for e in errors:
        if len(errors[e]) > 0:
            form_has_error = True

   

    if form_has_error:
        return render_template('form.html', username_error=errors['username_error'],password_error=errors['password_error'],
        verify_error=errors['verify_error'], email_error=errors['email_error'])
    else:
        return render_template('welcome.html', username=request.form['username'])
    # Otherwise, show success page
    
   











app.run()