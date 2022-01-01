from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [Question(data['text'], data['answer']) for data in question_data]

quiz_brain = QuizBrain(question_bank)
while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print(f"You've completed the quiz.\nYour final score was: {quiz_brain.score}/{quiz_brain.question_number}")
