
# 파이썬 퀴즈 프로그램

이 프로그램은 객체지향 프로그래밍(OOP)을 활용하여 만든 퀴즈 게임입니다.
(OPP: object- oriented programming. 플레이어 정보, 문제와 정답, 게임 진행, 점수 등 프로그램에 필요한 것들을 객체로 만들어서 서로 역할을 나누는 것을 객체지향이라고 할 수 있을 것.파이썬.)


## 프로젝트 개요
| 단계 | 작업 내용 |
|:---:|:---:|
| 01 | 퀴즈 주제와 선정 이유 |
| 02 | 실행 방법 |
| 03 | 기능 목록  |
| 04 | 프로젝트 파일 구조 |
| 05 | 데이터 설명-state.json |
| 06 | 주요 기능 |
| 07 | 사용 기술 |
| 08 | 커밋별 작업 내용 01-10 |
| 09 | 기술 스택 |
| 10 | SUB Info |
| 11 | Self Q&A and Feedback |

## 퀴즈 주제와 선정 이유
파이썬 실습인 만큼 파이썬에 대한 기본 문제를 퀴즈 주제로 선정함. 


## 실행 방법
기본 메뉴 페이지에서 원하는 항목의 번호를 누른 후 Enter.
퀴즈를 풀고 싶다면 1번, 
퀴즈를 추가하고 싶다면 2번, 
퀴즈 목록을 확인하고 싶다면 3번, 
최고 점수를 확인하고 싶다면 4번, 
퀴즈 프로그램을 종료하고 싶다면 5번을 선택한다.
   

### 예시)

=========================
   퀴즈 프로그램   
=========================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 최고 점수 확인
5. 종료

========================

메뉴를 선택하세요: 


## 기능 목록 (실현해 본 기능들)
-퀴즈 풀기

-퀴즈 추가

-퀴즈 목록

-최고 점수 확인 및 경신

-퀴즈 푸는 동안 실시간 진도 정보 제공

-비정상 종료 방지



## 📂 프로젝트 파일 구조 (Project Structure)
```text
.
├── main.py              # 프로그램의 시작점 (Entry Point)
├── quiz_manager.py      # 데이터 관리 (JSON 로드/저장, 퀴즈 데이터 핸들링)
├── quiz_game.py         # 게임 흐름 제어 (메뉴 출력, 퀴즈 실행, 입력 검증)
├── state.json           # 퀴즈 데이터 및 최고 점수가 저장되는 JSON 파일
└── README.md            # 프로젝트 설명 및 가이드
```

## 데이터 설명-states.json
jason: 데이터를 저장하거나 주고받을 때 사용하는 텍스트 형식 <br>
형식: JSON 파일 기반의 로컬 데이터베이스 구조 <br>
quizzes: 퀴즈 객체 리스트 (질문, 정답 포함) <br>
high_score: 역대 최고 점수 기록 (정수형) <br>
특이사항: UTF-8 인코딩 적용으로 한글 데이터 안정성 확보 <br>


## 주요 기능
- 퀴즈 플레이
- 저장된 퀴즈 출제
- 정답 확인 및 실시간 진도 제공 기능 포함
- 게임 종료 후 최고 점수 달성 시 자동 갱신함
- 동적 퀴즈 관리
- 사용자가 직접 새로운 퀴즈를 추가할 수 있음
- 현재 저장된 모든 퀴즈의 목록 조회 가능함
- 입력 검증 및 예외 처리

- 빈 값 방지: 공백만 입력하거나 엔터만 칠 경우 재입력 요구함
- 파일 예외: state.json이 없거나 깨졌을 경우 기본 데이터로 자동 복구함
- 비정상 종료 방지: Ctrl+C나 EOFError 발생 시 데이터를 안전하게 저장하고 종료함
- 데이터 영속성

- 모든 변경 사항(신규 퀴즈, 점수)은 즉시 JSON 파일에 반영되어 재실행 시 유지됨


## 사용 기술
- Python 3.x
- JSON (데이터 저장)
- Git / GitHub (버전 관리)



## 커밋별 작업 내용

###  01
**저장소 설정 및 로드맵 작성**  

프로젝트의 전체 코드 초안을 작성하고, 퀴즈 게임의 기본 구조를 구성하였다.

---

###  02
**Quiz 클래스와 기본 퀴즈 데이터 구조 구현**

