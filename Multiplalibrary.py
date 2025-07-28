class multifunctions():
    def Subfields():
        fields=["Machine Learning","Neural Networks","Vision,Robotics","Speech Processing","Natural Language Processing"]
        print("Sub-fields in AI are:")
        for field in fields:
            print(field)

    def OddEven():
        Number=int(input("Enter a Number: "))
        if Number % 2 == 0:
            print(Number,"is even number")
        else:
            print(Number,"is odd number")
        return
        
    def Eligible():
        Gender=input("Enter the Gender: ")
        Age=int(input("Enter the age: "))
        if Gender == "Male":
            if Age>=21:
                print("Male Eligible for Marriage")
            elif Gender == "Female":
            if Age>=18:
                print("Female Eligible for Marriage")
        return

    def percentage():
        Marks=[]
        TotalSubjects=int(input("Enter number of subjects:"))
        Totalmark=500
        for calculate in range(TotalSubjects):
            Mark = int(input("Enter mark for subject: "))
            Marks.append(Mark)
            total=sum(Marks)             
        percentage = (total / Totalmark) * 100
        print(Marks)
        print(total)
        print(percentage)
        
    def triangle():
            Height=int(input("Enter height:"))
            Breadth=int(input("Enter breadth:"))
            Height1=int(input("Enter height1:"))
            Height2=int(input("Enter height2:"))
            breadth2=int(input("Enter Breadth:"))
            Area=(Height * Breadth) / 2
            print("Area of Triangle",Area)
            perimeter = Height1 + Height2 + breadth2
            print("Perimeter is",perimeter)
