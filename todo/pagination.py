from rest_framework.pagination import PageNumberPagination

class StandarResultsSetPagination(PageNumberPagination):
    page_size=150
    page_size_query_param = 'page_size'
    max_page_size = 1000
