from .dbHelper import dbHelper

class Question:
    def __init__(self, questionId=None, question=None, subject=None, grade=None, answer1=None, answer2=None, answer3=None, answer4=None, correctAnswer=None, points=None, enabled=None):
        self.questionId = questionId
        self.question = question
        self.subject = subject
        self.grade = grade
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.answer4 = answer4
        self.correctAnswer = correctAnswer
        self.points = points
        self.enabled = enabled

    def __str__(self):
        return f"{self.question}, {self.subject}, {self.grade}, {self.answer1}, {self.answer2}, {self.answer3}, {self.answer4}, {self.correctAnswer}, {self.points}, {self.enabled}"
    
    def get_question(self, questionId):
        db = dbHelper()
        with db.get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Questions WHERE QuestionId = ?", (questionId,))
            row = cursor.fetchone()
            if row is not None:
                self.questionId = row.QuestionId
                self.question = row.Question
                self.subject = row.Subject
                self.grade = row.Grade
                self.answer1 = row.Answer1
                self.answer2 = row.Answer2
                self.answer3 = row.Answer3
                self.answer4 = row.Answer4
                self.correctAnswer = row.CorrectAnswer
                self.points = row.Points
                self.enabled = row.Enabled
            else: return None

    def json(self):
        return {
            "questionId": self.questionId,
            "question": self.question,
            "subject": self.subject,
            "grade": self.grade,
            "answer1": self.answer1,
            "answer2": self.answer2,
            "answer3": self.answer3,
            "answer4": self.answer4,
            "correctAnswer": self.correctAnswer,
            "points": self.points,
            "enabled": self.enabled
        }
    
    def add_question(self, question):
        db = dbHelper()
        with db.get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Questions (QuestionId, Question, Subject, Grade, Answer1, Answer2, Answer3, Answer4, CorrectAnswer, Points, Enabled) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (question.questionId, question.question, question.subject, question.grade, question.answer1, question.answer2, question.answer3, question.answer4, question.correctAnswer, question.points, question.enabled))
            conn.commit()

    def update_question(self, question, questionId):
        db = dbHelper()
        with db.get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE Questions SET Question = ?, Subject = ?, Grade = ?, Answer1 = ?, Answer2 = ?, Answer3 = ?, Answer4 = ?, CorrectAnswer = ?, Points = ?, Enabled = ? WHERE QuestionId = ?", (question.question, question.subject, question.grade, question.answer1, question.answer2, question.answer3, question.answer4, question.correctAnswer, question.points, question.enabled, questionId))
            conn.commit()

    def delete_question(self, questionId):
        db = dbHelper()
        with db.get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Questions WHERE QuestionId = ?", (questionId,))
            conn.commit()