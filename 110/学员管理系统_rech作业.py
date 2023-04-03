class Student:
    """学员实体类，学员名单管理类，学员名单管理系统"""
    pass

class StudentList:
    def __int__(self,student_list):
        self.s_list = student_list

    def get(self,student_id):
        """根据student_id查询信息"""
        pass

if __name__ == '__main__':
    #入参自己定义
    s1 = Student()
    s2 = Student()
    s3 = Student()
    #初始化一个成员名单
    s_list = StudentList([s1,s2,s3])
    #实现get()方法
    s_list.get()
    #实现delete
    s_list.delete()

class Human():