
from django.contrib import admin

from .models import State, Property_name
from .models import City
from .models import Locality
from .models import Sales
from .models import Suggestion

admin.site.register(State)
admin.site.register(City)
admin.site.register(Locality)
admin.site.register(Sales)
admin.site.register(Suggestion)
admin.site.register(Property_name)

