from django.db import models



# class User(models.Model):
#     username = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)

#     def __str__(self):
#         return self.username


#     def __str__(self):
#         return self.name


#     def __str__(self):
#         return f"Transaction by {self.user.username}"


class District(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Branch(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    

    