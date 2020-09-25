from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome ..."

@app.route(r'/hello')
def hello_world():
    return "Hello World."


if __name__ == '__main__':
    app.run(debug=True)


# from flask import Flask
# app = Flask(__name__)
#
# # @app.route('/')
# # def hello_world():
# #     return 'Hello World'
#
# if __name__ == '__main__':
#     app.run()