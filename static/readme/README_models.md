# Overview of all models used

## About app

````
class Contact(models.Model):**  
    """  
    Stores information from contact form  
    """  
    name = models.CharField(max_length=100)  
    email = models.EmailField(max_length=100)  
    message = models.TextField()  
    sent_on = models.DateField(auto_now_add=True)  
    read = models.BooleanField(default=False)
```` 

## Blog

````
class Article(models.Model):
    """  
    Containes one blog article  
    """  
    author = models.ForeignKey(  
        User,  
        null=True,  
        on_delete=models.SET_NULL,  
        related_name="articles")  
    title = models.CharField(max_length=255)  
    published = models.BooleanField(default=False)  
    publish_on = models.DateTimeField()  
    updated_on = models.DateTimeField(auto_now=True)  
    content = models.TextField()  
    image = models.ImageField(null=True, blank=True)  

    def __str__(self):  
     &nbsp; &nbsp;    return self.title

    @property  
    def number_of_comments(self):  
         &nbsp; &nbsp;return Article_Comment.objects.filter(  
         &nbsp; &nbsp; &nbsp; &nbsp;    article=self, visible=True).count()


class Article_Comment(models.Model):
    """
    Contains one comment on specific blog article
    """
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="comments")
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='article_commenter')
    comment = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user} commenting on {self.article} on {self.posted_on}"
````

## Events
````
class Event(models.Model):
    """
    Contains information about a specific Event/Course
    """
    title = models.CharField(max_length=255)
    time = models.DateTimeField()
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    max_capacity = models.IntegerField()
    cost = models.FloatField()
    publish_on = models.DateTimeField()
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    # Retrieves number of reserved spots for event
    # Includes booking being made (5-minute limit)
    @property
    def booked_spots(self):
        """ Retrieves number of reserved spots for event """

        # Remove all uncofirmed bookings older than 5 minutes
        Event_Registration.remove_unconfirmed_registrations()

        # Count reservations for this event
        return Event_Registration.objects.filter(event=self).count()

    # Retrieves number of available spots for event
    @property
    def available_spots(self):
        """ Retrieves number of available spots for event """
        return self.max_capacity - self.booked_spots


class Event_Registration(models.Model):
    """
    Registration for a specific event
    """
    event = models.ForeignKey(
        Event,
        on_delete=models.SET_NULL,
        null=True,
        related_name='participant')
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='courses')
    created_on = models.DateTimeField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)
    event_title = models.CharField(max_length=255)
    event_time = models.DateTimeField()
    event_cost = models.FloatField()

    def __str__(self):
        return self.event_title

    # Remove all registrations that has not been confirmed after five minutes
    @staticmethod
    def remove_unconfirmed_registrations():
        """
        Remove all event registrations that has not been
        confirmed within five minutes
        """
        cutoff_time = timezone.now() - timedelta(minutes=5)
        Event_Registration.objects.filter(
            created_on__lt=cutoff_time, confirmed=False).delete()
````
