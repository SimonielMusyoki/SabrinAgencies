from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import ContactForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
#  +======================Start of Property Views =========
class PropertiesListView(ListView):
    model = Properties
    template_name='property/properties.html'
    context_object_name = 'properties'
    paginate_by = 15

class PropertiesDetailView(DetailView):
    model=Properties
    template_name='property/property_detail.html'
    context_object_name = "property"
    

class PropertiesCreateView(LoginRequiredMixin, CreateView):
    model=Properties
    template_name='property/property_form.html'
    fields = '__all__'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PropertiesUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Properties
    template_name='property/property_create.html'
    fields = '__all__'

    def form_valid(self, form):
        return super().form_valid(form)

class PropertiesDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Properties
    success_url ='/'
    template_name='property/property_delete.html'

def propertiesCreateView(request):
    form = PropertiesForm(request.POST)
    if form.is_valid():
        message = "message send successfully. Please wait for response on your email"
        form.save()
        return redirect('home')

    return render(request,'properties/property_create.html', {'form':form,'title': 'Contact'})

# +=======================End of property Views ============

#  +======================Start of Units Views =============
class UnitsListView(ListView):
    model = Units
    template_name = 'units/units.html'
    context_object_name = 'posts'
    paginate_by = 5

class CustomerUnitsListView(ListView):
    model = Units
    template_name = 'units/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

class UnitsDetailView(DetailView):
    model = Units
    template_name = 'units/unit_detail.html'
    context_object_name = 'posts'

class UnitsCreateView(LoginRequiredMixin, CreateView):
    model = Units
    template_name = 'units/unit_form.html'
    fields = '__all__'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class UnitsUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Units
    template_name = 'units/unit_form.html'
    fields = ['title','content','url']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class UnitsDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model =  Units
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# +================= End of Units Views=====================+
# +================= Start of Tenant Views =================
class TenantListView(ListView):
    model = Tenant
    template_name='tenants/tenants.html'
    context_object_name = 'posts'
    paginate_by = 15

class TenantDetailView(DetailView):
    model=Tenant
    template_name='tenants/tenant_detail.html'
    context_object_name = "posts"
    

class TenantCreateView(CreateView):
    model=Tenant
    template_name='tenants/tenant_create.html'
    fields = '__all__'
    def form_valid(self, form):
        return super().form_valid(form)

class TenantUpdateView(UpdateView):
    model = Tenant
    template_name='tenants/tenant_create.html'
    fields = '__all__'

    def form_valid(self, form):
        return super().form_valid(form)

class TenantDeleteView(DeleteView):
    model = Tenant
    success_url ='/'
    template_name='tenants/tenant_delete.html'


# +==================End of Tenant Views ===================
# +================= Lease Views =======================
class LeaseListView(ListView):
    model = Lease
    template_name = 'lease/lease.html'
    context_object_name = 'posts'
    paginate_by = 5

class CustomerLeaseListView(ListView):
    model = Lease
    template_name = 'lease/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

class LeaseDetailView(DetailView):
    model = Lease
    template_name = 'lease/lease-detail.html'
    context_object_name = 'posts'

class LeaseCreateView(LoginRequiredMixin, CreateView):
    model = Lease
    template_name = 'lease/lease_form.html'
    fields = '__all__'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class LeaseUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Lease
    template_name = 'lease/lease_form.html'
    fields = ['title','content','url']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class LeaseDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model =  Lease
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

# +=================== End of Lease Views ================
# +================= Payment Views =======================
class PaymentListView(ListView):
    model = Payment
    template_name = 'payment/homepayments.html'
    context_object_name = 'posts'
    paginate_by = 5

class CustomerPaymentListView(ListView):
    model = Payment
    template_name = 'payment/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

class PaymentDetailView(DetailView):
    model = Payment
    template_name = 'payment/payment-_detail.html'
    context_object_name = 'posts'

class PaymentCreateView(LoginRequiredMixin, CreateView):
    model = Payment
    template_name = 'payment/payment_form.html'
    fields = '__all__'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PaymentUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Payment
    template_name = 'payment/payment_form.html'
    fields = ['title','content','url']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PaymentDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model =  Payment
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

# +=================== End of Payment Views ================

# +================= Vendor Views =======================
class VendorListView(ListView):
    model = Vendor
    template_name = 'vendors/vendors.html'
    context_object_name = 'posts'
    paginate_by = 5

class CustomerVendorListView(ListView):
    model = Vendor
    template_name = 'vendors/vendor_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

class VendorDetailView(DetailView):
    model = Vendor
    template_name = 'vendors/vendor-detail.html'
    context_object_name = 'posts'

class VendorCreateView(LoginRequiredMixin, CreateView):
    model = Vendor
    template_name = 'vendors/vendor_form.html'
    fields = '__all__'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class VendorUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Vendor
    template_name = 'vendors/vendor_form.html'
    fields = ['title','content','url']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class VendorDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model =  Vendor
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

# +=================== End of Vendor Views ================

# +================= Expense Views =======================
class ExpenseListView(ListView):
    model = Expense
    template_name = 'expenses/expense.html'
    context_object_name = 'posts'
    paginate_by = 5

class CustomerExpenseListView(ListView):
    model = Expense
    template_name = 'expenses/expense_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

class ExpenseDetailView(DetailView):
    model = Expense
    template_name = 'expenses/expense_detail.html'
    context_object_name = 'posts'

class ExpenseCreateView(LoginRequiredMixin, CreateView):
    model = Expense
    template_name = 'expenses/expense_form.html'
    fields = '__all__'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ExpenseUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Expense
    template_name = 'expenses/expense_form.html'
    fields = ['title','content','url']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class ExpenseDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model =  Expense
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

# +=================== End of Expense Views ================
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5
    


class BlogPostListView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5
    

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'posts'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title','content','url']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title','content','url']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model =  Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def home(request):
    context = {
    'posts': Post.objects.all()
    }
    return render(request,'blog/home.html',context)


def about(request):
    return render(request,'blog/about.html', {'title': 'About'})

def contact(request):
    form = ContactForm()
    if form.is_valid():
        message = "message send successfully. Please wait for response on your email"
        form.save()
        return redirect('blog-home')

    return render(request,'blog/contact.html', {'form':form,'title': 'Contact'})

class Contact(CreateView):
    model = Messages
    template_name = 'blog/contact.html'
    fields = ['name','email','message']

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Projects
    template_name = 'blog/project_create.html'
    fields = ['title', 'idea','technologies','git_link', 'project_link','status']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class ProjectDetailView(DetailView):
    model = Projects
    template_name = 'blog/project-detail.html'
    context_object_name = 'posts'

class ProjectListView(ListView):
    model = Projects
    template_name = 'blog/projects.html'
    context_object_name = 'posts'
    ordering = ['-date_started']
    paginate_by = 5

class MessagesListView(ListView):
    model = Messages
    template_name = 'blog/message.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class ProjectUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Projects
    template_name = 'blog/project_create.html'
    fields = ['title', 'idea','git_link', 'project_link','status']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class ProjectDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model =  Projects
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
