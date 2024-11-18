#hàm phủ trả về logic phủ
def phu(x):                   #hàm này trả về logic phủ của logic
  tam = x.copy()              #Lấy bản sao của biến x, tránh thay đổi trực tiếp biến đầu vào
  if tam[0][0] == '-':        #ví dụ: input: a(x, y) => output: -a(x, y)
    tam[0] = tam[0][1:]       #ví dụ: input: -a(x, y) => output: a(x, y)
  else:
    tam[0] = '-' + tam[0]
  return tam

#Hàm đổi biến
def doibien(tap_vitu, tap_doi):                 #Hàm này có tác dụng đổi biến của một tập logic vị từ
  tap_vidu_new = []                             #tạo list chứa tập hợp logic sau khi đổi biến                      
  for vitu in tap_vitu:                         #xét từng logic
    vitu_new = [vitu[0], vitu[1][:]]            #tạo logic bản sao
    for i in range(len(vitu[1])):               #xét từng biến trong logic
      for j in range(len(tap_doi)):             #xét từng cặp biến đổi
        if vitu[1][i] == tap_doi[j][0]:          #nếu biến trong logic trùng với biến đổi
          vitu_new[1][i] = tap_doi[j][1]         #đổi biến trong logic
    tap_vidu_new.append(vitu_new)               #thêm logic mới vào tập hợp logic
  return tap_vidu_new                           #trả về tập hợp logic mới


#hàm res trả về res (a,b)
def res(a, b, bien, giaTri):                     #Viết hàm để recuse a và b
  ans = []                                       #tạo biến ans  
  for i in a:                                    #xét từng logic trong a 
    if i not in ans:                             #nếu logic không có trong ans
      ans.append(i)                              #thêm logic vào ans, tránh trùng lặp          
  check = False                                 #tạo biến check = False, kiểm tra xem với a và b có chứa 2 logic là phủ của nhau không
  for i in b:                                   #xét từng logic trong b
    if i in ans:                                #nếu logic có trong ans
      continue                                  #bỏ qua
    tam = phu(i)                                #lấy logic phủ của logic i
    if tam in ans:                              #nếu logic phủ của i có trong ans
      ans.remove(tam)                           #xóa logic phủ của i trong ans
      check = True                              #gán check = True             
    else:                                       #ngược lại
      ans.append(i)                             #thêm logic i vào ans
    # print("ans = ", ans, check)
  if check:                                     #nếu check = True, res có thể loại bỏ được ít nhất 1 cặp logic
    return sorted(ans), None                    #sắp xếp ans và trả về ans, None
  tap_ketqua = []                               #tạo tập tap_ketqua lưu kết quả
  tap_doi = []                                  #tạo tập tap_doi lưu cặp biến đổi
  vitu_chon = []                                #tạo tập vitu_chon lưu logic chọn
  for i in ans:                                 #xét từng logic trong ans
    for j in i[1]:                              #kiểm tra phần biến của logic vị từ
      if j in giaTri:                           #nếu biến có trong tập biến giá trị
        vitu_chon.append(i)                     #thêm logic vào vitu_chon
        break                                   #thoát khỏi vòng lặp
  # print("vitu_chon = ", vitu_chon)          #ưu tiên chọn ra các vị từ đã có sẵn trong giá trị như ['P', ['x', 'cothe']]  
                                              #với 'x' là biến, 'cothe' là giá trị 

  for i in vitu_chon:                           #xét từng logic trong vitu_chon
    hang_doi = []                               #tạo tập hang_doi lưu cặp biến đổi
    for j in ans:
      if i[0] == '-' + j[0] or '-' + i[0] == j[0]: #nếu vị từ đó trái dấu với vị trừ đang xét: tăng khả năng có thể res
        check = True
        for k in range(len(i[1])):               #xét từng biến trong vị từ
          if ((j[1][k] in giaTri) and (i[1][k] in giaTri) or (j[1][k] in bien and i[1][k] in bien)) and j[1][k] != i[1][k]:
            check = False                        #nếu các cặp biến tương ứng đều nằm trong tập giá trị hoặc biến và khác nhau
            break
        if check:                                #nếu check = True
          hang_doi.append(j)
          # print('i=', i); print("hang_doi = ", hang_doi)
    for j in hang_doi:
      doi = []
      da_the = []
      for k in range(len(j[1])):
        if i[1][k] in giaTri and j[1][k] not in giaTri and j[1][k] not in da_the:     #nếu biến vị từ đã chọn là gtri và biến vị từ đợi không là giá trị và biến này chưa được thế
          doi.append([j[1][k], i[1][k]])                                              
          da_the.append(j[1][k])
        elif i[1][k] not in giaTri and j[1][k] in giaTri and i[1][k] not in da_the:    #nếu biến vị từ đã chọn và vị từ đợi khác nhau và chưa được thế
          doi.append([i[1][k], j[1][k]])
          da_the.append(i[1][k])

      a_new = doibien(a, doi)    
      b_new = doibien(b, doi)
      tmp1, tmp2 = res(a_new, b_new, bien, giaTri)
      tap_ketqua.append(sorted(tmp1))
      tap_doi.append(doi)
    return tap_ketqua, tap_doi                                                   
  
