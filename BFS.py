class Node:
  def __init__(self, ten, cha = None):
    self.ten = ten
    self.cha = cha
  def display(self):
    print(self.ten)

#tao do thi dang cay theo de bai
from collections import defaultdict
data = defaultdict(list)
data['A'] = ['B', 'C', 'D']
data['B'] = ['M', 'N']
data['C'] = ['L']
data['D'] = ['O', 'P']
data['M'] = ['X', 'Y']
data['N'] = ['U', 'V']
data['O'] = ['I', 'J']
data['Y'] = ['R', 'S']
data['V'] = ['G', 'H']

#tao ham kiem tra
def kiemTra(tam, MO):
  for v in MO:
    if v.ten == tam.ten:
      return True
  return False

#ham luu vet duong di
def duongDi(n):
  print(n.ten)
  if n.cha != None:
    duongDi(n.cha)
  else:
    return
  
#ham tim kiem theo chieu rong
def BFS (To, Tg):
  MO = []
  DONG = []
  MO.append(To)
  while True:
    #neu danh sach MO rong thi ket thuc
    if len(MO) == 0: 
      print("tim kiem khong thanh cong")
      return 
    #lay phan tu dau tien cua danh sach MO
    n = MO.pop(0)
    if n.ten == Tg.ten:
      print("tim kiem thanh cong")
      duongDi(n)
      return
    DONG.append(n)
    #duyet cac dinh ke cua dinh n
    for v in data[n.ten]:
      tam = Node(v)
      ok1 = kiemTra(tam, MO)
      ok2 = kiemTra(tam, DONG)
      if not ok1 and not ok2:
        MO.append(tam)
        tam.cha = n

#thuc hien tim kiem
BFS(Node('A'), Node('N'))