from django.db import models

# Create your models here.
class TableAclass(models.Model):
    EmpNo=models.IntegerField()
    Ename=models.CharField(max_length=20)
    Dept=models.CharField(max_length=20)
    Salary=models.IntegerField()
    def __str__(self):
        template='{0.EmpNo}, {0.Ename}, {0.Dept}, {0.Salary}'
        return template.format(self)
        #return str(self.EmpNo),self.Ename,self.Dept,str(self.Salary)
    


