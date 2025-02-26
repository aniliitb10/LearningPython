class Program:
    language: str = 'python'

    def instance_method(self, *args):
        return f'args: [{self} {args}]'

    @classmethod
    def class_method(cls, *args):
        return f'args: [{cls} {args}]'

    @staticmethod
    def static_method(*args):
        return f'args: [{args}]'

    def free_method(*args):
        return f'args: [{args}]'

    def __repr__(self):
        return 'Program'

    def __str__(self):
        return repr(self)
