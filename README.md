Set and forget file uploads with Flask-Upload.
Requirements: Flask-Uploads, Flask-WTF

1. File is saved automatically without any work to you upload set.
2. Populates your sqlalchemy object with a filename when using wtforms form.populate_obj(sqla_obj)
2. Prepends a link to the uploaded file right before the file input widget with the 'file-url' css class.


from flaskext.uploads import UploadSet, DOCUMENTS, configure_uploads
documents = UploadSet('documents', DOCUMENTS)
budget_upload = AutoSaveFileField(upload_set=documents)
