from wtforms.widgets.core import HTMLString, html_params
from flask_wtf.file import FileField

class UrlFileInput(object):
    def __init__(self, upload_set):
        self.upload_set = upload_set

    def __call__(self, field, **kwargs):
        kwargs.setdefault('id', field.id)
        if field.data:
            file_url = self.upload_set.url(field.data)
            return HTMLString('<a href="%s" class="file-url">%s</a><input %s>' % (file_url,
                                                                 field.data,
                                                                 html_params(name=field.name, type='file', **kwargs)))

        else: 
            return HTMLString('<input %s>' % html_params(name=field.name, type='file', **kwargs))

class AutoSaveFileField(FileField):

    def __init__(self, upload_set, **kwargs):
        self.upload_set = upload_set
        self.widget = UrlFileInput(upload_set)
        super(AutoSaveFileField, self).__init__(**kwargs)

    def populate_obj(self, obj, name):
        if self.data:
            setattr(obj, name, self.upload_set.save(self.data))



