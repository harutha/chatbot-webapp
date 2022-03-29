# extensions that allow specific flask classes and functions.
from flask import Flask, Blueprint, render_template, url_for, redirect, request
from animals import running_total
# from chatbot import predict_class, get_response, intents

##############################

# a 'blueprint' of the website structure.
views = Blueprint(__name__, "views")

# the website is defined as a flask app and the url prefix is set to '/'.
app = Flask(__name__)
app.register_blueprint(views, url_prefix = "/")
# app.config["SECRET_KEY"] = "a secret_keyyyyyy1234567"

# answer_list = []

##############################

# this is how the homepage is accessed.
@app.route("/") # the page is accessed via '/'.
def homepage(): # this is the homepage function.
    return render_template("index.html", running_total=running_total)

#############################
answer_list = []

@app.route("/chatbot", methods=["POST", "GET"])
def chatbot():
    global answer_list
    if request.method == "POST":
        message =  request.form["message"]
        ints = predict_class(message)
        response = get_response(ints, intents)
        answer_list.append(response)
        print(answer_list)
        if len(answer_list) > 5:
            answer_list.remove(answer_list[0])
        return render_template("chatbot.html", message=message, answer_list=answer_list)
    return render_template("chatbot.html", message="", answer_list=answer_list)

##############################


@app.route("/food")
def food_page():
    return render_template("food.html", user_name = "Food industry")

##############################

@app.route("/farming")
def farming_page():
    return render_template("farming.html", user_name = "Farming industry")

##############################

@app.route("/hunting")
def hunting_page():
    return render_template("hunting.html", user_name = "Hunting")

##############################

@app.route("/about")
def about_page():
    return render_template("about.html", user_name = "Hunting")

##############################

@app.route("/contact")
def contact_page():
    return render_template("contact.html", user_name = "Hunting")

##############################

@app.route("/card")
def card_page_page():
    return render_template("card.html", user_name = "Flip Card")

##############################

@app.route("/result")
def testing_page():
    return render_template("result.html", user_name = "Submitted")

##############################

@app.route("/home")
def home_redirect():
    return redirect(url_for("homepage"))

##############################

@app.errorhandler(404)
def page_not_found(e):
    return render_template("page_not_found.html"), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template("internal_server_error.html"), 500

##############################

# debugging is activated and the project is set to be hosted on port 8000 (debugging should only be used for testing purposes).
if __name__ == "__main__":
    app.run(debug = True, port = 8000)