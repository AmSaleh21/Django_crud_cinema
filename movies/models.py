from django.db import models

# Movie (name,production year, creation time,update time)
# + relation to be created from point 9


class Movie(models.Model):
    name = models.fields.CharField(verbose_name='movie name', max_length=25, unique=True)
    production_year = models.IntegerField(verbose_name='production year')
    actors = models.ManyToManyField('actors.actor')
    create_time = models.TimeField(verbose_name='Created at', auto_now=True)
    update_time = models.TimeField(verbose_name='Updated at', auto_now=True)

    def __str__(self):
        return f'{self.name}'
