from audioop import reverse
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )
    # 13 liniyada bug bor agar commentdan ob tashlansa error beradi
    #summary = models.CharField(max_length=400)
    body = models.TextField()

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('post_detail.html', args=[str(self.pk)])
