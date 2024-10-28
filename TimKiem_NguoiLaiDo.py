from enum import Enum
from collections import namedtuple

#định nghĩa các vị trí
Location = Enum('Location', ['A', 'B'])

#định nghĩa trạng thái
State = namedtuple("State", ['man', 'cabbage', 'goat', 'wolf'])

#kiểm tra trạng thái hợp lệ
def is_valid(state):
    goat_eats_cabbage = (state.goat == state.cabbage and state.man != state.goat)
    wolf_eats_goat = (state.wolf == state.goat and state.man != state.wolf)
    return not (goat_eats_cabbage or wolf_eats_goat)

#tìm kiếm theo chiều sâu
def depth_first_search(start, is_goal, get_neighbors):
    parent = dict() #lưu trạng thái cha của mỗi trạng thái
    to_visit = [start] #khoi tao ngan xep, lưu các trạng thái chưa xét
    discovered = set([start]) #lưu các trạng thái đã xét

    while to_visit:
        vertex = to_visit.pop() #lấy 1 trạng thái từ ngăn xếp
        if is_goal(vertex): #kiểm tra trạng thái đó có phải trạng thái kết thúc không
            path = [] #lưu đường đi từ trạng thái đầu đến trạng thái kết thúc
            while vertex is not None: #truy vết từ trạng thái kết thúc về trạng thái đầu
                path.insert(0, vertex) #thêm trạng thái vào đầu đường đi
                vertex = parent.get(vertex) #cap nhat dinh hien tai la  trạng thái cha của trạng thái hiện tại
            return path
        
        for neighbor in get_neighbors(vertex): #lấy các trạng thái kề của trạng thái hiện tại
            if neighbor not in discovered and is_valid(neighbor): #kiểm tra trạng thái kề có hợp lệ không
                discovered.add(neighbor) #đánh dấu trạng thái kề đã xét
                parent[neighbor] = vertex #dat hien tai lam dinh cha
                to_visit.append(neighbor) #thêm trạng thái kề vào ngăn xếp

#dinh nghia trang thai ban dau va trang thai muc tieu
start_state = State(man=Location.A, cabbage=Location.A, goat=Location.A, wolf=Location.A)
goal_state = State(man=Location.B, cabbage=Location.B, goat=Location.B, wolf=Location.B)

#dinh nghia ham lay cac trang thai ke tiep
def get_neighbors(state):
    neighbors = []
    for obj in ['man', 'cabbage', 'goat', 'wolf']:
        if getattr(state, obj) == state.man: #neu doi tuong dang o cung vi tri voi nguoi dan on
            new_location = Location.A if state.man == Location.B else Location.B #xac dinh vi tri nguoi dan ong va doi tuong
            new_State = State(**{k: new_location if k == obj or k == 'man' else v for k, v in state._asdict().items()}) #cap nhat trang thai moi
            neighbors.append(new_State) #tao mot trang thai moi voi nguoi dan ong va doi tuong o vi tri moi, con lai giu nguyen
    return neighbors

#tim duong di
path = depth_first_search(start=start_state, is_goal=goal_state.__eq__, get_neighbors=get_neighbors)

#in ra duong di
for state in path:
    print(state)