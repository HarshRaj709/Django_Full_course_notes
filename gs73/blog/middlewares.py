def my_middleware(get_response):
    print('1 time initializtion')           #ye sirf ek bar chalega only line no.2
    def my_function(request):
        print('this will work before View')             #ye humara views ke chlne se phle chalega
        response = get_response(request)
        print('this will work after view')          #ye views ke chlne ke bad chalega
        return response
    return my_function