`QuizManager` 클래스를 정의하고, 문제・선택지・정답으로 이루어진 기본 데이터 구조를 구현하였다.
<img width="500" height="657" alt="스크린샷 2026-08-14 오후 3 15 48" src="https://github.com/user-attachments/assets/12bba3a3-365e-4ec5-8589-c4043b8406a8" />
<img width="500" height="518" alt="스크린샷 2026-08-14 오후 3 16 08" src="https://github.com/user-attachments/assets/d762536d-23bb-46e1-846f-3952cc31d0f3" />
<img width="500" height="208" alt="스크린샷 2026-08-14 오후 3 16 21" src="https://github.com/user-attachments/assets/83ae9c63-6906-46b2-a761-53bc8d09bc6d" />

QuizManager는 데이터 관리 및 파일 입출력을 담당하는 클래스.

git push origin main : 내 컴퓨터의 내용을 깃허브에 올리는 명령

---

###  03
**QuizGame 클래스 정의**  
<img width="542" height="549" alt="Screenshot 2026-08-10 at 9 22 32 AM" src="https://github.com/user-attachments/assets/328304d3-a368-4d0e-8656-7be7713a911b" />
<img width="542" height="405" alt="Screenshot 2026-08-10 at 9 22 46 AM" src="https://github.com/user-attachments/assets/0ca1903c-28d3-4ecb-a6e9-2e52ce84fdde" />

QuizGame는 사용자 인터페이스 및 게임 흐름을 담당하는 클래스.

`QuizGame` 클래스의 기본 구조를 만들고, 메뉴를 통해 게임이 동작할 수 있도록 구성함.

---

###  04
**최고 점수 기록 기능**  
<img width="500" height="154" alt="스크린샷 2026-08-14 오후 3 22 22" src="https://github.com/user-attachments/assets/f718f5d2-18ba-42ef-8e1d-464c10a1981f" />

변수를 0으로 초기화하고 시작. 퀴즈를 모두 푼 후 획득한 점수를 기존 최고 점수와 비교하여 더 높은 점수일 경우 최고 점수를 갱신하도록 구현함. 최고 점수는 state.json의 high_score에 저장되어 프로그램을 종료한 후에도 기록이 유지됨.

update_high_score() 메서드에서 현재 점수와 기존 최고 점수를 비교함. 현재 점수가 더 높은 경우에만 high_score를 새로운 점수로 변경하고 save_data()를 호출하여 JSON 파일에 저장함. 기존 최고 점수보다 낮거나 같은 경우에는 기존 기록을 그대로 유지함.

이를 통해 사용자가 이전 기록보다 높은 점수를 획득했을 때 최고 기록을 경신했다는 메시지를 출력하도록 구현함.


<img width="500" height="177" alt="스크린샷 2026-08-14 오후 3 24 23" src="https://github.com/user-attachments/assets/bfa22388-a2af-4097-a4c6-173361e201bc" />



---

###  05
**state.json에 대하여..**  

<img width="691" height="699" alt="스크린샷 2026-08-14 오후 3 25 50" src="https://github.com/user-attachments/assets/230ea7ee-a5fc-4c88-9494-acc5eb6df51a" />
 정보, 데이터만 따로 빼두는 공간이라고 생각함. 기본적으로 만든 5개의 문제와 선지와 더불어, 사용자가 메뉴에서 문제 추가시 이 공간에 문제(q)와 답(a)이 각각 추가 됨. 문제별로, 답별로 q와 a로 구분하였지만 가독성을 높이기 위해 나의 state.json에서는 딕셔너리의 형태로 quiz_set별로 묶어 놓았음.


---

###  06
**브랜치 생성과 병합**  

<img width="563" height="351" alt="스크린샷 2026-08-14 오후 3 31 49" src="https://github.com/user-attachments/assets/e84feff2-4e60-4cf7-9ead-e9ba61f055f8" />
#### Git 브랜치 생성 및 병합 실습
1. 작업 목적

기존 퀴즈 프로그램에 4지선다형 퀴즈 기능을 추가하고,
Git의 브랜치 생성, 커밋, 병합 과정을 실습한다.

2. 브랜치 생성

기존 `main` 브랜치의 코드를 직접 수정하지 않고,
새로운 `quiz-play` 브랜치를 생성하여 퀴즈 기능을 개발하였다.

```bash
git checkout -b quiz-play
```

---

###  07
**JSONDecodeError 예외 처리와 자동 복구 기능 추가**  
JSONDecodeError는 JSON 파일의 형식이 올바르지 않을 때 발생하는 예외!

