def nhanvien():
    logged_in = False
    while logged_in == False:
        login_pass = input("Mật khẩu: ")
        if login_pass == "112233":
            print('Thành Công!')
            return logged_in == True
        else:
            print('Mật khẩu sai!')
            print()

def quanli():
    logged_in = False
    while logged_in == False:
        login_pass = input("Mật khẩu: ")
        if login_pass == "123456":
            print('Thành Công!')
            logged_in = True
        else:
            print('Mật khẩu sai!')
            print()

x="y" #khai báo biến cục bộ cho cả while ( 26 )

print("THE SPACE COFFEE"
      "\n[Xanh sạch đẹp]")
what = False #Khai báo bằng F để định nghĩa trước gtrj
while what >= 0:
    print()
    print("Bạn là???")
    print("Nhập 1 nếu bạn là Khách hàng")
    print("Nhập 2 nếu bạn là Nhân viên")
    print("Nhập 3 nếu bạn là Quản lí")
    print("Nhập 0 để Thoát")
    print()
    while (x != "0"):
        what = int(input("Chọn chức năng mà bạn muốn thực hiện: "))
        if what == 0:
            break
        if what == 1:
            gioithieu = []
            details = open("gt.txt", encoding="utf8")
            no_items = int((details.readline()).rstrip("\n"))
            for i in range(0, no_items):
                line = (details.readline().rstrip("\n"))
                gioithieu.append(line)

            sanpham = []
            details = open("sp.txt", encoding="utf8")
            no_items = int((details.readline()).rstrip("\n"))
            for i in range(0, no_items):
                line = (details.readline().rstrip("\n"))
                sanpham.append(line)

            ctkm = []
            details = open("ctkm.txt", encoding="utf8")
            no_items = int((details.readline()).rstrip("\n"))
            for i in range(0, no_items):
                line = (details.readline().rstrip("\n"))
                ctkm.append(line)

            cuahang = []
            details = open("ch.txt", encoding="utf8")
            no_items = int((details.readline()).rstrip("\n"))
            for i in range(0, no_items):
                line = (details.readline().rstrip("\n"))
                cuahang.append(line)

            tuyendung = []
            details = open("td.txt", encoding="utf8")
            no_items = int((details.readline()).rstrip("\n"))
            for i in range(0, no_items):
                line = (details.readline().rstrip("\n"))
                tuyendung.append(line)

            nq = []
            details = open("nq.txt", encoding="utf8")
            no_items = int((details.readline()).rstrip("\n"))
            for i in range(0, no_items):
                line = (details.readline().rstrip("\n"))
                nq.append(line)
            print()
            print(" ~~ Welcome to COFFEE ~~ ")
            print()
            print("A - Giới thiệu ")
            print("B - Sản phẩm ")
            print("C - Chương trình khuyến mãi ")
            print("D - Chuỗi cửa hàng ")
            print("E - Tuyển dụng ")
            print("F - Nhượng quyền ")
            print("Q - Thoát ")
            while (x != "q" or x != "Q"):
                c = input(" \nBạn cần gì? ")

                if (c == "q" or c == "Q"):
                    print()
                    break
                elif (c == "A" or c == "a"):
                    print()
                    for i in range(0, len(gioithieu)):
                        print('',gioithieu[i])
                elif (c == "B" or c == "b"):
                    print()
                    for i in range(0, len(sanpham)):
                        print('', sanpham[i])
                elif (c == 'C' or c == 'c'):
                    print()
                    for i in range(0, len(ctkm)):
                        print('', ctkm[i])
                elif (c == "D" or c == "d"):
                    print()
                    for i in range(0, len(cuahang)):
                        print('', cuahang[i])
                elif (c == "E" or c == "e"):
                    print()
                    for i in range(0, len(tuyendung)):
                        print('', tuyendung[i])
                elif (c == "F" or c == "f"):
                    print()
                    for i in range(0, len(nq)):
                        print('', nq[i])
                else:
                    print("Câu trả lời không đúng cú pháp vui lòng nhập lại")
            print("Cám ơn xin hẹn gặp lại")
            print()
            print("Bạn là???")
            print("Nhập 1 nếu bạn là Khách hàng")
            print("Nhập 2 nếu bạn là Nhân viên")
            print("Nhập 3 nếu bạn là Quản lí")
            print("Nhập 0 để Thoát")
            print()
        elif what == 2:
            print()
            nhanvien()
            print()
            print(" ~~ Welcome to HOME ~~ ")
            print()
            print("A - Thông tin cá nhân ")
            print("B - Bảng chấm lương ")
            print("Q - Thoát ")
            while (x != "q" or x != "Q"):
                c = input(" \nBạn cần gì? ")
                if (c == "q" or c == "Q"):
                    break
                elif (c == "A" or c == "a"):

                    name = {}
                    sex = {}
                    SDT = {}
                    CCCD = {}
                    STK = {}
                    place = {}

                    details = open("qlnv.txt", encoding="utf8")

                    no_items = int((details.readline()).rstrip("\n"))

                    for i in range(0, no_items):
                        line = (details.readline()).rstrip("\n")
                        x1, x2 = line.split("#")
                        x1 = int(x1)
                        name.update({x1: x2})

                    for i in range(0, no_items):
                        line = (details.readline()).rstrip("\n")
                        x1, x2 = line.split("#")
                        x1 = int(x1)
                        sex.update({x1: x2})

                    for i in range(0, no_items):
                        line = (details.readline()).rstrip("\n")
                        x1, x2 = line.split("#")
                        x1 = int(x1)
                        SDT.update({x1: x2})

                    for i in range(0, no_items):
                        line = (details.readline()).rstrip("\n")
                        x1, x2 = line.split("#")
                        x1 = int(x1)
                        CCCD.update({x1: x2})

                    for i in range(0, no_items):
                        line = (details.readline()).rstrip("\n")
                        x1, x2 = line.split("#")
                        x1 = int(x1)
                        STK.update({x1: x2})

                    for i in range(0, no_items):
                        line = (details.readline()).rstrip("\n")
                        x1, x2 = line.split("#")
                        x1 = int(x1)
                        place.update({x1: x2})

                    details.close()
                    print()
                    p_id=int(input("Nhập mã nhân viên của bạn :"))
                    print()
                    print(" THÔNG TIN NHÂN VIÊN ")
                    if p_id in name:
                        print(" Mã nhân viên | ", p_id)
                        print(" Tên nhân viên | ", name.get(p_id))
                        print(" Giới tính nhân viên | ", sex.get(p_id))
                        print(" SDT nhân viên | ", SDT.get(p_id))
                        print(" CCCD nhân viên | ", CCCD.get(p_id))
                        print(" STK nhân viên | ", STK.get(p_id))
                        print(" Nơi ở nhân viên | ", place.get(p_id))
                        print("----------")
                    else:
                        print()
                        print("Không có nhân viên này! "
                              "Vui lòng liên hệ sdt: 123456789 ")

                elif (c == "B" or c == "b"):
                    id = {}
                    bl = {}
                    mon = {}

                    details = open("blc.txt", encoding="utf8")
                    no_items = int((details.readline()).rstrip("\n"))

                    for i in range(0, no_items):
                        line = (details.readline()).rstrip("\n")
                        x1, x2 = line.split("#")
                        x1 = int(x1)
                        x2 = int(x2)
                        id.update({x1: x2})

                    for i in range(0, no_items):
                        line = (details.readline()).rstrip("\n")
                        x1, x2 = line.split("#")
                        x1 = int(x1)
                        x2 = int(x2)
                        mon.update({x1: x2})

                    for i in range(0, no_items):
                        line = (details.readline()).rstrip("\n")
                        x1, x2 = line.split("#")
                        x1 = int(x1)
                        x2 = str(x2)
                        bl.update({x1: x2})

                    details.close()
                    print()
                    mnv = int(input("Nhập mã nhân viên của bạn :"))
                    print()
                    if mnv in id:
                        print(" ~~ Welcome to HOME ~~ ")
                        print()
                        print("A - Xem bảng lương theo tháng ")
                        print("B - Xem tất cả bảng lương ")
                        print("Q - Thoát ")
                        while (x != "q" or x != "Q"):
                            c = input(" \nBạn cần gì? ")

                            if (c == "q" or c == "Q"):
                                break

                            elif (c == "A" or c == "a"):
                                print()
                                y = int(input("Nhập tháng lương bạn muốn xem :"))
                                k = 0
                                a=[]
                                for i in range(0, no_items):
                                    k = id.get(i + 1)
                                    if k == mnv:
                                        a.append(i)
                                        if ((i in a) and (mon.get(i + 1) == y)):
                                            print()
                                            print(" Lương tháng ", mon.get(i + 1), " : ", bl.get(i + 1))

                            elif (c == "B" or c == "b"):
                                k = 0
                                a = []
                                print()
                                for i in range(0, no_items):
                                    k = id.get(i + 1)
                                    if k == mnv:
                                        a.append(i)
                                for i in a:
                                    print(" Lương tháng ", mon.get(i + 1), " : ", bl.get(i + 1))
                    else:
                        print("Không có nhân viên này! "
                              "Vui lòng liên hệ sdt: 123456789 ")
        elif what == 3:
            print()
            quanli()
            print()
            print(" ~~ Welcome to COFFEE ~~ ")
            print()
            print("A - Quản lý nhân viên ")
            print("B - Quản lý kho ")
            print("C - Quản lý doanh thu từng cơ sở ( nhập )")
            print("K - Quản lý doanh thu từng ngày ( tổng )")
            print("D - Quản lý chi tiêu ")
            print("E - Quản lý lợi nhuận ")
            print("Q - Thoát ")
            while (x != "q" or x != "Q"):
                d = input(" \nBạn cần gì? ")
                if (d == "q" or d == "Q"):
                    break
                elif (d == "A" or d == "a"):
                    print()
                    print("Quản lí nhân viên")
                    print()
                    print("A - Thông tin nhân viên ")
                    print("B - Bảng lương nhân viên ")
                    print("Q - Thoát ")
                    while (x != "q" or x != "Q"):
                        e = input(" \nBạn cần gì? ")
                        if (e == "q" or e == "Q"):
                            break
                        elif (e == "A" or e == "a"):

                            name = {}
                            sex = {}
                            SDT = {}
                            CCCD = {}
                            STK = {}
                            place = {}

                            details = open("qlnv.txt", encoding="utf8")
                            no_items = int((details.readline()).rstrip("\n"))

                            for i in range(0, no_items):
                                line = (details.readline()).rstrip("\n")
                                x1, x2 = line.split("#")
                                x1 = int(x1)
                                x2 = str(x2)
                                name.update({x1: x2})

                            for i in range(0, no_items):
                                line = (details.readline()).rstrip("\n")
                                x1, x2 = line.split("#")
                                x1 = int(x1)
                                x2 = str(x2)
                                sex.update({x1: x2})

                            for i in range(0, no_items):
                                line = (details.readline()).rstrip("\n")
                                x1, x2 = line.split("#")
                                x1 = int(x1)
                                x2 = int(x2)
                                SDT.update({x1: x2})

                            for i in range(0, no_items):
                                line = (details.readline()).rstrip("\n")
                                x1, x2 = line.split("#")
                                x1 = int(x1)
                                x2 = int(x2)
                                CCCD.update({x1: x2})

                            for i in range(0, no_items):
                                line = (details.readline()).rstrip("\n")
                                x1, x2 = line.split("#")
                                x1 = int(x1)
                                x2 = int(x2)
                                STK.update({x1: x2})

                            for i in range(0, no_items):
                                line = (details.readline()).rstrip("\n")
                                x1, x2 = line.split("#")
                                x1 = int(x1)
                                x2 = str(x2)
                                place.update({x1: x2})

                            details.close()

                            cart = []
                            c = "y"
                            print()
                            print("A - Nhập thông tin nhân viên")
                            print("B - Xóa thông tin nhân viên")
                            print("C - Chỉnh sửa thông tin nhân viên")
                            print("D - Danh sách nhân viên")
                            print("E - Tìm kiếm thông tin nhân viên")
                            print("Q - Thoát ")
                            print("help - Xem lại tất cả các lệnh")

                            total_cost = 0
                            flag = 0

                            while (c != "q" or c != "Q"):
                                c = input(" \nBạn cần gì? ")
                                if (c == "q" or c == "Q"):
                                    print()
                                    print("Bạn đã hoàn thành công cụ quản lí nhân viên")
                                    break
                                elif (c == "A" or c == "a"):
                                    print()
                                    p_id = int(input(" Nhập mã nhân viên : "))
                                    p_name = str(input(" Nhập tên nhân viên : "))
                                    p_sex = str(input(" Nhập giới tính nhân viên : "))
                                    p_SDT = int(input(" Nhập số điện thoại nhân viên : "))
                                    p_CCCD = int(input(" Nhập số CCCD nhân viên : "))
                                    p_STK = int(input(" Nhập STK nhân viên : "))
                                    p_place = str(input(" Nhập nơi ở nhân viên : "))

                                    m = 0
                                    for i in range(0, len(name)):
                                        if (p_id in name):
                                            p_id += 1
                                            m = 1
                                    if (m == 1):
                                        print()
                                        print(" Mã nhân viên đó đã tồn tại :< thay đổi thành mã nhân viên : ", p_id)

                                    name.update({p_id: p_name})
                                    sex.update({p_id: p_sex})
                                    SDT.update({p_id: p_SDT})
                                    CCCD.update({p_id: p_CCCD})
                                    STK.update({p_id: p_STK})
                                    place.update({p_id: p_place})

                                    details = open("qlnv.txt", "w", encoding="utf8")
                                    no_items = len(name)
                                    details.write(str(no_items) + "\n")

                                    for p_id in name:
                                        details.write(str(p_id) + "#" + name[p_id] + "\n")

                                    for p_id in name:
                                        details.write(str(p_id) + "#" + sex[p_id] + "\n")

                                    for p_id in name:
                                        details.write(str(p_id) + "#" + str(SDT[p_id]) + "\n")

                                    for p_id in name:
                                        details.write(str(p_id) + "#" + str(CCCD[p_id]) + "\n")

                                    for p_id in name:
                                        details.write(str(p_id) + "#" + str(STK[p_id]) + "\n")

                                    for p_id in name:
                                        details.write(str(p_id) + "#" + place[p_id] + "\n")

                                    print()
                                    print("Mã nhân viên : ", p_id, " Tên nhân viên : ", name.get(p_id),
                                          " Giới tính nhân viên : ",
                                          sex.get(p_id), " SDT nhân viên : ", SDT.get(p_id), " \nSố CCCD nhân viên : ",
                                          CCCD.get(p_id), " STK nhân viên : ", STK.get(p_id), " Nơi ở nhân viên : ",
                                          place.get(p_id))
                                    print()
                                    print(" Thông tin nhân viên đã đươc nhập thành công !")
                                    print()
                                elif (c == "C" or c == "c"):  # Edit a part
                                    print()
                                    p_id = int(input(" Nhập mã nhân viên : "))
                                    if (p_id in name):
                                        p_name = str(input(" Nhập lại tên nhân viên : "))
                                        p_sex = str(input(" Nhập lại giới tính nhân viên : "))
                                        p_SDT = int(input(" Nhập lại số điện thoại nhân viên : "))
                                        p_CCCD = int(input(" Nhập lại số CCCD nhân viên : "))
                                        p_STK = int(input(" Nhập lại STK nhân viên : "))
                                        p_place = str(input(" Nhập lại nơi ở nhân viên : "))

                                        name.update({p_id: p_name})
                                        sex.update({p_id: p_sex})
                                        SDT.update({p_id: p_SDT})
                                        CCCD.update({p_id: p_CCCD})
                                        STK.update({p_id: p_STK})
                                        place.update({p_id: p_place})

                                        print()
                                        print("Mã nhân viên : ", p_id, " Tên nhân viên : ", name.get(p_id),
                                              " Giới tính nhân viên : ",
                                              sex.get(p_id), " SDT nhân viên : ", SDT.get(p_id),
                                              " Số CCCD nhân viên : ",
                                              CCCD.get(p_id), " \nSTK nhân viên : ", STK.get(p_id),
                                              " Nơi ở nhân viên : ",
                                              place.get(p_id))
                                        print()
                                        print(" Thông tin nhân viên đã đươc cập nhập thành công !")
                                        print()

                                        details = open("qlnv.txt", "w", encoding="utf8")
                                        no_items = len(name)
                                        details.write(str(no_items) + "\n")

                                        for p_id in name:
                                            details.write(str(p_id) + "#" + name[p_id] + "\n")

                                        for p_id in name:
                                            details.write(str(p_id) + "#" + sex[p_id] + "\n")

                                        for p_id in name:
                                            details.write(str(p_id) + "#" + str(SDT[p_id]) + "\n")

                                        for p_id in name:
                                            details.write(str(p_id) + "#" + str(CCCD[p_id]) + "\n")

                                        for p_id in name:
                                            details.write(str(p_id) + "#" + str(STK[p_id]) + "\n")

                                        for p_id in name:
                                            details.write(str(p_id) + "#" + place[p_id] + "\n")
                                        details.close()
                                    else:
                                        print()
                                        print(" Thông tin nhân viên đó không tồn tại, để nhập thông tin một nhân viên mới, hãy sử dụng phím A")
                                        print()
                                elif (c == "b" or c == "B"):  # Remove a part
                                    print()
                                    p_id = int(input(" Nhập mã nhân viên : "))
                                    if (p_id in name):
                                        print()
                                        are_you_sure = input(" Bạn có chắc muốn xóa thông tin nhân viên đó không ? ( y/n )")
                                        if (are_you_sure == "y" or are_you_sure == "Y"):
                                            name.pop(p_id)
                                            sex.pop(p_id)
                                            SDT.pop(p_id)
                                            CCCD.pop(p_id)
                                            STK.pop(p_id)
                                            place.pop(p_id)

                                            details = open("qlnv.txt", "w", encoding="utf8")
                                            no_items = len(name)
                                            details.write(str(no_items) + "\n")

                                            for p_id in name:
                                                details.write(str(p_id) + "#" + name[p_id] + "\n")

                                            for p_id in name:
                                                details.write(str(p_id) + "#" + sex[p_id] + "\n")

                                            for p_id in name:
                                                details.write(str(p_id) + "#" + str(SDT[p_id]) + "\n")

                                            for p_id in name:
                                                details.write(str(p_id) + "#" + str(CCCD[p_id]) + "\n")

                                            for p_id in name:
                                                details.write(str(p_id) + "#" + str(STK[p_id]) + "\n")

                                            for p_id in name:
                                                details.write(str(p_id) + "#" + place[p_id] + "\n")
                                            print()
                                            print(" Thông tin nhân viên này đã được xóa thành công!")
                                        print()
                                    else:
                                        print()
                                        print(" Xin lỗi, chúng tôi không có một thông tin nhân viên như vậy!")
                                        print()
                                elif (c == "D" or c == "d"):
                                    print()# List all the parts
                                    print(" Danh sách thông tin nhân viên ")
                                    print()
                                    for p_id in name:
                                        print(" Mã nhân viên | ", p_id)
                                        print(" Tên nhân viên | ", name.get(p_id))
                                        print(" Giới tính nhân viên | ", sex.get(p_id))
                                        print(" SDT nhân viên | ", SDT.get(p_id))
                                        print(" CCCD nhân viên | ", CCCD.get(p_id))
                                        print(" STK nhân viên | ", STK.get(p_id))
                                        print(" Nơi ở nhân viên | ", place.get(p_id))
                                        print("----------")
                                elif (c == "E" or c == "e"):
                                    print()
                                    p_id = int(input("Nhập mã nhân viên bạn cần tìm :"))
                                    print()
                                    if p_id in name:
                                        print(" Mã nhân viên | ", p_id)
                                        print(" Tên nhân viên | ", name.get(p_id))
                                        print(" Giới tính nhân viên | ", sex.get(p_id))
                                        print(" SDT nhân viên | ", SDT.get(p_id))
                                        print(" CCCD nhân viên | ", CCCD.get(p_id))
                                        print(" STK nhân viên | ", STK.get(p_id))
                                        print(" Nơi ở nhân viên | ", place.get(p_id))
                                        print("----------")
                                    else:
                                        print("Không có nhân viên này! "
                                              "Vui lòng nhấn phím A để tạo thông tin nhân viên ")
                                elif (c == "help"):  # Display all commands
                                    print("Quản lí nhân viên")
                                    print()
                                    print("A - Nhập thông tin nhân viên")
                                    print("B - Xóa thông tin nhân viên")
                                    print("C - Chỉnh sửa thông tin nhân viên")
                                    print("D - Danh sách nhân viên")
                                    print("E - Tìm kiếm thông tin nhân viên")
                                    print("Q - Thoát ")
                                    print("help - Xem lại tất cả các lệnh")
                                    print()
                                    print(
                                        "Nếu bạn có bất kỳ câu hỏi hoặc thắc mắc nào khác, vui lòng liên hệ sdt: 123456789 ")
                                    print()

                            details = open("qlnv.txt", "w", encoding="utf8")
                            no_items = len(name)
                            details.write(str(no_items) + "\n")

                            for p_id in name:
                                details.write(str(p_id) + "#" + name[p_id] + "\n")

                            for p_id in name:
                                details.write(str(p_id) + "#" + sex[p_id] + "\n")

                            for p_id in name:
                                details.write(str(p_id) + "#" + str(SDT[p_id]) + "\n")

                            for p_id in name:
                                details.write(str(p_id) + "#" + str(CCCD[p_id]) + "\n")

                            for p_id in name:
                                details.write(str(p_id) + "#" + str(STK[p_id]) + "\n")

                            for p_id in name:
                                details.write(str(p_id) + "#" + place[p_id] + "\n")

                            details.close()

                        elif (e == "B" or e == "b"):
                            id = {}
                            bl = {}
                            mon = {}

                            details = open("blc.txt", encoding="utf8")
                            no_items = int((details.readline()).rstrip("\n"))

                            for i in range(0, no_items):
                                line = (details.readline()).rstrip("\n")
                                x1, x2 = line.split("#")
                                x1 = int(x1)
                                x2 = int(x2)
                                id.update({x1: x2})

                            for i in range(0, no_items):
                                line = (details.readline()).rstrip("\n")
                                x1, x2 = line.split("#")
                                x1 = int(x1)
                                x2 = int(x2)
                                mon.update({x1: x2})

                            for i in range(0, no_items):
                                line = (details.readline()).rstrip("\n")
                                x1, x2 = line.split("#")
                                x1 = int(x1)
                                x2 = str(x2)
                                bl.update({x1: x2})

                            details.close()
                            cart = []
                            c = "y"

                            print()
                            print("Bảng lương nhân viên")
                            print()
                            print("A - Nhập bảng lương nhân viên")
                            print("B - Xóa bảng lương nhân viên")
                            print("C - Chỉnh sửa bảng lương nhân viên")
                            print("D - Danh sách bảng lương nhân viên")
                            print("E - Tìm kiếm bảng lương nhân viên")
                            print("Q - Thoát ")
                            print("help - Xem lại tất cả các lệnh")
                            print()

                            total_cost = 0
                            flag = 0

                            while (c != "q" or c != "Q"):
                                c = input(" Bạn cần gì? ")
                                if (c == "q" or c == "Q"):
                                    print()
                                    print("Bạn đã hoàn thành công cụ quản lí bảng lương nhân viên")
                                    break
                                elif (c == "A" or c == "a"):  # Add a part
                                    p_stt = int(input(" Nhập số thứ tự : "))
                                    p_id = int(input(" Nhập mã nhân viên : "))
                                    p_mon = int(input(" Nhập tháng : "))
                                    p_bl = str(input(" Nhập lương nhân viên : "))

                                    m = 0
                                    for i in range(0, len(id)):
                                        if (p_stt in id):
                                            p_stt += 1
                                            m = 1
                                    if (m == 1):
                                        print()
                                        print(" Số thứ tự đó đã tồn tại :< thay đổi thành số thứ tự ", p_stt)

                                    id.update({p_stt: p_id})
                                    bl.update({p_stt: p_bl})
                                    mon.update({p_stt: p_mon})

                                    details = open("blc.txt", "w", encoding="utf8")
                                    no_items = len(id)
                                    details.write(str(no_items) + "\n")

                                    for i in range(0, no_items):
                                        details.write(str(i + 1) + "#" + str(id[i + 1]) + "\n")

                                    for i in range(0, no_items):
                                        details.write(str(i + 1) + "#" + str(mon[i + 1]) + "\n")

                                    for i in range(0, no_items):
                                        details.write(str(i + 1) + "#" + str(bl[i + 1]) + "\n")

                                    details.close()
                                    k=0
                                    z=1
                                    for i in range(0, no_items):
                                        if k != z:
                                            k = id.get(i + 1)
                                            print("Mã nhân viên ",k)
                                            for i in range(0, len(id)):
                                                if id.get(i + 1) == k:
                                                    print(" Lương tháng ",mon.get(i+1)," : ",bl.get(i+1))
                                                z = id.get(i + 1)
                                    print()
                                    print(" Thông tin bảng lương nhân viên đã đươc nhập !")
                                    print()
                                elif (c == "C" or c == "c"):  # Edit a part
                                    print()
                                    p_stt = int(input(" Nhập số thứ tự : "))
                                    if (p_stt in id):
                                        p_id = int(input(" Nhập lại mã nhân viên : "))
                                        p_mon = str(input(" Nhập lại tháng lương : "))
                                        p_bl = str(input(" Nhập lại lương nhân viên : "))

                                        id.update({p_stt: p_id})
                                        mon.update({p_stt: p_mon})
                                        bl.update({p_stt: p_bl})

                                        details = open("blc.txt", "w", encoding="utf8")
                                        no_items = len(id)
                                        details.write(str(no_items) + "\n")

                                        for i in range(0, no_items):
                                            details.write(str(i + 1) + "#" + str(id[i + 1]) + "\n")

                                        for i in range(0, no_items):
                                            details.write(str(i + 1) + "#" + str(mon[i + 1]) + "\n")

                                        for i in range(0, no_items):
                                            details.write(str(i + 1) + "#" + str(bl[i + 1]) + "\n")

                                        details.close()
                                    else:
                                        print(
                                            " Thông tin nhân viên đó không tồn tại, để nhập thông tin bảng lương nhân viên mới, hãy sử dụng phím A")
                                    print()
                                elif (c == "b" or c == "B"):  # Remove a part
                                    print()
                                    p_stt = int(input(" Nhập số thứ tự : "))
                                    if (p_stt in id):
                                        are_you_sure = input(" Bạn có chắc muốn xóa thông tin bảng lương nhân viên đó không ? ( y/n )")
                                        if (are_you_sure == "y" or are_you_sure == "Y"):
                                            id.pop(p_stt)
                                            bl.pop(p_stt)
                                            mon.pop(p_stt)

                                            details = open("blc.txt", "w", encoding="utf8")
                                            no_items = len(id)
                                            details.write(str(no_items) + "\n")

                                            for i in range(0, no_items):
                                                details.write(str(i + 1) + "#" + str(id[i + 1]) + "\n")

                                            for i in range(0, no_items):
                                                details.write(str(i + 1) + "#" + str(mon[i + 1]) + "\n")

                                            for i in range(0, no_items):
                                                details.write(str(i + 1) + "#" + str(bl[i + 1]) + "\n")

                                            details.close()

                                            print(" Thông tin nhân viên này đã được xóa thành công!")
                                        print()
                                    else:
                                        print(" Xin lỗi, chúng tôi không có một thông tin nhân viên như vậy!")
                                        print()
                                elif (c == "D" or c == "d"):  # List all the parts
                                    print(" Danh sách thông tin nhân viên ")
                                    k = 0
                                    z = 1
                                    for i in range(0, no_items):
                                        if k != z:
                                            k = id.get(i + 1)
                                            print("Mã nhân viên ", k)
                                            for i in range(0, len(id)):
                                                if id.get(i + 1) == k:
                                                    print(" Lương tháng ", mon.get(i + 1), " : ", bl.get(i + 1))
                                                z = id.get(i + 1)
                                    print()
                                elif (c == "E" or c == "e"):
                                    mnv = int(input("Nhập mã nhân viên của bạn :"))
                                    if mnv in id:
                                        print(" ~~ Welcome to HOME ~~ ")
                                        print()
                                        print("A - Xem bảng lương theo tháng ")
                                        print("B - Xem tất cả bảng lương ")
                                        print("Q - Thoát ")
                                        print()
                                        while (x != "q" or x != "Q"):
                                            c = input(" Bạn cần gì? ")

                                            if (c == "q" or c == "Q"):
                                                break

                                            elif (c == "A" or c == "a"):
                                                y = int(input("Nhập tháng lương bạn muốn xem :"))
                                                k = 0
                                                a = []
                                                for i in range(0, no_items):
                                                    k = id.get(i + 1)
                                                    if k == mnv:
                                                        a.append(i)
                                                        if ((i in a) and (mon.get(i + 1) == y)):
                                                            print(" Lương tháng ", mon.get(i + 1), " : ", bl.get(i + 1))

                                            elif (c == "B" or c == "b"):
                                                k = 0
                                                a = []
                                                for i in range(0, no_items):
                                                    k = id.get(i + 1)
                                                    if k == mnv:
                                                        a.append(i)
                                                for i in a:
                                                    print(" Lương tháng ", mon.get(i + 1), " : ", bl.get(i + 1))
                                    else:
                                        print("Không có lương tháng này! "
                                              "Vui lòng nhấn phím A để tạo thông tin bảng lương nhân viên ")
                                elif (c == "help"):  # Display all commands
                                    print("Bảng lương nhân viên")
                                    print()
                                    print("A - Nhập bảng lương nhân viên")
                                    print("B - Xóa bảng lương nhân viên")
                                    print("C - Chỉnh sửa bảng lương nhân viên")
                                    print("D - Danh sách bảng lương nhân viên")
                                    print("Q - Thoát ")
                                    print("help - Xem lại tất cả các lệnh")
                                    print()
                                    print(
                                        "Nếu bạn có bất kỳ câu hỏi hoặc thắc mắc nào khác, vui lòng liên hệ sdt: 123456789 ")
                                    print()

                            details = open("blc.txt", "w", encoding="utf8")
                            no_items = len(id)
                            details.write(str(no_items) + "\n")

                            for i in range(0, no_items):
                                details.write(str(i + 1) + "#" + str(id[i + 1]) + "\n")

                            for i in range(0, no_items):
                                details.write(str(i + 1) + "#" + str(mon[i + 1]) + "\n")

                            for i in range(0, no_items):
                                details.write(str(i + 1) + "#" + str(bl[i + 1]) + "\n")

                            details.close()
                elif (d == "B" or d == "b"):
                    print()
                    print("A - Nhập kho ")
                    print("B - Xuất kho ")
                    print("C - Tồn kho ")
                    print("Q - Thoát ")
                    while (x != "q" or x != "Q"):
                        e = input(" \nBạn cần gì? ")

                        if (e == "q" or e == "Q"):
                            break
                        elif (e == "A" or e == "a"):
                            unit_price = {}
                            description = {}
                            stock = {}
                            day = {}

                            details = open("nhapkho.txt", "r",encoding="utf8")                  # First line of the file is the number of items
                            no_items = int((details.readline()).rstrip("\n"))

                            for i in range(0, no_items):
                                line = (details.readline()).rstrip("\n")
                                x1, x2 = line.split("#")
                                x1 = int(x1)
                                x2 = str(x2)
                                day.update({x1: x2})

                            for i in range(0, no_items):
                                line = (details.readline()).rstrip("\n")
                                x1, x2 = line.split("#")
                                x1 = int(x1)
                                x2 = float(x2)
                                unit_price.update({x1: x2})

                            for i in range(0, no_items):
                                line = (details.readline()).rstrip("\n")
                                x1, x2 = line.split("#")
                                x1 = int(x1)
                                description.update({x1: x2})

                            for i in range(0, no_items):
                                line = (details.readline()).rstrip("\n")
                                x1, x2 = line.split("#")
                                x1 = int(x1)
                                x2 = int(x2)
                                stock.update({x1: x2})

                            details.close()

                            cart = []

                            c = "y"  # Runs the while loop as long as user wants
                            print()
                            print("Nhập kho")
                            print()
                            print("A - Nhập sản phẩm")
                            print("R - Xóa sản phẩm")
                            print("E - Chỉnh sửa sản phầm")
                            print("L - Danh sách nhập kho ( theo thứ tự nhập )")
                            print("B - Danh sách nhập kho ( theo sản phẩm )")
                            print("C - Danh sách nhập kho ( theo ngày )")
                            print("D - Danh mục sản phẩm nhập kho ( tổng )")
                            print("Q - Thoát ")
                            print("help - Xem lại tất cả các lệnh")
                            print()

                            total_cost = 0
                            flag = 0  # To check if they have checked out

                            while (c != "q" or c != "Q"):
                                c = input(" Bạn cần gì? ")
                                if (c == "q" or c == "Q"):
                                    print()
                                    print("Bạn đã nhập kho thành công")
                                    break
                                elif (c == "A" or c == "a"):  # Add a part
                                    p_day = str(input(" Nhập thời gian xuất kho (dd.mm.yy) : "))
                                    p_no = int(input(" Nhập số thứ tự sản phẩm : "))
                                    p_pr = float(input(" Nhập giá tiền sản phẩm : "))
                                    p_desc = str(input(" Nhập tên sản phẩm : "))
                                    p_stock = int(input(" Số lượng sản phẩm : "))

                                    m = 0
                                    for i in range(0, len(unit_price)):
                                        if (p_no in unit_price):
                                            p_no += 1
                                            m = 1
                                    if (m == 1):
                                        print()
                                        print(" Số thứ tự đó đã tồn tại :< thay đổi thành số thứ tự ", p_no)
                                    day.update({p_no: p_day})
                                    unit_price.update({p_no: p_pr})
                                    description.update({p_no: p_desc})
                                    if (p_stock > -1):
                                        stock.update({p_no: p_stock})
                                    else:
                                        p_stock = 0
                                        stock.update({p_no: p_stock})
                                        print(
                                            " Số lượng của một sản phẩm không được âm, số lượng sản phẩm này đã được đặt thành 0.")
                                    print()
                                    print("Thời gian xuất kho : ", day.get(p_no), " Số thứ tự sản phẩm : ", p_no,
                                          " Tên sản phẩm : ", description.get(p_no), " Giá tiền sản phẩm : ",
                                          unit_price.get(p_no), " Số lượng sản phẩm : ", stock.get(p_no))
                                    print(" Sản phẩm đã được nhập kho thành công !")
                                    print()

                                    details = open("nhapkho.txt", "w", encoding="utf8")
                                    no_items = len(unit_price)
                                    details.write(str(no_items) + "\n")
                                    for i in range(0, no_items):
                                        details.write(str(i + 1) + "#" + str(day[i + 1]) + "\n")

                                    for i in range(0, no_items):
                                        details.write(str(i + 1) + "#" + str(unit_price[i + 1]) + "\n")

                                    for i in range(0, no_items):
                                        details.write(str(i + 1) + "#" + description[i + 1] + "\n")

                                    for i in range(0, no_items):
                                        details.write(str(i + 1) + "#" + str(stock[i + 1]) + "\n")
                                elif (c == "E" or c == "e"):  # Edit a part
                                    print()
                                    p_no = int(input(" Nhập số thứ tự sản phẩm : "))
                                    if (p_no in unit_price):
                                        p_day = str(input(" Nhập lại thời gian xuất kho (dd.mm.yy) : "))
                                        p_pr = float(input(" Nhập lại giá tiền sản phẩm: "))
                                        p_desc = input(" Nhập lại tên sản phẩm : ")
                                        p_stock = int(input(" Nhập lại số lượng sản phẩm : "))
                                        day.update({p_no: p_day})
                                        unit_price.update({p_no: p_pr})
                                        description.update({p_no: p_desc})
                                        stock.update({p_no: p_stock})

                                        details = open("nhapkho.txt", "w", encoding="utf8")
                                        no_items = len(unit_price)
                                        details.write(str(no_items) + "\n")
                                        for i in range(0, no_items):
                                            details.write(str(i + 1) + "#" + str(day[i + 1]) + "\n")

                                        for i in range(0, no_items):
                                            details.write(str(i + 1) + "#" + str(unit_price[i + 1]) + "\n")

                                        for i in range(0, no_items):
                                            details.write(str(i + 1) + "#" + description[i + 1] + "\n")

                                        for i in range(0, no_items):
                                            details.write(str(i + 1) + "#" + str(stock[i + 1]) + "\n")

                                    else:
                                        print(" Sản phẩm đó không tồn tại, để nhập một sản phẩm, hãy sử dụng phím A")
                                    print()
                                elif (c == "R" or c == "r"):  # Remove a part
                                    print()
                                    p_no = int(input(" Nhập số thứ tự sản phẩm : "))
                                    if (p_no in unit_price):
                                        are_you_sure = input(" Bạn có chắc muốn xóa sản phẩm đó không ? ( y/n )")
                                        if (are_you_sure == "y" or are_you_sure == "Y"):
                                            unit_price.pop(p_no)
                                            description.pop(p_no)
                                            stock.pop(p_no)
                                            day.pop(p_no)

                                            details = open("nhapkho.txt", "w", encoding="utf8")
                                            no_items = len(unit_price)
                                            details.write(str(no_items) + "\n")
                                            for i in range(0, no_items):
                                                details.write(str(i + 1) + "#" + str(day[i + 1]) + "\n")

                                            for i in range(0, no_items):
                                                details.write(str(i + 1) + "#" + str(unit_price[i + 1]) + "\n")

                                            for i in range(0, no_items):
                                                details.write(str(i + 1) + "#" + description[i + 1] + "\n")

                                            for i in range(0, no_items):
                                                details.write(str(i + 1) + "#" + str(stock[i + 1]) + "\n")

                                            print(" Sản phẩm đã được xóa thành công!")
                                        print()
                                    else:
                                        print(" Xin lỗi, chúng tôi không có một sản pẩm như vậy!")
                                        print()
                                elif (c == "L" or c == "l"):
                                    print()# List all the parts
                                    print(" Danh sách nhập kho ( theo thứ tự nhập ) ")
                                    print()
                                    print("A - Tìm kiếm ")
                                    print("B - Xem tất cả ")
                                    print("Q - Thoát ")
                                    while (x != "q" or x != "Q"):
                                        c = input(" \nBạn cần gì? ")
                                        if (c == "q" or c == "Q"):
                                            break
                                        elif (c == "A" or c == "a"):
                                            print()
                                            p_no = int(input("Nhập thứ tự nhập bạn muốn xem :"))
                                            print()
                                            if p_no in day:
                                                print(" Thời gian | ", day.get(p_no))
                                                print(" Số thứ tự | ", p_no)
                                                print(" Sản phẩm | ", description.get(p_no))
                                                print(" Giá cả | ", unit_price.get(p_no))
                                                print(" Số lượng | ", stock.get(p_no))
                                                print("----------")
                                            else:
                                                print("Không có số thứ tự nhập này! "
                                                      "Vui lòng nhấn phím A để cập nhập thông tin ")
                                        elif (c == "B" or c == "b"):
                                            print()
                                            for p_no in unit_price:
                                                print(" Thời gian | ", day.get(p_no))
                                                print(" Số thứ tự | ", p_no)
                                                print(" Sản phẩm | ", description.get(p_no))
                                                print(" Giá cả | ", unit_price.get(p_no))
                                                print(" Số lượng | ", stock.get(p_no))
                                                print("----------")


                                elif (c == "B" or c == "b"):  # List all the parts
                                    print()
                                    print(" Danh sách nhập kho ( theo sản phẩm )")
                                    k = 0
                                    z = 1
                                    for p_no in description:
                                        if k != z:
                                            k = description.get(p_no)
                                            print()
                                            print("Sản phẩm : ", k)
                                            for p_no in description:
                                                if description.get(p_no) == k:
                                                    print(" Thời gian | ", day.get(p_no))
                                                    print(" Số thứ tự | ", p_no)
                                                    print(" Giá cả | ", unit_price.get(p_no))
                                                    print(" Số lượng | ", stock.get(p_no))
                                                    print("----------")
                                                z = description.get(p_no)
                                    print()
                                elif (c == "C" or c == "c"):
                                    print()# List all the parts
                                    print(" Danh sách nhập kho ( theo ngày ) ")
                                    k = 'x'
                                    z = 'y'
                                    for p_no in day:
                                        if k != z:
                                            k = day.get(p_no)
                                            print()
                                            print("Ngày : ", k)
                                            for p_no in day:
                                                if day.get(p_no) == k:
                                                    print(" Số thứ tự | ", p_no)
                                                    print(" Sản phẩm | ", description.get(p_no))
                                                    print(" Giá cả | ", unit_price.get(p_no))
                                                    print(" Số lượng | ", stock.get(p_no))
                                                    print("----------")
                                                z = day.get(p_no)
                                elif (c == "D" or c == "d"):
                                    print()# List all the parts
                                    print(" Danh mục sản phẩm nhập kho ( tổng ) ")
                                    k = 0
                                    z = 1
                                    for p_no in description:
                                        if k != z:
                                            k = description.get(p_no)
                                            print()
                                            print("Sản phẩm : ", k)
                                            y = 0
                                            for p_no in description:
                                                if description.get(p_no) == k:
                                                    y+=stock.get(p_no)
                                                z = description.get(p_no)
                                            print("Số lượng nhập kho :",y)
                                    print()
                                elif (c == "help"):
                                    print()# Display all commands
                                    print("Nhập kho")
                                    print()
                                    print("A - Nhập sản phẩm")
                                    print("R - Xóa sản phẩm")
                                    print("E - Chỉnh sửa sản phầm")
                                    print("L - Danh mục sản phẩm nhập kho")
                                    print("Q - Thoát ")
                                    print("help - Xem lại tất cả các lệnh")
                                    print()
                                    print("Nếu bạn có bất kỳ câu hỏi hoặc thắc mắc nào khác, vui lòng liên hệ với người quản lí.")
                                    print()

                            details = open("nhapkho.txt", "w",encoding="utf8")
                            no_items = len(unit_price)
                            details.write(str(no_items) + "\n")
                            for i in range(0, no_items):
                                details.write(str(i + 1) + "#" + str(day[i + 1]) + "\n")

                            for i in range(0, no_items):
                                details.write(str(i + 1) + "#" + str(unit_price[i + 1]) + "\n")

                            for i in range(0, no_items):
                                details.write(str(i + 1) + "#" + description[i + 1] + "\n")

                            for i in range(0, no_items):
                                details.write(str(i + 1) + "#" + str(stock[i + 1]) + "\n")

                            details.close()
                        elif (e == "B" or e == "b"):
                            unit_price = {}
                            description = {}
                            stock = {}
                            coso = {}
                            day = {}

                            details = open("xuatkho.txt", encoding="utf8")

                            no_items = int((details.readline()).rstrip("\n"))

                            for i in range(0, no_items):
                                line = (details.readline()).rstrip("\n")
                                x1, x2 = line.split("#")
                                x1 = int(x1)
                                x2 = str(x2)
                                day.update({x1: x2})

                            for i in range(0, no_items):
                                line = (details.readline()).rstrip("\n")
                                x1, x2 = line.split("#")
                                x1 = int(x1)
                                x2 = float(x2)
                                unit_price.update({x1: x2})

                            for i in range(0, no_items):
                                line = (details.readline()).rstrip("\n")
                                x1, x2 = line.split("#")
                                x1 = int(x1)
                                description.update({x1: x2})

                            for i in range(0, no_items):
                                line = (details.readline()).rstrip("\n")
                                x1, x2 = line.split("#")
                                x1 = int(x1)
                                x2 = int(x2)
                                stock.update({x1: x2})

                            for i in range(0, no_items):
                                line = (details.readline()).rstrip("\n")
                                x1, x2 = line.split("#")
                                x1 = int(x1)
                                x2 = str(x2)
                                coso.update({x1: x2})

                            details.close()

                            cart = []

                            c = "y"  # Runs the while loop as long as user wants
                            print()
                            print("Xuất kho")
                            print()
                            print("A - Nhập sản phẩm")
                            print("R - Xóa sản phẩm")
                            print("E - Chỉnh sửa sản phầm")
                            print("L - Danh sách xuất kho ( theo thứ tự )")
                            print("B - Danh sách xuất kho ( theo sản phẩm )")
                            print("C - Danh sách xuất kho ( theo ngày )")
                            print("T - Danh sách xuất kho ( theo cơ sở )")
                            print("D - Danh mục sản phẩm nhập kho ( tổng )")
                            print("Q - Thoát ")
                            print("help - Xem lại tất cả các lệnh")
                            print()

                            total_cost = 0
                            flag = 0  # To check if they have checked out

                            while (c != "q" or c != "Q"):
                                c = input(" Bạn cần gì? ")

                                if (c == "q" or c == "Q"):
                                    print()
                                    print("Bạn đã xuất kho thành công")
                                    break

                                elif (c == "A" or c == "a"):  # Add a part
                                    p_day = str(input(" Nhập thời gian xuất kho (dd.mm.yy) : "))
                                    p_no = int(input(" Nhập số thứ tự sản phẩm : "))
                                    p_pr = float(input(" Nhập giá tiền sản phẩm : "))
                                    p_desc = str(input(" Nhập tên sản phẩm : "))
                                    p_stock = int(input(" Số lượng sản phẩm : "))
                                    p_cs = str(input(" Nhập tên cơ sở nhận sản phẩm : "))

                                    m = 0
                                    for i in range(0, len(unit_price)):
                                        if (p_no in unit_price):
                                            p_no += 1
                                            m = 1
                                    if (m == 1):
                                        print()
                                        print(" Số thứ tự đó đã tồn tại :< thay đổi thành số thứ tự ", p_no)

                                    unit_price.update({p_no: p_pr})
                                    description.update({p_no: p_desc})
                                    coso.update({p_no: p_cs})
                                    day.update({p_no: p_day})

                                    if (p_stock > -1):
                                        stock.update({p_no: p_stock})
                                    else:
                                        p_stock = 0
                                        stock.update({p_no: p_stock})
                                        print(
                                            " Số lượng của một sản phẩm không được âm, số lượng sản phẩm này đã được đặt thành 0.")
                                    print()
                                    print("Thời gian xuất kho : ", day.get(p_no), " Số thứ tự sản phẩm : ", p_no,
                                          " Tên sản phẩm : ", description.get(p_no), " Giá tiền sản phẩm : ",
                                          unit_price.get(p_no), " Số lượng sản phẩm : ", stock.get(p_no),
                                          " Cơ sở nhận sản phẩm : ", coso.get(p_no))
                                    print(" Sản phẩm đã được xuất thành công !")
                                    print()

                                    details = open("xuatkho.txt", "w", encoding="utf8")
                                    no_items = len(unit_price)
                                    details.write(str(no_items) + "\n")
                                    for i in range(0, no_items):
                                        details.write(str(i + 1) + "#" + str(day[i + 1]) + "\n")

                                    for i in range(0, no_items):
                                        details.write(str(i + 1) + "#" + str(unit_price[i + 1]) + "\n")

                                    for i in range(0, no_items):
                                        details.write(str(i + 1) + "#" + description[i + 1] + "\n")

                                    for i in range(0, no_items):
                                        details.write(str(i + 1) + "#" + str(stock[i + 1]) + "\n")

                                    for i in range(0, no_items):
                                        details.write(str(i + 1) + "#" + str(coso[i + 1]) + "\n")

                                    details.close()
                                elif (c == "E" or c == "e"):  # Edit a part
                                    print()
                                    p_no = int(input(" Nhập số thứ tự sản phẩm : "))
                                    if (p_no in unit_price):
                                        p_day = str(input(" Nhập lại thời gian xuất kho (dd.mm.yy) : "))
                                        p_pr = float(input(" Nhập lại giá tiền sản phẩm: "))
                                        p_desc = input(" Nhập lại tên sản phẩm : ")
                                        p_stock = int(input(" Nhập lại số lượng sản phẩm : "))
                                        p_cs = str(input(" Nhập lại tên cơ sở nhận sản phẩm : "))
                                        unit_price.update({p_no: p_pr})
                                        description.update({p_no: p_desc})
                                        stock.update({p_no: p_stock})
                                        coso.update({p_no: p_cs})
                                        day.update({p_no: p_day})

                                        details = open("xuatkho.txt", "w", encoding="utf8")
                                        no_items = len(unit_price)
                                        details.write(str(no_items) + "\n")
                                        for i in range(0, no_items):
                                            details.write(str(i + 1) + "#" + str(day[i + 1]) + "\n")

                                        for i in range(0, no_items):
                                            details.write(str(i + 1) + "#" + str(unit_price[i + 1]) + "\n")

                                        for i in range(0, no_items):
                                            details.write(str(i + 1) + "#" + description[i + 1] + "\n")

                                        for i in range(0, no_items):
                                            details.write(str(i + 1) + "#" + str(stock[i + 1]) + "\n")

                                        for i in range(0, no_items):
                                            details.write(str(i + 1) + "#" + str(coso[i + 1]) + "\n")

                                        details.close()
                                    else:
                                        print(" Sản phẩm đó không tồn tại, để nhập một sản phẩm, hãy sử dụng phím A")
                                    print()
                                elif (c == "R" or c == "r"):  # Remove a part
                                    print()
                                    p_no = int(input(" Nhập số thứ tự sản phẩm : "))
                                    if (p_no in unit_price):
                                        are_you_sure = input(" Bạn có chắc muốn xóa sản phẩm đó không ? ( y/n )")
                                        if (are_you_sure == "y" or are_you_sure == "Y"):
                                            unit_price.pop(p_no)
                                            description.pop(p_no)
                                            stock.pop(p_no)
                                            coso.pop(p_no)
                                            day.pop(p_no)

                                            details = open("xuatkho.txt", "w", encoding="utf8")
                                            no_items = len(unit_price)
                                            details.write(str(no_items) + "\n")
                                            for i in range(0, no_items):
                                                details.write(str(i + 1) + "#" + str(day[i + 1]) + "\n")

                                            for i in range(0, no_items):
                                                details.write(str(i + 1) + "#" + str(unit_price[i + 1]) + "\n")

                                            for i in range(0, no_items):
                                                details.write(str(i + 1) + "#" + description[i + 1] + "\n")

                                            for i in range(0, no_items):
                                                details.write(str(i + 1) + "#" + str(stock[i + 1]) + "\n")

                                            for i in range(0, no_items):
                                                details.write(str(i + 1) + "#" + str(coso[i + 1]) + "\n")

                                            details.close()
                                            print(" Sản phẩm đã được xóa thành công!")
                                        print()
                                    else:
                                        print(" Xin lỗi, chúng tôi không có một sản pẩm như vậy!")
                                        print()
                                elif (c == "L" or c == "l"):  # List all the parts
                                    print(" Danh sách sản phẩm đã xuất ")
                                    print()
                                    print("A - Tìm kiếm ")
                                    print("B - Xem tất cả ")
                                    print("Q - Thoát ")
                                    print()
                                    while (x != "q" or x != "Q"):
                                        c = input(" Bạn cần gì? ")

                                        if (c == "q" or c == "Q"):
                                            break

                                        elif (c == "A" or c == "a"):
                                            p_no = int(input("Nhập thứ tự nhập bạn muốn xem :"))
                                            if p_no in day:
                                                print(" Thời gian | ", day.get(p_no))
                                                print(" Số thứ tự | ", p_no)
                                                print(" Sản phẩm | ", description.get(p_no))
                                                print(" Giá cả | ", unit_price.get(p_no))
                                                print(" Số lượng | ", stock.get(p_no))
                                                print("----------")
                                            else:
                                                print("Không có số thứ tự nhập này! "
                                                      "Vui lòng nhấn phím A để cập nhập thông tin ")

                                        elif (c == "B" or c == "b"):
                                            for p_no in unit_price:
                                                print(" Thời gian | ", day.get(p_no))
                                                print(" Số thứ tự | ", p_no)
                                                print(" Sản phẩm | ", description.get(p_no))
                                                print(" Giá cả | ", unit_price.get(p_no))
                                                print(" Số lượng | ", stock.get(p_no))
                                                print("----------")

                                elif (c == "B" or c == "b"):  # List all the parts
                                    print(" Danh sách xuất kho ( theo sản phẩm )")
                                    k = 0
                                    z = 1
                                    for p_no in description:
                                        if k != z:
                                            k = description.get(p_no)
                                            print("Sản phẩm : ", k)
                                            for p_no in description:
                                                if description.get(p_no) == k:
                                                    print(" Thời gian | ", day.get(p_no))
                                                    print(" Số thứ tự | ", p_no)
                                                    print(" Giá cả | ", unit_price.get(p_no))
                                                    print(" Số lượng | ", stock.get(p_no))
                                                    print(" Cơ sở | ", coso.get(p_no))
                                                    print("----------")
                                                z = description.get(p_no)
                                    print()
                                elif (c == "C" or c == "c"):  # List all the parts
                                    print(" Danh sách xuất kho ( theo ngày ) ")
                                    k = 'x'
                                    z = 'y'
                                    for p_no in day:
                                        if k != z:
                                            k = day.get(p_no)
                                            print("Ngày : ", k)
                                            for p_no in day:
                                                if day.get(p_no) == k:
                                                    print(" Số thứ tự | ", p_no)
                                                    print(" Sản phẩm | ", description.get(p_no))
                                                    print(" Giá cả | ", unit_price.get(p_no))
                                                    print(" Số lượng | ", stock.get(p_no))
                                                    print(" Cơ sở | ", coso.get(p_no))
                                                    print("----------")
                                                z = day.get(p_no)
                                elif (c == "D" or c == "d"):  # List all the parts
                                    print(" Danh mục sản phẩm xuất kho ( tổng ) ")
                                    k = 0
                                    z = 1
                                    for p_no in description:
                                        if k != z:
                                            k = description.get(p_no)
                                            print("Sản phẩm : ", k)
                                            y = 0
                                            for p_no in description:
                                                if description.get(p_no) == k:
                                                    y+=stock.get(p_no)
                                                z = description.get(p_no)
                                            print("Số lượng xuất kho :",y)
                                    print()
                                elif (c == "T" or c == "t"):
                                    print()# List all the parts
                                    print(" Danh sách xuất kho ( theo cơ sở )")
                                    k = 0
                                    z = 1
                                    for p_no in coso:
                                        if k != z:
                                            k = coso.get(p_no)
                                            print()
                                            print("Cơ sở : ", k)
                                            for p_no in coso:
                                                if coso.get(p_no) == k:
                                                    print(" Thời gian | ", day.get(p_no))
                                                    print(" Số thứ tự | ", p_no)
                                                    print(" Sản phẩm | ", description.get(p_no))
                                                    print(" Giá cả | ", unit_price.get(p_no))
                                                    print(" Số lượng | ", stock.get(p_no))
                                                    print("----------")
                                                z = coso.get(p_no)
                                    print()
                                elif (c == "help"):  # Display all commands
                                    print("Xuất kho")
                                    print()
                                    print("A - Nhập sản phẩm")
                                    print("R - Xóa sản phẩm")
                                    print("E - Chỉnh sửa sản phầm")
                                    print("L - Danh mục sản phẩm nhập kho")
                                    print("Q - Thoát ")
                                    print("help - Xem lại tất cả các lệnh")
                                    print()
                                    print(
                                        "Nếu bạn có bất kỳ câu hỏi hoặc thắc mắc nào khác, vui lòng liên hệ với người quản lí.")
                                    print()

                            details = open("xuatkho.txt", "w", encoding="utf8")
                            no_items = len(unit_price)
                            details.write(str(no_items) + "\n")
                            for i in range(0, no_items):
                                details.write(str(i + 1) + "#" + str(day[i + 1]) + "\n")

                            for i in range(0, no_items):
                                details.write(str(i + 1) + "#" + str(unit_price[i + 1]) + "\n")

                            for i in range(0, no_items):
                                details.write(str(i + 1) + "#" + description[i + 1] + "\n")

                            for i in range(0, no_items):
                                details.write(str(i + 1) + "#" + str(stock[i + 1]) + "\n")

                            for i in range(0, no_items):
                                details.write(str(i + 1) + "#" + str(coso[i + 1]) + "\n")

                            details.close()
                        elif (e == "C" or e == "c"):

                            unit_price1 = {}
                            description1 = {}
                            stock1 = {}
                            day1 = {}

                            details = open("nhapkho.txt", encoding="utf8")

                            no_items = int((details.readline()).rstrip("\n"))

                            for i in range(0, no_items):
                                line = (details.readline()).rstrip("\n")
                                x1, x2 = line.split("#")
                                x1 = int(x1)
                                day1.update({x1: x2})

                            for i in range(0, no_items):
                                line = (details.readline()).rstrip("\n")
                                x1, x2 = line.split("#")
                                x1 = int(x1)
                                unit_price1.update({x1: x2})

                            for i in range(0, no_items):
                                line = (details.readline()).rstrip("\n")
                                x1, x2 = line.split("#")
                                x1 = int(x1)
                                description1.update({x1: x2})

                            for i in range(0, no_items):
                                line = (details.readline()).rstrip("\n")
                                x1, x2 = line.split("#")
                                x1 = int(x1)
                                stock1.update({x1: x2})

                            details.close()

                            unit_price = {}
                            description = {}
                            stock = {}
                            day = {}
                            coso = {}
                            details = open("xuatkho.txt", encoding="utf8")

                            no_items = int((details.readline()).rstrip("\n"))

                            for i in range(0, no_items):
                                line = (details.readline()).rstrip("\n")
                                x1, x2 = line.split("#")
                                x1 = int(x1)
                                x2 = str(x2)
                                day.update({x1: x2})

                            for i in range(0, no_items):
                                line = (details.readline()).rstrip("\n")
                                x1, x2 = line.split("#")
                                x1 = int(x1)
                                x2 = float(x2)
                                unit_price.update({x1: x2})

                            for i in range(0, no_items):
                                line = (details.readline()).rstrip("\n")
                                x1, x2 = line.split("#")
                                x1 = int(x1)
                                description.update({x1: x2})

                            for i in range(0, no_items):
                                line = (details.readline()).rstrip("\n")
                                x1, x2 = line.split("#")
                                x1 = int(x1)
                                x2 = int(x2)
                                stock.update({x1: x2})

                            for i in range(0, no_items):
                                line = (details.readline()).rstrip("\n")
                                x1, x2 = line.split("#")
                                x1 = int(x1)
                                x2 = str(x2)
                                coso.update({x1: x2})

                            details.close()
                            print()
                            print("Danh sách sản phẩm tồn kho")
                            for p_no in unit_price:
                                print()
                                print(" Số thứ tự | ", p_no)
                                print(" Sản phẩm | ", description.get(p_no))
                                if (int(stock1.get(p_no)) - int(stock.get(p_no)) > 0):
                                    print(" Số lượng | ", str(int(stock1.get(p_no)) - int(stock.get(p_no))))
                                else:
                                    print(" Đã xuất kho quá số lượng đã nhập kho !!! ")
                                print("----------")

                            details = open("tonkho.txt", "w",encoding="utf8")
                            no_items = len(unit_price)
                            details.write(str(no_items) + "\n")
                            for i in range(0, no_items):
                                details.write(str(i + 1) + "#" + str(unit_price[i + 1]) + "\n")

                            for i in range(0, no_items):
                                details.write(str(i + 1) + "#" + description[i + 1] + "\n")

                            for i in range(0, no_items):
                                details.write(str(i + 1) + "#" + str(int(stock1[i + 1]) - int(stock[i + 1])) + "\n")

                            details.close()
                elif (d == "C" or d == "c"):

                    doanhthu = {}
                    coso = {}
                    day = {}

                    details = open("doanhthu.txt", encoding="utf8")

                    no_items = int((details.readline()).rstrip("\n"))

                    for i in range(0, no_items):
                        line = (details.readline()).rstrip("\n")
                        x1, x2 = line.split("#")
                        x1 = int(x1)
                        x2 = str(x2)
                        day.update({x1: x2})

                    for i in range(0, no_items):
                        line = (details.readline()).rstrip("\n")
                        x1, x2 = line.split("#")
                        x1 = int(x1)
                        x2 = str(x2)
                        coso.update({x1: x2})

                    for i in range(0, no_items):
                        line = (details.readline()).rstrip("\n")
                        x1, x2 = line.split("#")
                        x1 = int(x1)
                        x2 = float(x2)
                        doanhthu.update({x1: x2})

                    details.close()

                    cart = []
                    c = "y"

                    print("Quản lý doanh thu")
                    print()
                    print("A - Nhập doanh thu")
                    print("R - Xóa doanh thu")
                    print("E - Chỉnh sửa doanh thu")
                    print("L - Danh mục doanh thu")
                    print("Q - Thoát ")
                    print("help - Xem lại tất cả các lệnh")
                    print()

                    total_cost = 0
                    flag = 0  # To check if they have checked out

                    while (c != "q" or c != "Q"):
                        c = input(" Bạn cần gì? ")

                        if (c == "q" or c == "Q"):
                            print()
                            print("Bạn đã quản lý doanh thu thành công")
                            break

                        elif (c == "A" or c == "a"):  # Add a part
                            p_stt = int(input(" Nhập số thứ tự doanh thu : "))
                            p_day = str(input(" Nhập thời gian (dd.mm.yy) : "))
                            p_cs = str(input(" Nhập tên cơ sở : "))
                            p_dt = float(input(" Nhập doanh thu cơ sở : "))

                            m = 0
                            for i in range(0, len(doanhthu)):
                                if (p_stt in doanhthu):
                                    p_stt += 1
                                    m = 1
                            if (m == 1):
                                print()
                                print(" Số thứ tự đó đã tồn tại :< thay đổi thành số thứ tự ", p_stt)

                            coso.update({p_stt: p_cs})
                            day.update({p_stt: p_day})

                            if (p_dt > -1):
                                doanhthu.update({p_stt: p_dt})
                            else:
                                p_dt = 0
                                doanhthu.update({p_stt: p_dt})
                                print(
                                    " Doanh thu của một cơ sở không được âm, doanh thu của cơ sở này đã được sửa thành 0.")
                            print()
                            print(" Số thứ tự : ", p_stt, "Thời gian : ", day.get(p_stt), " Cơ sở : ", coso.get(p_stt)
                                  , " Doanh thu : ", doanhthu.get(p_dt))
                            print(" Cơ sở đã được nhập thành công !")
                            print()

                            details = open("doanhthu.txt", "w", encoding="utf8")
                            no_items = len(doanhthu)
                            details.write(str(no_items) + "\n")

                            for i in range(0, no_items):
                                details.write(str(i + 1) + "#" + str(day[i + 1]) + "\n")

                            for i in range(0, no_items):
                                details.write(str(i + 1) + "#" + coso[i + 1] + "\n")

                            for i in range(0, no_items):
                                details.write(str(i + 1) + "#" + str(doanhthu[i + 1]) + "\n")
                            details.close()

                        elif (c == "E" or c == "e"):  # Edit a part
                            print()
                            p_stt = int(input(" Nhập số thứ tự : "))
                            if (p_stt in doanhthu):
                                p_day = str(input(" Nhập lại thời gian (dd.mm.yy) : "))
                                p_cs = str(input(" Nhập lại tên cơ sở : "))
                                p_dt = float(input(" Nhập lại doanh thu cơ sở : "))

                                coso.update({p_stt: p_cs})
                                day.update({p_stt: p_day})

                                details = open("doanhthu.txt", "w", encoding="utf8")
                                no_items = len(doanhthu)
                                details.write(str(no_items) + "\n")

                                for i in range(0, no_items):
                                    details.write(str(i + 1) + "#" + str(day[i + 1]) + "\n")

                                for i in range(0, no_items):
                                    details.write(str(i + 1) + "#" + coso[i + 1] + "\n")

                                for i in range(0, no_items):
                                    details.write(str(i + 1) + "#" + str(doanhthu[i + 1]) + "\n")
                                details.close()

                                if (p_dt > -1):
                                    doanhthu.update({p_stt: p_dt})
                                else:
                                    p_dt = 0
                                    doanhthu.update({p_stt: p_dt})
                                    print(
                                        " Doanh thu của một cơ sở không được âm, doanh thu của cơ sở này đã được đsở thành 0.")
                            else:
                                print(" Số thứ tự đó không tồn tại, để nhập một doanh thu cơ sở, hãy sử dụng phím A")
                            print()

                        elif (c == "R" or c == "r"):  # Remove a part
                            print()
                            p_stt = int(input(" Nhập số thứ tự : "))
                            if (p_stt in doanhthu):
                                are_you_sure = input(" Bạn có chắc muốn xóa doanh thu của cơ sở đó không ? ( y/n )")
                                if (are_you_sure == "y" or are_you_sure == "Y"):
                                    doanhthu.pop(p_stt)
                                    coso.pop(p_stt)
                                    day.pop(p_stt)

                                    details = open("doanhthu.txt", "w", encoding="utf8")
                                    no_items = len(doanhthu)
                                    details.write(str(no_items) + "\n")

                                    for i in range(0, no_items):
                                        details.write(str(i + 1) + "#" + str(day[i + 1]) + "\n")

                                    for i in range(0, no_items):
                                        details.write(str(i + 1) + "#" + coso[i + 1] + "\n")

                                    for i in range(0, no_items):
                                        details.write(str(i + 1) + "#" + str(doanhthu[i + 1]) + "\n")
                                    details.close()

                                    print(" Doanh thu cơ sở đã được xóa thành công!")
                                print()
                            else:
                                print(" Xin lỗi, chúng tôi không có một thông tin như vậy!")
                                print()

                        elif (c == "L" or c == "l"):  # List all the parts
                            print(" Danh sách doanh thu cơ sở ")
                            for p_stt in doanhthu:
                                print(" Số thứ tự | ", p_stt)
                                print(" Thời gian | ", day.get(p_stt))
                                print(" Cơ sở | ", coso.get(p_stt))
                                print(" Doanh thu | ", doanhthu.get(p_stt))
                                print("----------")

                        elif (c == "help"):  # Display all commands
                            print("Quản lý doanh thu")
                            print()
                            print("A - Nhập doanh thu")
                            print("R - Xóa doanh thu")
                            print("E - Chỉnh sửa doanh thu")
                            print("L - Danh mục doanh thu")
                            print("Q - Thoát ")
                            print("help - Xem lại tất cả các lệnh")
                            print()

                    details = open("doanhthu.txt", "w", encoding="utf8")
                    no_items = len(doanhthu)
                    details.write(str(no_items) + "\n")
                    for i in range(0, no_items):
                        details.write(str(i + 1) + "#" + str(day[i + 1]) + "\n")

                    for i in range(0, no_items):
                        details.write(str(i + 1) + "#" + coso[i + 1] + "\n")

                    for i in range(0, no_items):
                        details.write(str(i + 1) + "#" + str(doanhthu[i + 1]) + "\n")
                    details.close()
                elif (d == "D" or d == "d"):
                    unit_price = {}
                    description = {}
                    stock = {}
                    day = {}

                    details = open("nhapkho.txt", "r", encoding="utf8")  # First line of the file is the number of items
                    no_items = int((details.readline()).rstrip("\n"))

                    for i in range(0, no_items):
                        line = (details.readline()).rstrip("\n")
                        x1, x2 = line.split("#")
                        x1 = int(x1)
                        x2 = str(x2)
                        day.update({x1: x2})

                    for i in range(0, no_items):
                        line = (details.readline()).rstrip("\n")
                        x1, x2 = line.split("#")
                        x1 = int(x1)
                        x2 = float(x2)
                        unit_price.update({x1: x2})

                    for i in range(0, no_items):
                        line = (details.readline()).rstrip("\n")
                        x1, x2 = line.split("#")
                        x1 = int(x1)
                        description.update({x1: x2})

                    for i in range(0, no_items):
                        line = (details.readline()).rstrip("\n")
                        x1, x2 = line.split("#")
                        x1 = int(x1)
                        x2 = float(x2)
                        stock.update({x1: x2})
                    details.close()
                    print()
                    print("Quản lý chi tiêu")
                    ngay = {}
                    chi = {}
                    for i in range(0, no_items):
                        x1 = 0
                        k = str(day.get(i + 1))
                        for i in range(0, no_items):
                            if day.get(i + 1) == k:
                                x1 += ((stock.get(i + 1))*unit_price.get(i+1))
                                ngay.update({(i + 1): k})
                                chi.update({(i + 1): x1})
                    for i in ngay:
                        print()
                        print(" Thời gian | ", ngay.get(i))
                        print(" Tổng chi tiêu trong ngày | ", chi.get(i))
                        print("----------")

                    details = open("ct.txt", "w", encoding="utf8")
                    no_items = len(ngay)

                    details.write(str(no_items) + "\n")
                    for i in range(0, no_items):
                        details.write(str(i + 1) + "#" + str(ngay[i + 1]) + "\n")

                    for i in range(0, no_items):
                        details.write(str(i + 1) + "#" + str(chi[i + 1]) + "\n")

                    details.close()
                elif (d == "K" or d == "k"):

                    doanhthu = {}
                    coso = {}
                    day = {}

                    details = open("doanhthu.txt", encoding="utf8")
                    no_items = int((details.readline()).rstrip("\n"))

                    for i in range(0, no_items):
                        line = (details.readline()).rstrip("\n")
                        x1, x2 = line.split("#")
                        x1 = int(x1)
                        x2 = str(x2)
                        day.update({x1: x2})

                    for i in range(0, no_items):
                        line = (details.readline()).rstrip("\n")
                        x1, x2 = line.split("#")
                        x1 = int(x1)
                        x2 = str(x2)
                        coso.update({x1: x2})

                    for i in range(0, no_items):
                        line = (details.readline()).rstrip("\n")
                        x1, x2 = line.split("#")
                        x1 = int(x1)
                        x2 = float(x2)
                        doanhthu.update({x1: x2})

                    details.close()
                    ngay={}
                    thu={}
                    print()
                    print("Quản lý doanh thu từng ngày ( tổng )")
                    for i in range(0, no_items):
                        x1=0
                        k = str(day.get(i+1))
                        for i in range(0, no_items):
                            if day.get(i+1) == k :
                                x1 +=(float(doanhthu.get(i+1)))
                                ngay.update({(i+1):k})
                                thu.update({(i+1):x1})
                    for i in ngay:
                        print()
                        print(" Thời gian | ", ngay.get(i))
                        print(" Tổng doanh thu trong ngày | ", thu.get(i))
                        print("----------")

                    details = open("dtn.txt", "w", encoding="utf8")
                    no_items = len(ngay)

                    details.write(str(no_items) + "\n")
                    for i in range(0, no_items):
                        details.write(str(i + 1) + "#" + str(ngay[i + 1]) + "\n")

                    for i in range(0, no_items):
                        details.write(str(i + 1) + "#" + str(thu[i + 1]) + "\n")

                    details.close()
                elif (d == "E" or d == "e"):
                    chitieu={}
                    doanhthu={}
                    ngayc={}
                    ngayt={}

                    details = open("ct.txt", "r", encoding="utf8")  # First line of the file is the number of items
                    no_items = int((details.readline()).rstrip("\n"))

                    for i in range(0, no_items):
                        line = (details.readline()).rstrip("\n")
                        x1, x2 = line.split("#")
                        x1 = int(x1)
                        x2 = str(x2)
                        ngayc.update({x1: x2})

                    for i in range(0, no_items):
                        line = (details.readline()).rstrip("\n")
                        x1, x2 = line.split("#")
                        x1 = int(x1)
                        x2 = float(x2)
                        chitieu.update({x1: x2})
                    details.close()

                    details = open("dtn.txt", "r", encoding="utf8")  # First line of the file is the number of items
                    no_items = int((details.readline()).rstrip("\n"))

                    for i in range(0, no_items):
                        line = (details.readline()).rstrip("\n")
                        x1, x2 = line.split("#")
                        x1 = int(x1)
                        x2 = str(x2)
                        ngayt.update({x1: x2})

                    for i in range(0, no_items):
                        line = (details.readline()).rstrip("\n")
                        x1, x2 = line.split("#")
                        x1 = int(x1)
                        x2 = float(x2)
                        doanhthu.update({x1: x2})
                    details.close()
                    print()
                    print("Quản lý lợi nhuận ")
                    loinhuanngay = {}
                    for i in range(0, no_items):
                        y = 0
                        k = str(ngayt.get(i+1))
                        for i in range(0, no_items):
                            if ngayt.get(i + 1) == k:
                                y = ((doanhthu.get(i + 1))-(chitieu.get(i+1)))
                                loinhuanngay.update({k: y})
                    for k in loinhuanngay:
                        print()
                        print(" Thời gian | ", k)
                        print(" Tổng lợi nhuận trong ngày | ", loinhuanngay.get(k))
                        print("----------")
                    x = 0
                    for k in loinhuanngay:
                        x += 1
                    details = open("lnn.txt", "w", encoding="utf8")
                    details.write(str(x) + "\n")
                    for k in loinhuanngay:
                        details.write(k + " # " + str(loinhuanngay.get(k)) + "\n")
                    details.close()


