import json
import os

# [커밋 2] Quiz 클래스 정의 및 기본 데이터
class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer  # 1~4 사이의 정수

    def display(self, index):
        print(f"\n문제 {index}. {self.question}")
        for i, choice in enumerate(self.choices, 1):
            print(f"{i}) {choice}")

    def check_answer(self, user_answer):
        return user_answer == self.answer

# 기본 퀴즈 데이터 (5개 이상)
def get_default_quizzes():
    return [
        Quiz("파이썬의 창시자는?", ["Guido van Rossum", "Elon Musk", "Bill Gates", "Mark Zuckerberg"], 1),
        Quiz("파이썬 파일의 확장자는?", [".py", ".js", ".java", ".cpp"], 1),
        Quiz("리스트에 요소를 추가하는 메서드는?", ["add()", "push()", "append()", "insert()"], 3),
        Quiz("파이썬에서 'Hello World'를 출력하는 함수는?", ["printf()", "print()", "echo()", "say()"], 2),
        Quiz("파이썬의 데이터 타입이 아닌 것은?", ["int", "float", "string", "double"], 4)
    ]