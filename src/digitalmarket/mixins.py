from django.shortcuts import get_object_or_404



class MultiSlugMixim(object):
    model = None

    def get_object(self, *args, **kwargs):
        slug = self.kwargs.get("slug")
        ModelClass = self.model
        if slug is not None:
            try:
                obj = get_object_or_404(ModelClass, slug=slug)
            except ModelClass.MultupleObjectsReturned:
                obj = ModelClass.objects.filter(slug=slug).order_by("-title").first()
        else:
            obj = super(MultiSlugMixim, self).get_object(*args, **kwargs)
        return obj 