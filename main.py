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
    list_all_user = query.list_all_user()
    if request.method == "POST":
        question_title = request.form['question_title']
        question_message = request.form['message']
        question_user = request.form['user']
        query.insert_data(question_title, question_message, question_user)
        query.fetch_user_id(question_user)
        return redirect(url_for('home_page'))
    return render_template("add_question.html",  list_all_user=list_all_user, title=title, button_name=title)


@app.route('/question/<int:question_id>', methods=['GET', 'POST'])
def question_page(question_id):
    question_data = query.question(question_id)
    answer_data = query.answer(question_id)
    question_comment_data = query.question_comment(question_id)

    # vote question
    current_question_vote = request.args.get('current_question_vote')
    if request.args.get('vote') == "add":
        query.update_vote("question", question_id, int(current_question_vote) + 1)
        return redirect(url_for('question_page', question_id=question_id))
    elif request.args.get('vote') == "remove":
        query.update_vote("question", question_id, int(current_question_vote) - 1)
        return redirect(url_for('question_page', question_id=question_id))

    # vote answer
    current_answer_vote = request.args.get('current_answer_vote')
    answer_id = request.args.get('answer_id')
    if request.args.get('vote_answer') == "add":
        query.update_vote("answer", int(answer_id), int(current_answer_vote) + 1)
        return redirect(url_for('question_page', question_id=question_id))
    elif request.args.get('vote_answer') == "remove":
        query.update_vote("answer", int(answer_id), int(current_answer_vote) - 1)
        return redirect(url_for('question_page', question_id=question_id))

    #answer_comment_data = query.answer_comment(answer_id)
    return render_template('question_page.html', question_data=question_data, answer_data=answer_data,
                           question_comment_data=question_comment_data)



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
        insert_question_comment = query.insert_question_comment(comment_message, question_id)
        # display question list page

        all_question = query.all_question()
        return render_template("all_question.html", all_question=all_question, title="All question")
    return render_template("add_comment_question.html", add_comment_question=add_comment_question,
                           question_id=question_id, title="Add comment to question")



@app.route('/answer/<int:answer_id>/new-comment', methods=['GET'])
def add_comment_answer(answer_id):
    add_comment_answer = query.get_answer(answer_id)
    return render_template("add_comment_answer.html", add_comment_answer=add_comment_answer,
                           answer_id=answer_id, title="Add comment to answer")


@app.route('/answer/<int:answer_id>/new-comment', methods=['POST'])
def add_comment_answer_post(answer_id):
    comment_message = request.form['message']
    insert_answer_comment = query.insert_answer_comment(comment_message, answer_id)
    question_id_from_answer = query.question_id_from_answer(answer_id)
    return redirect(url_for('question_page', question_id=question_id_from_answer))


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


@app.errorhandler(404)
def page_not_found(e):
    title = "404 - This page not found"
    return render_template('error.html', title=title), 404


@app.errorhandler(500)
def page_not_found(e):
    title = "500 - Internal Server Error"
    return render_template('error.html', title=title), 500


if __name__ == "__main__":
    app.run(debug=True)

