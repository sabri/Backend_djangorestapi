from django.db import models


class Document(models.Model):
    document = models.CharField(max_length=2000, unique=True)


class Dictionary(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='annotations')
    text = models.CharField(max_length=200)
    label = models.CharField(max_length=200)
    start = models.CharField(max_length=200)
    end = models.CharField(max_length=200)

    class Meta:
        unique_together = ['document', 'text', 'label', 'end', 'start']
        ordering = ['text', 'label', 'end', 'start']

    def __str__(self):
        return "{}".format(self.text, self.label, self.end, self.start)
