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
        diff = 7*(pair.week-1)+7*4*count+pair.day
        new_date = timedelta(days=diff) + settings.SEMESTER_BEGIN - timedelta(days=settings.SEMESTER_BEGIN.isoweekday()-1)
        time=new_date
        if time<=settings.SEMESTER_END:
            if time>=settings.SEMESTER_BEGIN:
                dates.append(new_date)
            i+=1
        else:
            break

    return dates