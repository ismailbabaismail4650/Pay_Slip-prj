from django.db import models

# Create your models here.

class Staff (models.Model):
    first_name = models.CharField(max_length=100) 
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    basic_salary = models.IntegerField()    
    
    def __str__(self):
        return f"Pay Slip for {self.first_name} - {self.last_name}"


class Pay_slip (models.Model):
    position= models.ForeignKey(Staff,on_delete=models.CASCADE) 
    days_absent = models.IntegerField(default=0)
    loan_iou = models.IntegerField(default=0)
    deductions = models.IntegerField(default=500)
    bonus = models.IntegerField(default=0)
    monthly_earning = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.monthly_earning = self.position.basic_salary - (self.days_absent * self.deductions) - self.loan_iou + self.bonus
        return super().save(*args, **kwargs)

    
    def __str__(self):
        return self.position.first_name


