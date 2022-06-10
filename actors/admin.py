from django.contrib import admin

from actors.models import Actor


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    search_fields = ('actor_name',)
    list_filter = ('gender',)
    # Exception Type:	ProgrammingError
    # Exception Value:  can't adapt type 'Actor'
    # list_display = ['actor_name', 'age', 'gender', 'movies_count']
    list_display = ['actor_name', 'age', 'gender', ]
    readonly_fields = ['movies_count']

    def movies_count(self, obj):
        count = 0
        for mv in Actor.objects.raw('select * from movies_movie_actors '
                                    'where actor_id='
                                    '(select id from actors_actor where actor_name=%s)', [obj]):
            count += 1
        return str(count)

    movies_count.short_description = 'movie count'
