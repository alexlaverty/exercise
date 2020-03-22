import django_tables2 as tables
from .models import Entries

class EntriesTable(tables.Table):
    class Meta:
        model = Entries
        fields = ('DateTime', 'Username','String_Value') # fields to display
