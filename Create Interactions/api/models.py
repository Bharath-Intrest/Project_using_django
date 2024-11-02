from django.db import models

#binary_default_img=0

def get_default_image():
    with open(r"C:\Users\bhara\Downloads\default_img.jpeg", 'rb') as file:
        return file.read()
# Create your models here.
class log_in(models.Model):
    user_name=models.CharField(max_length=50)
    password1=models.CharField(max_length=50)
    
class home(models.Model):
    global binary_default_img
    pri_id=models.ForeignKey(log_in, on_delete=models.CASCADE,related_name='homes')
    name=models.CharField(max_length=100)
    dept=models.CharField(max_length=100)
    rollno=models.CharField(max_length=50)
    phno=models.CharField(max_length=20)
    user_img = models.BinaryField(blank=True, null=True)  

    def save(self, *args, **kwargs):
        if not self.user_img:
            self.user_img = get_default_image()
        super().save(*args, **kwargs)


class all_up_doc(models.Model):
    uploaded_by=models.IntegerField()
    title=models.CharField(max_length=100)
    img=models.BinaryField()
    url=models.CharField(max_length=1000)
    project_details=models.CharField(max_length=2000)

class user_chat(models.Model):
    user1=models.IntegerField(null=True)
    user2=models.IntegerField(null=True)
    receive=models.CharField(max_length=500,null=True)
    send=models.CharField(max_length=500,null=True)
    s_date_time=models.DateTimeField(null=True)
    r_date_time=models.DateField(null=True)


class course(models.Model):
    c_name=models.CharField(max_length=100)
    c_duration=models.CharField(max_length=20)
    staffs=models.CharField(max_length=500)
    c_details=models.CharField(max_length=5000)
    c_books=models.CharField(max_length=1000)


class background(models.Model):
    img=models.BinaryField()
    project_details=models.CharField(max_length=2000)