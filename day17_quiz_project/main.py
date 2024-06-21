import question_model, html, requests, json
from quiz_brain import QuizBrain

# Modification to get the same quiz every time. Credit to Coe from the python 100 days course on Udemy.
url = requests.get("https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=boolean")
url.raise_for_status()
text = url.text
quiz_api_data = json.loads(text)
question_data = quiz_api_data["results"]

q = question_model.Question("q","a")
question_bank = []
# Get all the data from the list of dictionaries into a list of objects.
# for i in data.question_data: # Removed this since we're not using the local data any more.
for i in question_data:
    # print(i["text"])
    question_bank.append(question_model.Question(html.unescape(i["question"]), i["correct_answer"]))

quiz = QuizBrain(question_bank)
while quiz.still_has_questions(): # If quiz still has questions remaining.
    quiz.next_question()

print(f"You've completed the quiz. Your final score was {quiz.score}/{quiz.question_number}.")
