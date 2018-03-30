from accounts.models import room_form
rf = room_form.objects.get(pk=2)
rf.room_no = 'L23'
rf.save()