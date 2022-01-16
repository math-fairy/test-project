

from Final_class import Student


#==================연락처 관리 프로그램===================

def phoneNum():
    a=0
    while a != 9:
        print("===연락처 관리===")
        print("1. 연락처 보기 ")
        print("2. 연락처 추가 ")
        print("3. 연락처 삭제 ")
        print("4. 연락처 검색 ")
        print("9. 종료 ")
        a=int(input("수행할 작업을 선택해주세요 : "))

        #연락처 보기
        if a==1:
            file=open("friendsList.txt",'r')
            r = file.read()
            print("=== 저장된 연락처 목록 ===")
            print(r)
            file.close()
        
        #연락처 추가
        elif a==2:
            T = Student()
            
            name=input("이름 : ")
            T.setName(name)
            t=T.getName()
            
            while True:
                try:
                    age=int(input("나이 : "))
                    T.setAge(age)
                    s=T.getAge()
                    break
                except ValueError:
                    print("나이를 정수값으로 정확히 입력해주세요")
            while True:
                try:
                    stunum=int(input("학번 : "))
                    T.setStunum(stunum)
                    u=T.getStunum()
                    break
                except ValueError:
                    print("학번을 정수값으로 정확히 입력해주세요")

            hobby=input("취미 : ")
            T.setHobby(hobby)
            v=T.getHobby()

            new = "%s, %d, %d, %s\n" %(t,s,u,v)
            file=open("friendsList.txt",'a')
            file.write(new)

            while True:
                try:
                    T.__eq__()
                    break
                except:
                    pass

            file.close()
            
        #연락처 삭제  
        elif a==3:
            
            delete = input("삭제할 이름을 입력해주세요 : ")
            
            file1=open("friendsList.txt",'r')
            lines = file1.readlines()
            file2=open("friendsList.txt",'w')
            for line in lines:
                if delete not in line:
                    file2.write(line)
                
            
            
            file1.close()
            file2.close()
        
        #연락처 검색
        elif a==4:
            file=open('friendsList.txt','r')
            lines = file.readlines()
            who = input("검색할 사람의 이름을 입력해주세요 : ")
            
            
            for line in lines:
                if who not in line:
                    pass
                    
                elif who in line:
                    print("검색한 사람의 정보가 존재합니다")
                    print(line)
                    break
            
            file.close()

        elif a==9:
            break
        else:
            print("1,2,3,4,9 중에서 숫자를 선택해주세요")    



phoneNum()

            

    