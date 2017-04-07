from .models import Profile

def backend_save_profile(backend, user, response, *args, **kwargs):
    try:
        Profile.objects.create(user=user)
    except:
        pass
