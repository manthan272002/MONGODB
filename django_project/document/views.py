# views.py
from django.shortcuts import render
from .forms import DocumentForm
import pymongo

def index(request):
    form = DocumentForm()
    if request.method == 'POST':
        form = DocumentForm(request.POST)
        if form.is_valid():
            # Connect to MongoDB
            mongo_client = pymongo.MongoClient('mongodb://localhost:27017/')
            mongo_db = mongo_client['Document']

            # Insert document into MongoDB collection
            document_data = {
                "document_id": form.cleaned_data['document_id'],
                "document_type": form.cleaned_data['document_type'],
                "case_id": form.cleaned_data['case_id'],
                "update_date": form.cleaned_data['update_date'].strftime('%Y-%m-%d')
            }
            mongo_db['document.info'].insert_one(document_data)
            mongo_client.close()

            return render(request, 'document.html', {'form': DocumentForm(), 'message': 'Document saved successfully'})
    return render(request, 'document.html', {'form': form})
