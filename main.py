from flask import Flask, render_template, request, redirect, url_for
import query
import common
import config

app = Flask(__name__)


@app.route("/")
def home_page():
    five_latest_questions = common.fetch_data(query.five_latest_questions(config.connection()))
    return render_template("all_question.html", all_question=five_latest_questions, title="Homepage")


@app.route("/list")
def questions():
    all_question = common.fetch_data(query.all_question(config.connection()))
    return render_template("all_question.html", all_question=all_question, title="All question")


@app.route("/question/new", methods=['GET', 'POST'])
def add_question():
    title = "Ask question"
    if request.method == "POST":
        question_title = request.form['question_title']
        question_message = request.form['message']
        query.insert_data(config.connection(), question_title, question_message)
        return redirect(url_for('home_page'))
    return render_template("add_question.html",  title=title, button_name=title)


@app.route('/question/<question_id>', methods=['GET', 'POST'])
def all_answers(question_id):
    question_data = query.question(config.connection(), question_id)
    answer_data = query.answer(config.connection(), question_id)
    return render_template('all_answers.html', question_data=question_data, answer_data=answer_data)


@app.route('/question/<question_id>/new-answer', methods=['GET', 'POST'])
def new_answer(question_id):
    title = "Add answer"
    if request.method == "POST":
        answer_message = request.form['message']
        query.insert_answer(config.connection(), answer_message, question_id)
        return redirect(url_for('all_answers', question_id=question_id))
    return render_template("add_answer.html",  title=title, button_name=title)


if __name__ == "__main__":
    app.run(debug=True)
