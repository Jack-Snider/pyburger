from django.http import HttpResponse

def main( request ):
    return HttpResponse( "Hello, this is pyburger" )

def burger_list( request ):
    return HttpResponse( "This is burger list of pyburger" )