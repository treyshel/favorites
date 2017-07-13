#file used for opening, appending, and writing files ONLY


def open_student_checklist():
    '''None -> [[str, str]]'''
    students = []
    with open('total_student_checklist.txt', 'r') as file:
        file.readline()
        for names in file:
            split_string = names.split(', ')
            students.append([split_string[0], split_string[1]])
        return students

def is_male():
    ''' [[str, str]] -> bool'''
    male = []
    with open('male_checkin_list.txt', 'r') as file:
        file.readline()
        for lines in file:
            split_string = names.split(', ')
            male.append([split_string[0]])
        return ('Mr.', male.capitalize())

def is_female():
    ''' [[str, str]] -> bool'''
    female = []
    with open('female_checkin_list.txt', 'r') as file:
        file.readline()
        for lines in file:
            split_string = names.split(', ')
            female.append([split_string[0]])
        return ('Ms.', female.capitalize())

def is_valid_student(students, names):
    ''' [[str, str]] -> bool '''
    with open('total_student_checklist.txt', 'r') as file:
        file.readline()
        for item in students:
            if name == item[0]:
                return True
            else:
                return False
        return False

def log_checkin():
    ''' [[str, str]] -> bool '''
    log = []
    with open('checkin_log.txt', 'a') as history:
        history.readline()
        readlines = history.readlines()
    for lines in readlines:
        split_string = lines.strip().split(', ')
        log.append([split_string[0], split_string[1]])
    return log


