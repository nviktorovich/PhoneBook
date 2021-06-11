from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from .models import SimpleBook

# Create your views here.

from django.views import View


class BookView(View):

    def get(self, request):
        res = SimpleBook.objects.all().order_by('second_name')
        return render(request, 'pb.html', {'res': res})


class NewContact(View):
    def get(self, request):
        res = request
        return render(request, 'nc.html', {'res': res})

    def post(self, request):
        new_entry = SimpleBook(
            first_name=request.POST.get("first_name"),
            second_name=request.POST.get("second_name"),
            fathers_name=request.POST.get("fathers_name"),

            phone1=request.POST.get("phone1"),
            phone2=request.POST.get("phone2"),
            phone3=request.POST.get("phone3"),

            email=request.POST.get("email"),

            company=request.POST.get("company"),
            job_title=request.POST.get("job_title"),
            address=request.POST.get("address"),

            more=request.POST.get("more")
        )
        new_entry.save()
        return HttpResponseRedirect("/phone_book/")


class UpdateContact(View):
    def get(self, request):
        obj = SimpleBook.objects.get(id=request.GET.get('id'))
        return render(request, 'uc.html', {'res': obj})

    def post(self, request):
        updated_entry = SimpleBook.objects.get(id=request.POST.get('id'))  # object to update
        updated_entry.first_name = request.POST.get('first_name')
        updated_entry.second_name = request.POST.get('second_name')
        updated_entry.fathers_name = request.POST.get('fathers_name')
        updated_entry.phone1 = request.POST.get('phone1')
        updated_entry.phone2 = request.POST.get('phone2')
        updated_entry.phone3 = request.POST.get('phone3')
        updated_entry.email = request.POST.get('email')
        updated_entry.company = request.POST.get('company')
        updated_entry.job_title = request.POST.get('job_title')
        updated_entry.address = request.POST.get('address')
        updated_entry.more = request.POST.get('more')
        updated_entry.save()
        return HttpResponseRedirect("/phone_book/")


class RemoveContact(View):
    def get(self, request):
        obj = SimpleBook.objects.get(id=request.GET.get('id'))
        return render(request, 'rc.html', {'res': obj})

    def post(self, request):
        removed_entry = SimpleBook.objects.get(id=request.POST.get('id'))  # object to update
        removed_entry.delete()
        return HttpResponseRedirect("/phone_book/")
