from django.db import models

class Ping(models.Model):
    destination = models.CharField(max_length=50)
    packet_transmit = models.IntegerField()
    packet_receive = models.IntegerField()
    packet_loss_rate = models.FloatField()
    packet_loss_count = models.IntegerField()
    rtt_min = models.FloatField()
    rtt_avg = models.FloatField()
    rtt_max = models.FloatField()
    date = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f'{destination}-{date}'