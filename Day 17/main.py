from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for text_answer in question_data:
    # print(text_answer)
    # question = text_answer['text']
    question = text_answer['question']
    # print(question)
    # answer = text_answer['answer']
    answer = text_answer['correct_answer']
    # print(answer)
    question_object = Question(question, answer)
    question_bank.append(question_object)


# print(len(question_bank))
# print(question_bank[0].answer)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.current_score}/{len(quiz.questions_list)}")
