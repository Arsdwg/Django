from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest

class ClubMiddleware(MiddlewareMixin):
    def progress_request(self, request):
        if request.path == '/register/' and request.method == 'POST':
            exp = int(request.POST.get('experience'))
            age = int(request.POST.get('age'))
            if age < 5:
                return HttpResponseBadRequest('иди в детский сад.')
            if exp < 1:
                request.club = 'Vagabond'
            elif 1 <= exp <= 2:
                request.club = 'Beginner'
            elif 2 <= exp <= 3:
                request.club = 'Simpleton'
            elif 3 <= exp <= 5:
                request.club = 'Knight'
            elif exp > 5:
                request.club = 'Duke'
            else:
                return HttpResponseBadRequest('не робит что-то , попробуй заного.')

        elif request.path == '/register/' and request.method == 'GET':
            setattr(request, 'club', 'клуб не определен.')