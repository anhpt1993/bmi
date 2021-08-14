# Body Mass Index

def check_bmi(index):
    print("Chỉ số BMI của bạn là {:.2f}".format(index))
    print()
    if index < 16:
        print("Bạn đang gầy cấp độ III.".format(index))
    elif index >= 16 and index < 17:
        print("Bạn đang gầy cấp độ II.")
    elif index >= 17 and index < 18.5:
        print("Bạn đang gầy cấp độ I.")
    elif index >= 18.5 and index < 25:
        print("Bạn vẫn đang bình thường, không có gì phải lo lắng.")
    elif index >= 25 and index < 30:
        print("Bạn đang thừa cân nhẹ.")
    elif index >= 30 and index < 35:
        print("Bạn đang béo phì cấp độ I.")
    elif index >= 35 and index < 40:
        print("Bạn đang béo phì cấp độ II.")
    else:
        print("Bạn đang béo phì cấp độ III.")

while True:
    try:
        weight = float(input("Nhập cân nặng nhé bạn (kg): "))
        if weight > 0:
            while True:
                try:
                    height = float(input("Nhập chiều cao của bạn (m): "))
                    if height > 0 and height <= 3:
                        break
                    elif height <= 0:
                        print("Bạn chắc không tồn tại trên cõi đời này rồi.")
                        print()
                    else:
                        print("Người Trái Đất chúng tôi không cao đến vậy. Quay về hành tinh của bạn đi.")
                        print()
                except Exception:
                    print("Nhập vào một số, không phải dạng chuỗi nhé!!!")
                    print()
            break
        else:
            print("Đến không khí còn có khối lượng. Bạn chắc không phải vật chất rồi.")
            print()
    except Exception:
        print("Nhập vào một số, không phải dạng chuỗi nhé!!!")
        print()

print("Cân nặng của bạn là {} kg, và chiều cao của bạn là {} m".format(weight,height))
bmi = weight / (height**2)
check_bmi(bmi)