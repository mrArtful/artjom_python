from flask import Flask, render_template, request

app = Flask(__name__)

# By default, a route only answers to GET requests. 
# To handle form submissions (POST), we must explicitly list the methods.
@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    message = None
    if request.method == 'POST':
        # request.form is a dictionary-like object containing submitted form data.
        # 'username' and 'user_comment' come from the 'name' attribute in the HTML form.
        name = request.form.get('username')
        comment = request.form.get('user_comment')
        
        message = f"Thank you, {name}! Your comment '{comment}' was received."
        print(f"DEBUG: Form submitted - Name: {name}, Comment: {comment}")

    return render_template('form.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
