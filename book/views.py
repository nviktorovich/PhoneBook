from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from .models import SimpleBook

# Create your views here.

from django.views import View


class BookView(View):

    def get(self, request):
        res = SimpleBook.objects.all()
        return render(request, 'pb.html', {'res': res})


class NewContact(View):
    def get(self, request):
        res = request
        return render(request, 'nc.html', {'res': res})

    def post(self, request):
        new_entry = SimpleBook(
            name=request.POST.get("name"),
            phone=request.POST.get("phone"),
            e_mail=request.POST.get("email"),
            more=request.POST.get("more")
        )
        new_entry.save()
        return HttpResponseRedirect("/phone_book/")


class UpdateContact(View):
    def get(self, request):
        obj = SimpleBook.objects.get(id=request.GET.get('id'))
        return render(request, 'uc.html', {'res': obj})

    def post(self, request):
        print('here')
        updated_entry = SimpleBook.objects.get(id=request.POST.get('id'))  # object to update
        updated_entry.name = request.POST.get('name')
        updated_entry.phone = request.POST.get('phone')
        updated_entry.e_mail = request.POST.get('email')
        updated_entry.more = request.POST.get('more')
        updated_entry.save()
        return HttpResponseRedirect("/phone_book/")