# Đề bài
graph = {
  'A': [('B', 4, 11), ('C', 3, 11)],
  'B': [('F', 5,11), ('E', 12, 4)],
  'C': [('D', 7, 6), ('E', 10, 4)],
  'D': [('E', 2, 4)],
  'E': [('Z', 5, 0)],
  'F': [('Z', 16, 0)]
}

#tao ham h(n) theo de bai
def h(node):
  #ham tinh h(n) - o day mk se gia su h(n) la chi phi truc tiep n den dich Z
  h = {
    'A': 11,
    'B': 11,
    'C': 11,
    'D': 6,
    'E': 4,
    'F': 0,
    'Z': 0
  }
  return h[node]

#ham in duong di va chi phi
def print_path_and_cost(start, goal, parent, g):
  path = []
  current = goal
  while current != start:
    path.append(current)
    current = parent[current]
  path.append(start)
  path.reverse()
  print("Duong di:", '->'.join(path))
  print("Chi phi:", g[goal])

#ham A*
def A_star(graph, start, goals):
  MO = [start] #tap dinh mo, ban dau chua dinh start (chua xet xong)
  DONG = []  #tap dinh da xet, ban dau rong
  g = {start: 0} #chi phi tu start den dinh hien tai
  f = {start: h(start)} #f(n) = g(n) + h(n) gia tri f(n) cho moi dinh
  parent = {} #luu lai cha cua moi dinh

  while MO:
    #chon dinh n co f(n) nho nhat tu tap MO
    min_f = float('inf')
    min_node = None
    for node in MO:
      if f[node] < min_f:
        min_f = f[node]
        min_node = node
    n = min_node
    if n in goals:
      #neu n la dinh dich thi in duong di va chi phi
      print_path_and_cost(start, n, parent, g)
      print(parent)
      return True
    # xoa dinh n khoi tap MO va them vao tap DONG
    MO.remove(n)
    DONG.append(n)

    #duyet qua cac dinh ke cua n
    for m, cost_g, cost_h in graph.get(n, []): 
      #chi phi moi tu start den m
      cost_g_new = g[n] + cost_g
      if m not in MO and m not in DONG:
        #mo tong dinh m
        g[m] = cost_g_new
        f[m] = g[m] + cost_h
        parent[m] = n
        MO.append(m)
      elif m in MO and g[m] > cost_g_new:
        #cap nhat dinh m neu co chi phi moi tot hon
        g[m] = cost_g_new
        f[m] = g[m] + cost_h
        parent[m] = n
  #khong tim thay duong di den dich
  return False

print('A*')
A_star(graph, 'A', ['Z', 'F'])
