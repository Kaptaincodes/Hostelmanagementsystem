from django.db import models


class Hostel(models.Model):
    """
    Model for individual hostels.
    """
    name = models.CharField(max_length=10, default='xyz')
    total_bedspace = models.IntegerField(default=0)                # total rooms in the hostel
    total_available_bedspace = models.IntegerField(default=0)      # total available rooms for booking purposes
    total_booked_bedspace = models.IntegerField(default=0)         # total rooms that are already booked
    # hostel_type = models.CharField(max_length=8)

    def __str__(self):
        return self.name

    def available_rooms(self):
        return self.total_available_rooms
