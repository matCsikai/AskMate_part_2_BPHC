from flask import Flask, render_template, request, redirect, url_for
import time
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
    question = query.all_answers(config.connection(), question_id)
    return render_template('all_answers.html', question=question)


@app.route('/question/<question_id>/new-answer', methods=['GET', 'POST'])
def new_answer(question_id):
    question_database = read_data('question.csv')
    for line in question_database:
        if str(question_id) in line[0]:
            question_line = line

    file_name = "answer.csv"
    button_name = "Post your answer"
    all_data = read_data(file_name)
    timestamp = int(time.time())
    data_list = []
    if request.method == "POST":
        data_list.append(str(generate_data_id(file_name)))
        data_list.append(str(timestamp))
        data_list.append(' ')  # view number
        data_list.append(question_id)
        data_list.append(request.form['message'])
        data_list.append(' ')  # for picture
        all_data.append(data_list)
        new_data_to_write = write_data(file_name, all_data)
        return redirect(url_for('all_answers', question_id=question_id))
    return render_template("add_answer.html", question_line=question_line)


if __name__ == "__main__":
    app.run(debug=True)
