# ⭕️❌ゲーム
import random

# ボードを表示する
def board_show():
  for i in range(3):
    print("|ー＋ー＋ー|")
    for j in range(3):
      print(end='|')
      if board[i][j]==0:
        print(end='  ')
      elif board[i][j]==1:
        print(end='⭕️')
      elif board[i][j]==2:
        print(end='❌')
    print(end='|')
    print(i+1)
    if i==2:
      print("|ー＋ー＋ー|\n  1  2  3")

# 座標の入力
def input_xy():
  while True:
    x=input("Enter the X from 1 to 3: ")
    y=input("Enter the Y from 1 to 3: ")

    try:
      x=int(x)
      y=int(y)
    except ValueError:
      print("Try again: Please enter a number from 1 to 3")
      continue

    if 1>x or 3<x or 1>y or 3<y:
      print("Try again: Please enter a number from 1 to 3")
      continue

    else:
      x-=1
      y-=1
      if board[y][x]==0:
        board[y][x]=1
        break
      else:
        print("Try again: Please fill in the blank cells")

# CPU座標の決定
def CPU_xy():
  while True:
    x=random.randint(0,2)
    y=random.randint(0,2)
    if board[y][x]==0:
      board[y][x]=2
      break

# 正解判定
def judge():
  hantei=0
  for i in range(3):
    if board[i][0]==board[i][1] and board[i][1]==board[i][2] and board[i][0]!=0:
      hantei=board[i][0]
      break
    elif board[0][i]==board[1][i] and board[1][i]==board[2][i] and board[0][i]!=0:
      hantei=board[0][i]
      break
  if hantei==0:

    if board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[0][0]!=0:
      hantei=board[0][0]
    elif board[2][0]==board[1][1] and board[1][1]==board[0][2] and board[2][0]!=0:
      hantei=board[2][0]
  return hantei

# ランダムに先手を決める
def first_move():
  print("Decide first move")
  D_fm=random.randint(0,1)
  if D_fm==0:
    print("You are first")
  else:
    print("CPU is first")
  return D_fm

# 終局判定
def no_space():
  ns=0
  for i in range(3):
    for j in range(3):
      if board[i][j]==0:
        ns+=1
  if ns==0:
    return 'fin'

def game():
  board = [[0 for i in range(3)] for j in range(3)]
  print("Decide first move")
  D_fm=first_move()

  while True:
    board_show()
    if D_fm==0:
      print("Your turn")
      input_xy()
      D_fm=1
    else:
      print("CPU turn")
      CPU_xy()
      D_fm=0 

    ha=judge()
    if ha==1:
      print("\nYou win\n")
      break
    elif ha==2:
      print("\nCPU win\n")
      break

    NS=no_space()
    if NS=='fin':
      print("There is no space")
      break


while True:
  board = [[0 for i in range(3)] for j in range(3)]
  game()
  board_show()
  a=input("Do you want to continue? y/n: ")
  if a=="y":
    continue
  else:
    print("It's end")
    break
