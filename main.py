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
        print(f"\n총 {len(quizzes)}문제를 시작합니다!")
        for i, item in enumerate(quizzes, 1):
            answer = input(f"Q{i}. {item['q']}: ").strip()
            if answer == item['a']:
                print("✅ 정답입니다!")
                score += 1
            else:
                print(f"❌ 틀렸습니다. 정답은 '{item['a']}'입니다.")
        
        print(f"\n최종 점수: {score}/{len(quizzes)}")
        if self.manager.update_high_score(score):
            print("🎊 축하합니다! 최고 기록을 경신했습니다!")

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
        while True:
            choice = self.display_menu()
            if choice == '1':
                self.play()
            elif choice == '2':
                self.add_new_quiz()
            elif choice == '3':
                self.show_list()
            elif choice == '4':
                print(f"\n현재 최고 점수: {self.manager.data['high_score']}점")
            elif choice == '5':
                print("프로그램을 종료합니다. 즐거운 하루 되세요!")
                break
            else:
                print("⚠️ 잘못된 선택입니다. 다시 입력해주세요.")

# 프로그램 시작
if __name__ == "__main__":
    game = QuizGame()
    game.run()