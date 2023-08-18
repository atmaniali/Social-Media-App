from django.db import models


# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=200, blank=True)
    online = models.ManyToManyField('users.profile', blank=True)

    def __str__(self):
        return f"{self.name}-Group"

    def join_group(self, user):
        self.online.add(user)
        self.save()

    def leave_group(self, user):
        self.online.remove(user)
        self.save()


class Message(models.Model):
    user = models.ForeignKey('users.profile', on_delete=models.CASCADE, related_name='user_message')
    content = models.TextField(blank=True, null=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='group_message')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}-Message"
