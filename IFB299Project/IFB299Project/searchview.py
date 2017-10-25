import operator

from django.db.models import Q


class BlogSearchListView(BlogListView):
    """
    Display a Blog List page filtered by the search query.
    """
    paginate_by = 10

    def get_queryset(self):
        result = super(BlogSearchListView, self).get_queryset()

        query = self.request.GET.get('q')


        return result