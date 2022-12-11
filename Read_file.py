import os
import face_recognition

# images 폴더 안의 사진으로 list 생성 (출석체크 대기자)
student_images = os.listdir('images')
print(student_images) # test code (image)
print()

# {student_name : 출석여부} 의 dictionary 생성 (출석부)
student_dic = {}
for student in student_images:
    
        if student.count(".") == 1: 
            name = student.split('.')[0]
            student_dic[name] = '결석'

# student_dic 출력
def name_print():
    for name, val in student_dic.items():
        print(name, val)

    print('\n-------------------------\n')
    main()