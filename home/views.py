from django.core.mail import message
from util.Common import *
from home.forms import SignUpForm

class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def error_404(request, exception):
    return render(request, 'home/404.html',{})

@login_required
def home(request):
    return render(request, 'home/home.html', {})

@method_decorator([login_required], name='dispatch')
class Profile(View):
    template_name = "home/profile.html"

    def get(self, request, *args, **kwargs):
        if not request.user.get_name_is_empty():
            messages.error(request, "Please complete your profile")

        profile_info = {}
        profile_info['First Name'] = request.user.first_name
        profile_info['Last Name'] = request.user.last_name
        profile_info['Username'] = request.user.username
        profile_info['Email'] = request.user.email
        context = {
            'profile_info':profile_info
        }
        print(profile_info)
        return render(request, self.template_name,context)

    def post(request, self, *args, **kwargs):
        return HttpResponse("Invalid Method")
