from django.http import HttpResponse
from django.views import generic
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy

from ksplib import persistent
from ksplib.model import Kerbals

from .models import Kerbal

# this method does not use the database, it parses the ascii file and stores the kerbals in the data structure
# the datastructure is then rendered to html

def list_basic(request):
    html = "<html><body>"
    filename = "r:\source\django\ksp_nico\kerbals\static\kerbals\persistent.sfs"

    # read all the kerbals into the data structure
    myKerbals = Kerbals(persistent.readKerbals(filename))
    living_kerbals = myKerbals.getKerbals(['Available', 'Assigned'])
    for kerbal in living_kerbals[:]:
        if (kerbal.career.flights > 0):
            html = html + "<h3>" + kerbal.__str__() + "</h3>"
            html = html + "<h4>" + kerbal.career.__str__() + "</h4>"
            html = html + "----"

    html = html + "</body></html>"
    return HttpResponse(html)


class myIndexView(generic.ListView):
    template_name = 'kerbals/index.html'

    # by default this returns the list in an object called object_list, so use 'object_list' in the html page.
    # but if 'context_object_name' is defined, then this returned list is named and can be accessed that way in html.
    context_object_name = 'my_kerbals_all'

    def get_queryset(self):
        return Kerbal.objects.all()


class myListView(generic.ListView):
    template_name = 'kerbals/list.html'

    # by default this returns the list in an object called object_list, so use 'object_list' in the html page.
    # but if 'context_object_name' is defined, then this returned list is named and can be accessed that way in html.
    context_object_name = 'my_kerbals_all'

    # clear the database and fill with values from the file
    Kerbal.objects.all().delete()

    filename = "r:\source\django\ksp_nico\kerbals\static\kerbals\persistent.sfs"

    # read all the kerbals into the data structure
    myKerbals = Kerbals(persistent.readKerbals(filename))
    all_kerbals = myKerbals.getKerbals(['Available', 'Assigned', 'Dead'])
    for kerbal in all_kerbals[:]:
        if (kerbal.career.flights > 0):
            k = Kerbal(name=kerbal.name, trait=kerbal.trait, state=kerbal.state, flights=int(kerbal.career.flights),
                       land=kerbal.career.land, orbit=kerbal.career.orbit)
            k.save()

    def get_queryset(self):
        return Kerbal.objects.all()

class myDeleteKerbal(DeleteView):
    model = Kerbal
    success_url = reverse_lazy('kerbals:index')