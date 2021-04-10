from django.shortcuts import render, get_object_or_404, get_list_or_404


# class DetailObjectMixin:
#     model = None
#     template = None
#     context = 'data'
#     query = None
#
#     def get_object(self, request, id):
#         try:
#             obj = get_object_or_404(self.model, id=id)
#             return render(request, self.template, context={self.context: obj})
