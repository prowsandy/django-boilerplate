from util.Common import *
from home.forms import SignUpForm

class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

@login_required
def home(request):
    return render(request, 'home/home.html', {})
