#### OSS-term-project  
###### team 23
---
# ✅Student Attendance System  

### 1. Project Overview
#### 1) Project Name
#### Student attendance system
---

#### 2) Project Objectives

##### Instead of checking attendance using the existing character input method and name method,
##### We wanted to make a attendance system using the face recognition method.
##### Because the existing method had problems such as proxy attendance and fraudulent attendance
##### We thought we should create a system in which attendance is recognized only when people recognize their faces.
##### Also, We wanted to use methods such as image recognition and face recognition that we learned through the existing open source class.
---
#### 3) Project Features

##### This project features facial recognition through images.
##### Compared to the newly entered face image through the input image, the person concerned
##### You can check your attendance. It also includes an attendance check system.
##### After checking the list and checking attendance, it has the characteristic of informing the attendance status on the screen.
##### The advantage is that not only those who attend but also those who are absent can be painted.

### 2. version & install  
1. Python (3.10.1)  
2. CMake (3.25.0)  
2. dlib (19.24.0)  
3. face_recognition  

### 3. File Setting  
![folder1](https://user-images.githubusercontent.com/97026673/206913915-e6461f04-3ce3-4bde-8386-901f5f095515.jpg)  
![folder2](https://user-images.githubusercontent.com/97026673/206914066-e8b3cf84-51c0-4e6f-8080-ca46b60bba20.jpg)  

### 4. Point of the Code  

```python
import os  
import face_recognition  
```
> import the module to using for the program  

```python
# 프로그램의 하위 폴더 images  
student_images = os.listdir('images')  
```
> reading image files in images folder & creating list of file-names  

```python
# create an empty dictionary   
student_dic = {}  
for student in student_images:  
    
        if student.count(".") == 1:   
            name = student.split('.')[0]  
            student_dic[name] = '결석'  
```
> Setting the initial state of the dictionary    

```python
# 프로그램과 동일 폴더 image (or 경로까지 작성)  
student_name = input('파일을 업로드 하세요(ex: name.jpg) : ')    
image_to_recognition = face_recognition.load_image_file(student_name)  
image_to_recognition_encoded = face_recognition.face_encodings(image_to_recognition)[0]  
```
> Read the image file name of the student to attendance check & face recognition    
```python
def main():  
    print('출석체크 시스템입니다\n')  
    print('1. 명단 확인\n2. 출석체크\n3. 종료\n')  
    func = int(input('실행할 기능의 번호를 입력하세요 : '))  
    print()  

    if func == 1:  
        name_print()  
    elif func == 2:  
        attendance()  
    elif func == 3:  
        print('종료합니다\n')  
    else:  
        print('Error..\n')  
        main()  
        
main()  
```
> Run the program repeatedly using the main function  

### 5. Result  
> Run the program  
![1](https://user-images.githubusercontent.com/97026673/206917722-71bb45d2-edca-4661-b8b3-c6c7af8a3066.jpg)  
  
#### case " 1 " : print the student list with attendance status  
<img src="https://user-images.githubusercontent.com/97026673/206917723-7c10e46e-2649-4878-ac7d-b5a1a2e29da1.jpg" width="30%" height="30%" />  

#### case " 2 " : User enters the name (name.jpg)  
<img src="https://user-images.githubusercontent.com/97026673/206917712-ccb07f03-e94f-42bf-8dfa-0a448d8de5a0.jpg" width="30%" height="30%" />  

#### read the name and modify the value of the dictionary  
<img src="https://user-images.githubusercontent.com/97026673/206917716-bea9795d-6682-47a4-b3ad-f97605459200.jpg" width="30%" height="30%" />   

#### Enter 1, user can see the result of the modification  
<img src="https://user-images.githubusercontent.com/97026673/206917718-1c4c43a1-3854-47b9-bb07-1f53e93f5d01.jpg" width="30%" height="30%" />   

#### case " 3 " : exit the program  
<img src="https://user-images.githubusercontent.com/97026673/206917719-427144e9-eddc-4dc9-8030-53eb0958a56b.jpg" width="30%" height="30%" />   


### 6. 참고 자료  
1. dlib installation on Windows ( https://sulastri.tistory.com/3 )  
2. face comparison in image and webcam ( https://bskyvision.com/entry/ubuntupython-%ED%8A%B9%EC%A0%95-%EC%9D%B8%EB%AC%BC-%EC%96%BC%EA%B5%B4%EB%A7%8C-%EA%B2%80%EC%B6%9C%ED%95%98%EA%B8%B0 )  
3. file read & storing the file name ( https://seong6496.tistory.com/100 )  
