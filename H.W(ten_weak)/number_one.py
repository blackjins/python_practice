'''
프랙탈 트리 알고리즘을 아래 사항들에 맞추어 수정하라.

branch_len 이 줄어들면 나뭇가지의 두께 또한 점점 얇아지도록 하라.
나뭇가지의 색상 또한 branch_len와 함께 달라져서 결국엔 나뭇잎 색깔이 되도록 하라.
좌우 가지치기의 각도를 15도에서 45도 사이에서 임의로 변할 수 있도록 하라. 단, 생성된 트리의 모양이 적절하게 보기 좋아야 한다.
나뭇가지의 길이가 일정하게 줄어드는 대신 가지치기 할 때마다 임의의 크기만큼 줄어들도록 하라. 단, 적절한 범위 내에서 줄어들어야 하며, 최종적으로 자연스럽게 보여야 한다.
제출 내용: trinket 사이트에서 코드를 작성하고 실행한 후에 공유 링크를 제출한다.
'''
import turtle
# import time                    # 주의: repl.it 사이트에서 오류 발생

def transeturtle(branch_len):
    if 55 < branch_len < 75:
        t.pensize(6)
        t.color(43, 21, 0)
    elif 40 < branch_len < 55:
        t.pensize(4)
        t.color(138, 69, 0)
    elif 25 < branch_len < 40:
        t.pensize(2)
        t.color(0, 255, 64)
    elif 10 < branch_len < 25:
        t.pensize(1)
        t.color(0, 102, 26)

def tree(branch_len, t, angle):
    if angle < 15 or angle > 45:
        raise Exception("15~45사이의 각도만 입력 해주세요")
    if branch_len >= 15:           # 종료조건: branch_len < 15
        transeturtle(branch_len)
        t.forward(branch_len)    # 전진
        # time.sleep(1)          
        t.right(angle)              # 오른쪽 가지치기
        tree(branch_len - 15, t, angle)
        t.left(angle*2)               # 왼쪽 가지치기
        tree(branch_len - 15, t, angle)
        transeturtle(branch_len)
        t.right(angle)              # 한 단계 후진
        t.backward(branch_len)

t = turtle.Turtle()
turtle.colormode(255)
my_win = turtle.Screen()
t.pensize(8)
t.left(90)
t.up()
t.backward(100)
t.down()
t.color(43, 21, 0)
tree(75, t, 40)
my_win.exitonclick()