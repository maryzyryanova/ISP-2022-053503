from main.models import Schedule
from django.conf import settings
from datetime import timedelta

def get_pairs(dicipline, group):
    pairs = Schedule.objects.filter(dicipline=dicipline, group=group).order_by('week','day','bell')
    time = settings.SEMESTER_BEGIN
    dates = []
    count = 0
    i = 0
    while True:
        if i==pairs.count():
            i = 0
            count+=1
        pair = pairs[i]
        new_date = timedelta(days=7*pair.week+7*4*count+pair.day-settings.SEMESTER_BEGIN.weekday()) + settings.SEMESTER_BEGIN
        time=new_date
        if time<settings.SEMESTER_END:
            dates.append(new_date)
            i+=1
        else:
            break

    return dates