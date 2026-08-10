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

# [커밋 3]
class QuizGame:
    def __init__(self, quizzes):
        self.quizzes = quizzes  # Quiz 객체들이 담긴 리스트
        self.score = 0          # 맞춘 개수

    def start(self):
        """게임을 시작하고 전체 문제를 순회하는 메인 루프"""
        print("\n" + "="*30)
        print("   파이썬 퀴즈 게임을 시작합니다!   ")
        print("="*30)

        for i, quiz in enumerate(self.quizzes, 1):
            print(f"\n[문제 {i}] {quiz.question}")
            for option in quiz.options:
                print(option)

            # 사용자 입력 받기 (예외 처리 포함)
            try:
                user_input = input("정답 번호를 입력하세요 (1-4): ").strip()
                user_answer = int(user_input)

                if quiz.check_answer(user_answer):
                    print("✅ 정답입니다!")
                    self.score += 1
                else:
                    print(f"❌ 틀렸습니다. 정답은 {quiz.answer}번입니다.")
            except ValueError:
                print("⚠️ 숫자만 입력해 주세요! 이번 문제는 무효 처리됩니다.")

        self.show_result()

    def show_result(self):
        """최종 결과를 출력"""
        print("\n" + "="*30)
        print(f"게임 종료! 당신의 최종 점수는 {self.score}/{len(self.quizzes)}입니다.")
        print("="*30)