# cấu trúc đồ thị
graph = {
  'A': {'B': 2, 'C': 4, 'F': 6},
  'B': {},
  'C': {'D': 8, 'E': 2},
  'D': {},
  'E': {},
  'F': {'G': 5, 'H': 1},
  'G': {},
  'H': {}
}

# hàm in đường đi và chi phí
def print_path_and_cost(start, goal, parent, g):
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = parent[current]
    path.append(start)
    path.reverse()
    print("Đường đi:", '->'.join(path))
    print("Chi phí:", g[goal])

# thuật toán AT
def AT(graph, start, goals):
    MO = [start]
    g = {start: 0}
    DONG = []
    parent = {}

    while MO:
        # tìm nút trong MO có chi phí g(n) nhỏ nhất
        min_cost = float('inf')
        n = None
        for vertex in MO:
            cost = g.get(vertex, float('inf'))
            if cost < min_cost:
                min_cost = cost
                n = vertex
        
        # kiểm tra nếu n là nút mục tiêu
        if n in goals:
            print_path_and_cost(start, n, parent, g)
            return True
        
        # xóa n khỏi MO và thêm vào DONG
        MO.remove(n)
        DONG.append(n)

        # duyệt qua các nút kề của n
        for m in graph.get(n, {}):
            cost = graph[n][m]
            new_cost = g.get(n, float('inf')) + cost
            
            if m in g and new_cost < g[m]:
                g[m] = new_cost
                parent[m] = n
            elif m not in MO and m not in DONG:
                g[m] = new_cost
                parent[m] = n
                MO.append(m)
                
    return False

# khởi tạo dữ liệu        
start = 'A'
goals = ['D', 'H']
AT(graph, start, goals)
