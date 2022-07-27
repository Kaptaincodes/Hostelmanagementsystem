from hostel.models import Hostel


def total_rooms_available():
    """
    Returns total number of available rooms for booking purposes.
    """
    try:
        rooms = 0
        for hostel in Hostel.objects.all():
            rooms += hostel.available_rooms()
        return rooms
    except:
        return 0


def generate_choices_of_hostels():
    """
    Returns a tuple of hostel and the corresponding 'key'
    """
    temp = (('1', 'PETER JASPER AKINOLA'),
            ('2', 'JOSEPH ADETILOYE HOSTEL'),
            ('3', 'DIOSES OF LAGOS WEST FEMALE HOSTEL'),
            ('4','UNIVERSITY FEMALE HOSTEL')
            # Add a new hostel here. Eg. ('4', 'hostelName'),
            )
    return temp
