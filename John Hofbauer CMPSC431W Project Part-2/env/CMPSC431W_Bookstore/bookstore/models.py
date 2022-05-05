from django.db import models

# Create your models here.


class Book(models.Model):
    ISBN = models.CharField(max_length=20, primary_key=True)
    Title = models.CharField(max_length=255)
    Subject = models.CharField(max_length=255)
    keywords = models.TextField()
    Price = models.FloatField()
    StockLevel = models.IntegerField()
    NumberOfPages = models.IntegerField()
    PublicationDate = models.DateField()
    Language = models.CharField(max_length=255)
    Publisher = models.CharField(max_length=255)

    def __str__(self):
        return self.Title 

class Author(models.Model):
    AuthorID = models.AutoField(primary_key=True)
    ISBN = models.ForeignKey(Book, on_delete=models.CASCADE)
    FullName = models.CharField(max_length=255)

    def __str__(self):
        return self.FullName 
    
class Order(models.Model):
    OrderId = models.AutoField(primary_key=True)
    ISBN = models.ForeignKey(Book, on_delete=models.CASCADE)
    Username = models.CharField(max_length=255)
    Amount = models.IntegerField()
    Price = models.FloatField()
    Date = models.DateTimeField()

    def __str__(self):
        return self.ISBN.Title 

class TrustFactor(models.Model):
    TrustId = models.AutoField(primary_key=True)
    UsernameGiver = models.CharField(max_length=255)
    UsernameReceiver = models.CharField(max_length=255)
    Score = models.IntegerField()

    def __str__(self):
        return self.UsernameGiver + "  " +  self.UsernameReceiver

    class Meta:
        unique_together = (("UsernameGiver", "UsernameReceiver"),)
    

class Comments(models.Model):
    CommentId = models.AutoField(primary_key=True)
    ISBN = models.ForeignKey(Book, on_delete=models.CASCADE)
    Username = models.CharField(max_length=255)
    Comment = models.TextField()

    def __str__(self):
        return self.Username 

    class Meta:
        unique_together = (("ISBN", "Username"),)

class Usefulness(models.Model):
    UsefulnessId = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=255)
    CommentId = models.ForeignKey(Comments, on_delete=models.CASCADE)
    Score = models.IntegerField()

    def __str__(self):
        return self.Username 

    class Meta:
        unique_together = (("Username", "CommentId"),)
