from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

quiz_list = [Question(item["text"], item["answer"]) for item in question_data]

quiz_brain = QuizBrain(quiz_list)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()
else:
    print("You've completed the quiz")
    print(f"Your final score was {quiz_brain.score}/{quiz_brain.question_number}")
