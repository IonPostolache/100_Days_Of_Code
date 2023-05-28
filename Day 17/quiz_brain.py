class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.questions_list = question_list
        self.current_score = 0

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        current_question_number = self.questions_list[self.question_number]
        self.question_number += 1
        # print(current_question_number)
        users_answer = input(f"Q.{self.question_number}. {current_question_number.text} (True/False)?: ").lower()
        # print(f"users_answer.title(): {users_answer}")
        correct_answer = current_question_number.answer.lower()
        # print(f"the correct answer is: {correct_answer}")
        self.check_answer(users_answer, correct_answer)

    def check_answer(self, users_answer, correct_answer):
        if users_answer == correct_answer:
            self.current_score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer.title()}.")
        print(f"Your current score is: {self.current_score}/{self.question_number}. \n")