state.json 파일의 형식이 잘못되어 JSON 데이터를 정상적으로 불러오지 못하는 경우 JSONDecodeError와 ValueError를 예외 처리하도록 구현함. JSON 파일이 손상되거나 비어 있는 등의 문제가 발생하면 프로그램이 종료되지 않고 기본 데이터를 새로 생성하여 state.json에 저장하도록 처리함. 이를 통해 잘못된 JSON 파일로 인해 프로그램이 실행되지 않는 상황을 방지하고 자동으로 기본 상태로 복구할 수 있도록 구현함.
<img width="542" height="483" alt="08" src="https://github.com/user-attachments/assets/740979ed-9997-4b2b-a837-c07ef35af3af" />
<img width="498" height="514" alt="스크린샷 2026-08-14 오후 3 45 54" src="https://github.com/user-attachments/assets/051d80c3-415f-4837-9deb-40a03078ce70" />


---
###  08
**퀴즈 추가 기능**
<img width="452" height="408" alt="스크린샷 2026-08-14 오후 3 35 05" src="https://github.com/user-attachments/assets/788a1f62-c2d1-4149-b8fd-871382dc921e" />
<img width="452" height="528" alt="스크린샷 2026-08-14 오후 3 35 36" src="https://github.com/user-attachments/assets/cf5e6dde-f09e-4270-8166-727cd92c4ab7" />

사용자가 직접 새로운 퀴즈를 추가할 수 있도록 구현하였다. 문제를 입력한 후 4개의 선지를 차례대로 입력하고, 그중 정답을 선택하면 새로운 퀴즈가 등록된다. 추가된 퀴즈는 state.json 파일에 저장되기 때문에 프로그램을 종료한 후에도 데이터가 유지된다. 또한 등록된 퀴즈는 퀴즈 목록에서 확인할 수 있으며, 이후 퀴즈 풀기 기능에서도 출제되도록 구현하였다. (직접 실행 후 확인 필)



###  09
**feat: Ctrl+C, EOFError 비정상 종료 처리 추가**  

KeyboardInterrupt

사용자가 프로그램 실행 중 Ctrl+C를 눌러 강제로 종료할 때 발생하는 예외임. 프로그램에서는 해당 예외를 처리하여 종료 안내를 출력하고 데이터를 저장한 후 안전하게 종료하도록 구현함.

EOFError

input()으로 사용자 입력을 받는 과정에서 더 이상 입력을 받을 수 없을 때 발생하는 예외임. 해당 예외가 발생하면 데이터를 저장하고 프로그램을 안전하게 종료하도록 처리함.

<img width="626" height="549" alt="09" src="https://github.com/user-attachments/assets/457d31c7-0497-4ebb-986d-543bcb556c12" />

---

###  10
**Clone 실습: 복제한 저장소에서 README를 수정**


<깃 저장소 복제 실습 완료 내용>
원격 GitHub 저장소를 git clone 명령어로 로컬에 복제하였다.
복제한 저장소(quiz-game-clone)에서 README.md 파일을 수정한 뒤 add, commit, push를 수행하여 변경 내용을 원격 저장소에 반영하였다.
이후 원래 프로젝트 폴더에서 git fetch와 git pull 명령어를 사용해 원격 저장소의 최신 내용을 가져왔고, 수정 사항이 정상적으로 반영되는 것을 확인하였다.
이를 통해 저장소 복제, 복제본에서의 작업, 원격 반영, 원본 로컬 저장소 동기화 과정을 실습함.
<img width="626" height="223" alt="Screenshot 2026-08-10 at 12 16 07 PM" src="https://github.com/user-attachments/assets/bb36cdd2-76b8-4e93-8b28-0886bf32f1ff" />

<img width="338" height="214" alt="Screenshot 2026-08-10 at 12 28 30 PM" src="https://github.com/user-attachments/assets/cbc49923-0fab-4b96-adf9-9b6fe0df4c64" />
[클론에서 확인 시 main.py, README.md, state.json이 원본 파일과 동일하게 들어가 있는 것을 확인할 수 있다!]

<img width="305" height="342" alt="스크린샷 2026-08-14 오후 4 38 56" src="https://github.com/user-attachments/assets/a50e2f4f-5e87-441d-9ebc-f5a627114140" />
<img width="927" height="442" alt="스크린샷 2026-08-14 오후 4 39 13" src="https://github.com/user-attachments/assets/7ac1151e-bc02-4437-bebd-947fba4a9477" />




## 🛠️ 기술 스택
- Language: Python 3.x
- Data Format: JSON
- Version Control: Git / GitHub

## SUB Info
1. 파이썬 기초 (Python Basics)

변수 (Variable): 데이터를 담는 공간. 데이터를 재사용하고, 이름(라벨)을 붙여서 관리하기 위해 사용

<자료형 (Data Types)>
 
int: 정수 (예: 1, 100)

