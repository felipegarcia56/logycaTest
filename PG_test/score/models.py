from django.db import models
from professor.models import Professor
from student.models import Student


class Score(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, db_column="professor_id", blank=True, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, db_column="student_id", blank=True, null=True)
    value = models.FloatField(default=0.0)

    def __str__(self):
        return str(self.name)

    class Meta:
        managed = True