#hàm tạo logic vị từ
def tao_vitu(tap_vitu):
  tam = []
  for i in range(len(tap_vitu)):
    a = (', ').join(tap_vitu[i][1])
    a = tap_vitu[i][0] + '(' + a + ')'
    tam.append(a)
  tam = (' v ').join(tam)
  return tam
  
#hàm tạo phép thế
def tao_phep_the(doi):
  tam = doi.copy()
  for i in range(len(tam)):
    tam[i] = (' = ').join(tam[i])
  tam = (', ').join(tam)
  return tam

#hàm robinson
def robison(TAP, bien, giaTri):
  so = 1
  my_dict = {}
  for vitu in TAP:
    my_dict[so] = vitu
    so += 1

  for key, val in my_dict.items():
    print("{:>3}.{}".format(key, tao_vitu(val)))
  
  da_duyet = set()
  i = 1
  while i < so:
    for j in list(my_dict.keys())[i:]:
      if (i, j) not in da_duyet:
        dong_moi, tap_doi = res(my_dict[i], my_dict[j], bien, giaTri)
        da_duyet.update({(i, j)})
        if tap_doi is None:
          if not dong_moi:
            print("{:>3}.Res({:>2}, {:>3}) = {}.".format(so, i, j, '[]'))
            print("=> Điều phải chứng minh.")
            return True
          if dong_moi not in my_dict.values():
            my_dict[so] = dong_moi
            print("{:>3}.Res({:>2}, {:>3}) = {}.".format(so, i, j, tao_vitu(dong_moi)))
            so += 1
          continue
        for k in range(len(dong_moi)):
          if not dong_moi[k]:
            print("{:>3}. Res({:>2}, {:>3}) = {}. Thế ({})".format(so, i, j, [], tao_phep_the(tap_doi[k])))
            print("=> Điều phải chứng minh.")
            return True
          if dong_moi[k] not in my_dict.values():
            my_dict[so] = dong_moi[k]
            print("{:>3}.Res({:>2}, {:>3}) = {}. Thế ({})".format(so, i, j, tao_vitu(dong_moi[k]), tao_phep_the(tap_doi[k])))
            da_duyet.update({(i, so), (j, so)})
            so += 1
    i += 1
    return False
  
#xử lý đầu vào
def xulyDauVao(dong):
  dong = dong.replace(' ', '')
  dong = dong + ','
  dong = dong.split('),')
  dong = [i + ')' for i in dong][:-1]
  for i in range(len(dong)):
    dong[i] = dong[i].split('v')
    dong[i] = [j[:-1].split('(') for j in dong[i]]
    for j in range(len(dong[i])):
      dong[i][j][1] = dong[i][j][1].split(',')
  return dong

#main
TAP = '-chame(x,y) v -chame(x,z) v anhem[y,z], -chame(x,y) v -chame(z,t) v -anhem(x,z) v anhem(y,t), -anhem(x,y) v anhem(y,x), chame(B,N), chame(T,D), chame(A,B), chame(A,T), -anhem(N,D)'
bien = ['x', 'y', 'z', 't']
giaTri = ['A', 'B','N', 'T', 'D']

#chạy ctrinh
TAP = xulyDauVao(TAP)
print(TAP)
robison(TAP, bien, giaTri)
                  