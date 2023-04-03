class Student:
    """
    学员实体类，学员名单管理类，学员名单管理系统
    """
    number : int
    name : str
    sex : str
    def __init__(self, number, name, sex):
        self.number = number
        self.name = name
        self.sex = sex
    def __str__(self):
        return f"{self.number},{self.name},{self.sex}"



class StudentList:

    def __init__(self,student_list):
        self.s_list = student_list

    def get(self,student_id):
        """
        根据student_id查询信息
        """
        for i in self.s_list:
            if i.number == student_id:
                return i



    def delete(self, student_id):
        """
        根据 student_id 删除信息
        """
        for i in self.s_list:
            if i.number == student_id:
                self.s_list.remove (i)
                return self.s_list


if __name__ == '__main__':
    #入参自己定义
    s1 = Student(1, "李华", "男")
    s2 = Student(2, "王淼", "男")
    s3 = Student(3, "张盼盼", "女")
    #初始化一个成员名单
    s_list = StudentList([s1,s2,s3])
    #实现get()方法
    A = s_list.get(2)
    print(A)
    #实现delete
    DA = s_list.delete(1)
    for i in DA:
        print(i)

