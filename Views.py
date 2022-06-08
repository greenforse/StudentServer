def single_student_print(student):
    print(f"id: {student[0]} ФИО: {student[1]} , {student[2]}, {student[3]}, группа: {student[4]}")

def single_predmet_print(predmet):
    if predmet[2] == False :
        zachet = "оценка"
    else: zachet = "зачет"
    print(f"id:{predmet[0]}, название:{predmet[1]} , {zachet}")

def print_spec(spec,number):
    print(f"{number}, id/name: {spec[0]}, направление: {spec[1]})")

