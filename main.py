import json
import os

class QuizManager:
    """데이터 관리 및 파일 입출력을 담당하는 클래스"""
    def __init__(self, filename="state.json"):
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        """파일에서 데이터를 불러오거나 기본 데이터를 생성함"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (json.JSONDecodeError, ValueError):
                # 파일이 비어있거나 형식이 잘못된 경우 기본 데이터 생성
                return self.create_default_data()
        else:
            return self.create_default_data()

    def create_default_data(self):
        """기본 데이터 생성 및 저장"""
        initial_data = {
            "high_score": 0,
            "quizzes": [
                {"q": "파이썬에서 리스트에 요소를 추가하는 함수는?", "a": "append"},
                {"q": "파이썬의 창시자 이름은?", "a": "귀도 반 로섬"},
                {"q": "출력할 때 사용하는 함수는?", "a": "print"},
                {"q": "정수형 데이터 타입을 무엇이라 하나요? (약자)", "a": "int"},
                {"q": "조건문을 사용할 때 쓰는 키워드는?", "a": "if"}
            ]
        }
        self.save_data(initial_data)
        return initial_data

    def save_data(self, data=None):
        """데이터를 JSON 파일로 저장함"""
        if data:
            self.data = data
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)

    def add_quiz(self, question, answer):
        self.data["quizzes"].append({"q": question, "a": answer})
        self.save_data()

    def update_high_score(self, score):
        if score > self.data["high_score"]:
            self.data["high_score"] = score
            self.save_data()
            return True
        return False

class QuizGame:
    """사용자 인터페이스 및 게임 흐름을 담당하는 클래스"""
    def __init__(self):
        self.manager = QuizManager()

    # --- [08번 커밋: 새로 추가되는 메서드들] ---
    def add_new_quiz(self):
        print("\n➕ 새로운 퀴즈 추가")
        question = self.get_input("질문: ")
        answer = self.get_input("정답: ")
        
        new_quiz = {"q": question, "a": answer}
        self.manager.data["quizzes"].append(new_quiz)
        self.manager.save_data()
        print("✅ 퀴즈가 성공적으로 추가되었습니다!")

    def show_list(self):
        quizzes = self.manager.data["quizzes"]
        print("\n📋 현재 퀴즈 목록")
        print("-" * 30)
        if not quizzes:
            print("등록된 퀴즈가 없습니다.")
        else:
            for i, item in enumerate(quizzes, 1):
                # f-string을 사용하여 목록을 깔끔하게 출력합니다.
                print(f"{i}. {item['q']} (정답: {item['a']})")
        print("-" * 30)
    #08커밋 추가 완료

    def get_input(self, prompt, required=True): # [커밋5]
        """입력값이 비어있지 않은지 확인하고 반환하는 안전한 입력 메서드"""
        while True:
            value = input(prompt).strip()
            if not value and required:
                print("⚠️ 입력값이 비어있습니다. 다시 입력해주세요.")
                continue
            return value

    def display_menu(self):
        print("\n" + "="*25)
        print("   퀴즈 프로그램   ")
        print("="*25)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 최고 점수 확인")
        print("5. 종료")
        print("="*25)
        return input("메뉴를 선택하세요: ")

    def play(self):
        quizzes = self.manager.data["quizzes"]
        if not quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        score = 0
        total = len(quizzes)
        
        print(f"\n🚀 퀴즈 게임을 시작합니다! (총 {total}문제)")
        print("-" * 30)

        for i, item in enumerate(quizzes, 1):
            print(f"[{i}/{total}] {item['q']}")
            user_answer = self.get_input("답변 입력: ")

            # 정답 체크 로직 (공백 제거 및 소문자 변환으로 유연하게 체크)
            if user_answer.strip().lower() == item['a'].strip().lower():
                print("✅ 정답입니다!")
                score += 1
            else:
                print(f" 틀렸습니다. (정답: {item['a']})")
            print("-" * 30)

        # 최종 결과 출력
        print(f"\n📊 게임 종료! 최종 점수: {score} / {total}")
        
        if self.manager.update_high_score(score):
            print("🎊 축하합니다! 최고 기록을 경신했습니다!")
        else:
            print(f"현재 최고 기록: {self.manager.data['high_score']}점")

    def add_new_quiz(self):
        q = input("새로운 문제 내용을 입력하세요: ")
        a = input("정답을 입력하세요: ")
        if q and a:
            self.manager.add_quiz(q, a)
            print("✨ 퀴즈가 성공적으로 추가되었습니다.")
        else:
            print("⚠️ 문제와 정답을 모두 입력해야 합니다.")

    def show_list(self):
        print("\n--- 퀴즈 목록 ---")
        for i, item in enumerate(self.manager.data["quizzes"], 1):
            print(f"{i}. {item['q']} (정답: {item['a']})")

    def run(self):
        try:
            while True:
                choice = self.display_menu()
                
                if choice == '1':
                    self.play()
                elif choice == '2':
                    self.add_new_quiz()
                elif choice == '3':
                    self.show_list()
                elif choice == '4':
                    print(f"\n🏆 현재 최고 점수: {self.manager.data['high_score']}점")
                elif choice == '5':
                    print("👋 프로그램을 종료합니다. 다음에 또 만나요!")
                    break
                else:
                    print("⚠️ 잘못된 선택입니다. 1~5 사이의 숫자를 입력해주세요.")
        
        # Ctrl+C(KeyboardInterrupt) 또는 EOFError(입력 종료) 발생 시 처리
        except (KeyboardInterrupt, EOFError):
            print("\n\n👋 프로그램이 강제 종료되었습니다. 데이터를 안전하게 저장하고 종료합니다.")
            self.manager.save_data()

# 프로그램 시작
if __name__ == "__main__":
    game = QuizGame()
    game.run()