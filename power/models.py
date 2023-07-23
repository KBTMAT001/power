from django.db import models

# Create your models here.
class Enquiry(models.Model):
    """
    A model representing an Enquiry.

    This class defines the fields for an Enquiry object, which represents an enquiry
    or inquiry made by a person or company.

    :param company: The company name associated with the enquiry.
    :type company: str
    :param date_sent: The date and time the enquiry was sent.
    :type date_sent: datetime.datetime
    :param person: The name of the person associated with the enquiry.
    :type person: str
    :param email: The email address associated with the enquiry.
    :type email: str
    """

    company = models.CharField(max_length=200)
    date_sent = models.DateTimeField('date_sent')
    person = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        """
        Return a string representation of the Enquiry.

        This method returns the company name as the string representation of the Enquiry
        object, which can be useful for displaying the Enquiry in the admin interface
        or other contexts.

        :return: The company name of the Enquiry.
        :rtype: str
        """
        return self.company