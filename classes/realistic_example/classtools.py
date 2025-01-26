"Assorted class utilities and tools"

class Attr_Display:
    """
    Provides and inheritance print overload method that displays instances with their class names and name=value pair for each attribute stored on the instance itself (but not attrs inherited from its classes). Can be mixed into any class, and will work on any instance.
    """
    def get_attrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append("%s=%s" % (key, getattr(self, key)))
        return", ".join(attrs)
    def __str__(self):
        return "[%s: %s]" % (self.__class__.__name__, self.get_attrs())