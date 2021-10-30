from django.db import models

# Create your models here.
class Sensor_data(models.Model):
    # Define the attributes in the table
    person_number = models.IntegerField()
    distance = models.IntegerField()
    timestamp = models.DateTimeField(auto_now=True)

    # Define the to string method
    def __str__(self):
        return "Person" + str(self.person_number) + " Entered: " + str(self.distance) + " cms away at " + str(self.timestamp) 
    
