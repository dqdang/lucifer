from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, View
from lucifer import db_builder
from lucifer import db_worker
import main.settings as settings


def index(request):
    return HttpResponse("Hello, world.")


def update(request):
    db_builder.update()
    return HttpResponse("Updating database complete")


class BaseView(View):
    template_name = "base.html"

    def get(self, request):
        return render(request, self.template_name)


class ResultsView(View):
    template_name = "results.html"

    def post(self, request):
        stamina = request.POST.get("stamina")
        experience = request.POST.get("experience")
        efficient_dungeons = db_worker.find_efficient_dungeons(
            experience, stamina)
        return render(request, self.template_name, {"stamina": stamina, "experience": experience, "efficient_dungeons": efficient_dungeons})

    def get(self, request):
        return render(request, self.error_template_name)
