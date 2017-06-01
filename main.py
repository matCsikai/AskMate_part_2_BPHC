from flask import Flask, render_template, request, redirect, url_for
import query
import common
import config


app = Flask(__name__)


@app.route("/")
def home_page():
    five_latest_questions = query.five_latest_questions()
    return render_template("all_question.html", all_question=five_latest_questions, title="Homepage")


@app.route("/list")
def questions():
    all_question = query.all_question()
    return render_template("all_question.html", all_question=all_question, title="All question")


@app.route("/question/new", methods=['GET', 'POST'])
def add_question():
    title = "Ask question"
    if request.method == "POST":
        question_title = request.form['question_title']
        question_message = request.form['message']
        query.insert_data(question_title, question_message)
        return redirect(url_for('home_page'))
    return render_template("add_question.html",  title=title, button_name=title)


@app.route('/question/<int:question_id>', methods=['GET', 'POST'])
def question_page(question_id):
    question_data = query.question(question_id)
    answer_data = query.answer(question_id)
    question_comment_data = query.question_comment(question_id)
    return render_template('question_page.html', question_data=question_data,
                           answer_data=answer_data, question_comment_data=question_comment_data)


@app.route('/question/<question_id>/new-answer', methods=['GET', 'POST'])
def new_answer(question_id):
    title = "Add answer"
    if request.method == "POST":
        answer_message = request.form['message']
        query.insert_answer(answer_message, question_id)
        return redirect(url_for('question_page', question_id=question_id))
    return render_template("add_answer.html",  title=title, button_name=title)


@app.route('/question/<question_id>/new-comment', methods=['GET', 'POST'])
def add_comment_question(question_id):
    add_comment_question = query.get_question(question_id)
    if request.method == 'POST':
        comment_message = request.form['message']
        insert_question = query.insert_question_comment(comment_message, question_id)
        # display question list page
        all_question = query.all_question()
        return render_template("all_question.html", all_question=all_question, title="All question")
    return render_template("add_comment_question.html", add_comment_question=add_comment_question,
                           question_id=question_id, title="Add comment to question")


@app.route('/registration', methods=['GET', 'POST'])
def add_new_user():
    title = "User registration"
    button = "Send the registration"
    if request.method == "POST":
        user = request.form['user']
        insert_username = query.insert_username(user)
        return redirect(url_for('home_page'))
    return render_template("user_registration.html", title=title, button_name=button)


@app.route("/users")
def users():
    all_user = query.all_user()
    
    return render_template("users.html", all_user=all_user, title="All registered user")


if __name__ == "__main__":
    app.run(debug=True)

