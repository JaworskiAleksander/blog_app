from django.db import models
from django.utils import timezone
from django.urls import reverse,reverse_lazy

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    text = models.TextField()
    create_date = models.DateTimeField(default = timezone.now())
    publish_date = models.DateTimeField(blank = True, null = True)

    def publish(self):
        """
        release the post once this method is used
        set publish_date to the moment it's published
        save the post instance into database
        """
        self.publish_date = timezone.now()
        self.save()

    def approve_comments(self):
        """Once we have a list of comments posted by viewers, only the approved 
        ones will be displayed
        Grab those comments and filter them
        
        Returns:
            [type] -- [description]
        """
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})

    def __str__(self):
        """ We ain't done yet with this method, but for now it gets the job done
        
        Returns:
            [string] -- [string representation of a post title]
        """
        return self.title

class Comment(models.Model):
    """
    Comments are almost like a mini-posts
    'approved_comment' field name should match with filter parameter used in
     approve_comments method in Post class

    """
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length = 200)
    text = models.TextField()
    create_date = models.DateTimeField(default = timezone.now())
    approved_comment = models.BooleanField(default = False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse("post_list", kwargs={"pk": self.pk})    

    def __str__(self):
        return self.text
