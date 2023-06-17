from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for ques_dict in question_data:
    ques_text = ques_dict["text"]
    ques_ans = ques_dict["answer"]
    ques_object = Question(ques_text, ques_ans)
    question_bank.append(ques_object)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions() == True:
    quiz.next_question()