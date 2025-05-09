from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from datetime import datetime
from bson.objectid import ObjectId
from openai import OpenAI

from app import mongo
from app.ai.forms import AIQuestionForm
from config import Config

ai = Blueprint('ai', __name__)

# Initialize the OpenAI client
client = OpenAI(api_key=Config.OPENAI_API_KEY)

@ai.route('/ask', methods=['GET', 'POST'])
@login_required
def ask_question():
    form = AIQuestionForm()
    if form.validate_on_submit():
        question = form.question.data.strip()

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are Green Genius, an expert in sustainability."},
                    {"role": "user", "content": question}
                ]
            )
            answer = response.choices[0].message.content.strip()

            # Save to DB
            result = mongo.db.ai_suggestions.insert_one({
                "user_id": current_user.get_id(),
                "question": question,
                "response": answer,
                "timestamp": datetime.utcnow(),
                "saved": False
            })

            return render_template('ai/response.html', question=question, response=answer, suggestion_id=result.inserted_id)

        except Exception as e:
            flash("There was an error with the AI service. Please try again later.", "danger")
            print(e)

    return render_template('ai/ask.html', form=form)

@ai.route('/save/<suggestion_id>')
@login_required
def save_suggestion(suggestion_id):
    mongo.db.ai_suggestions.update_one(
        {'_id': ObjectId(suggestion_id), 'user_id': current_user.get_id()},
        {'$set': {'saved': True}}
    )
    flash('Suggestion saved!', 'success')
    return redirect(url_for('ai.view_history'))

@ai.route('/history')
@login_required
def view_history():
    suggestions = list(mongo.db.ai_suggestions.find({'user_id': current_user.get_id()}).sort('timestamp', -1))
    return render_template('ai/history.html', suggestions=suggestions)