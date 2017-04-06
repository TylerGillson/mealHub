from .models import Profile

def backend_save_profile(backend, user, response, *args, **kwargs):
    Profile.objects.create(user=user)
