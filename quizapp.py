class Question:
    def __init__(self , question_text , options, correct_answer):
        self.question_text = question_text
        self.options = options
        self.correct_answer = correct_answer

    def check_answer(self, answer): # this method checks if the provided answer matches the correct answer (True or False )
        return answer == self.correct_answer

class Quiz: # to manage quiz flow
    def __init__(self, questions):
        self.questions = questions
        self.score = 0  # instance variable initialized directly in the constructor

    def start(self):
        print ("Welcome to the Quizz app!\n")
        for index,question in enumerate(self.questions, start =1):   # enumerate gives both the index and question.
            print(f"Question {index}: {question.question_text}")
            for i , option in enumerate (question.options , start=1):
                print(f"{i}.{option}")

              # prompt user input btwn 1 to 4. -1 is subtracted to adjust for zero-based indexing ie 1 becomes 0
            try:
                answer = int(input("Your answer (1-4): ")) - 1
                if answer < 0 or answer >= len(question.options):
                     print("Invalid choice. Please select a number between 1 and 4.\n")
                     continue
            except ValueError:
                print("Invalid input. Please enter a number.\n")
                continue
            if not question.check_answer(question.options[answer]):
                print(f"Wrong! The correct answer was: {question.correct_answer}\n")

                # Display the final score
                print(f"Quiz completed! Your final score is: {self.score}/{len(self.questions)}")
        # Check if the answer is correct
        else:
                print("Correct!\n")
                self.score += 1

# questions
questions =[
Question("What is the capital of France?", ["Berlin", "London", "Paris", "Madrid"], "Paris"),
Question("Which planet is known as the Red Planet?", ["Earth", "Mars", "Jupiter", "Saturn"], "Mars"),
Question("Who wrote 'To be, or not to be'?", ["Shakespeare", "Hemingway", "Orwell", "Twain"], "Shakespeare"),
Question("What is the chemical symbol for water?", ["H2O", "O2", "CO2", "NaCl"], "H2O")
]

# Create a Quiz instance with the defined questions
quiz = Quiz(questions)

# Start the quiz
quiz.start()


# score
def display_score_summary(self):
        total_questions = len(self.questions)
        percentage_score = (self.score / total_questions) * 100
        print(f"Quiz completed! Your score is {self.score}/{total_questions} "
              f"({percentage_score:.2f}%).")   