str: 문자열 (예: "안녕하세요")

bool: 참/거짓 (True, False)

list: 순서가 있는 데이터의 목록 (예: [1, 2, 3])

dict: 키(Key)-값(Value) 쌍으로 이루어진 사전형 데이터 (예: {"이름": "홍길동"})

<제어문>

if/elif/else: 조건에 따라 길을 나누는 분기점

for vs while: for는 정해진 횟수나 범위를 반복할 때, while은 특정 조건이 참인 동안 계속 반복할 때 사용

함수 (Function): 반복되는 코드를 묶어놓은 것.

매개변수(Parameter): 함수에 전달하는 입력값.

반환값(Return): 함수가 실행된 후 내놓는 결과값.


2. 클래스와 객체

클래스 (Class): 객체를 만들기 위한 설계도. 비슷한 기능을 하는 변수와 함수를 하나로 묶기 위해 사용.

객체 (Object): 설계도(클래스)를 통해 실제로 만들어진 실체.

__init__ 메서드: 객체가 생성될 때 자동으로 호출되는 초기화 함수 (이름, 점수 등을 처음에 설정)

self: **"객체 자기 자신"**을 가리킴 클래스 내부에서 자신의 속성이나 메서드에 접근할 때 사용

속성(Attribute): 객체가 가진 상태/데이터 (예: 퀴즈의 문제 내용, 정답)

메서드(Method): 객체가 할 수 있는 동작/함수 (예: 퀴즈 확인하기, 점수 계산하기)


3. 파일 입출력 및 예외 처리
- 파일 입출력: open()으로 파일을 열고, read()/write()로 내용을 읽거나 쓴 뒤, close()로 닫는 과정 (파이썬에서는 with문을 쓰면 자동으로 닫아줌)

- JSON: 데이터를 저장하는 표준 텍스트 형식. 딕셔너리 구조와 비슷해서 읽기 쉽고, 다른 언어와 데이터를 주고받을 때 유리

- try/except: 프로그램 실행 중 발생할 수 있는 에러를 가로채서 처리하는 장치. 프로그램이 갑자기 꺼지는 것을 방지


4. Git 기초 (Version Control)
- Git: 코드의 변경 이력을 기록하는 버전 관리 시스템 과거로 되돌아가거나 협업할 때 필수

<주요 명령어>
- init: 새로운 Git 저장소 만들기(시작).

- add: 변경된 파일을 기록할 준비.

- commit: 변경 사항을 확정하여 기록.

- push: 로컬의 기록을 원격 저장소(GitHub)에 올리기.

- pull: 원격 저장소의 최신 내용을 내 컴퓨터로 가져오기.

- checkout: 다른 브랜치로 이동하기.

- clone: 원격 저장소를 내 컴퓨터로 통째로 복사해오기.

<브랜치(Branch) & 병합(Merge)>
- 브랜치: 원본 코드에 영향을 주지 않고 새로운 기능을 만들기 위한 복사된 작업 공간(가지).

- 병합: 브랜치에서 만든 기능을 검토 후 메인 코드에 합치는 것.

## Self Q&A and Feedback

Q1. if name == "main" 가 무엇인가?

A1. 이번에 프로그램을 만들면서 코드의 맨마지막에 
if __name__=="__main__":
    game = QuizGame()
    game.run()
이라고 쓰인 코드를 발견과 동시에 평가를 받는 과정에서 이 코드의 쓰임이 궁금해짐.
__name__이란 파이썬이 자동으로 만들어주는 특별한 변수 중 하나. 파이썬에서 파일을 직접 실행하면 파이썬은 이 파일의 __name__을 "__main__"으로 설정함. 그ㅡ래서 print(__name__) 실행하면 __main__이 출력된다. 
그렇다면 if __name__=="__main__": 의 뜻은? '파일을 직접 실행한 경우에만 아래 코드를 실행하라'라는 뜻.
왜 이렇게 사용할까? 사실상 지금 메인 프로그램으로 직접 실행되고 있는지를 확인하는 코드임.메인 파일로 직접 실행되고 있다면 실행하고 다른 파일에서 import된 것이라면 실행하지 않음. 직접 실행할 때만 실행되고 다른 파일에서 import를 통해 가져다 쓰면 아래 두줄은 자동으로 실행되지 않음!

Q2. EOFError란?
A2. 입력을 받아야 하는데 입력할 데이터가 없을 때 발생하는 에러. 입력을 받지 못하고 입력 자체가 끝나버리면 이 에러는 발생시킴. 이 프로젝트에서는 이를 방지하기 위해 commit 09 에서 기능을 추가함.
