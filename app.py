from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def my_func():
    # define variables to pass through to the template
    currentUser = "Chris"
    users = ["Gav", "Chris", "Eddy"]

    # return the template when user accesses the root, while passing through the created variables
    return render_template('index.html', user=currentUser, userList=users)

@app.route('/test_route')
def my_func_2():
    # return raw html as a string
    return '<h2>Hi from /test_route!</h2>'

if __name__ == "__main__":
    app.run(debug=True)
