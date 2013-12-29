Flask-AutoSaveFileField - Set and forget file uploads in Flask
----

Requirements: Flask-Uploads, Flask-WTF

1. File is saved automatically without any work to your upload set.
2. Populates your sqlalchemy object with a filename when using wtform's form.populate_obj(obj).
2. Prepends a link to the uploaded file right before the file input widget with the 'file-url' css class.
3. Does not clear out your existing upload if no file is uploaded on subsequent form submits.


```
documents = UploadSet('documents', DOCUMENTS)

class MyForm(Form):
    name = TextField()
    budget_upload = AutoSaveFileField(upload_set=documents)
    
    
@app.route('/my_view', methods=['POST'])
def my_view():
    form = MyForm()
    obj = MyModel()
    if form.validate_on_submit():
        form.populate_obj(obj)

```
