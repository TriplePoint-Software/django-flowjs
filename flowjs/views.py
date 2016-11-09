import json
from django import forms, http
from django.shortcuts import get_object_or_404
from django.views.generic.base import View

from .models import FlowFile, FlowFileChunk


class FlowFileForm(forms.Form):
    file = forms.FileField()

def upload(request):
    request_method_data = getattr(request, request.method)
    flowChunkNumber = int(request_method_data.get('flowChunkNumber'))
    flowChunckSize = int(request_method_data.get('flowChunkSize'))
    flowCurrentChunkSize = int(
        request_method_data.get('flowCurrentChunkSize'))
    flowTotalSize = int(request_method_data.get('flowTotalSize'))
    flowIdentifier = request_method_data.get('flowIdentifier')
    flowFilename = request_method_data.get('flowFilename')
    flowRelativePath = request_method_data.get('flowRelativePath')
    flowTotalChunks = int(request_method_data.get('flowTotalChunks'))

    # identifier is a combination of session key and flow identifier
    if not request.session.session_key:
        request.session.save()
    identifier = (
        '%s-%s' % (request.session.session_key, flowIdentifier))[:200]

    if request.method == 'GET':
        get_object_or_404(FlowFileChunk, number=flowChunkNumber,
                          parent__identifier=identifier)
        return http.HttpResponse(identifier)
    elif request.method == 'POST':
        # get file or create if doesn't exist the identifier
        flow_file, created = FlowFile.objects.get_or_create(identifier=identifier, defaults={
            'original_filename': flowFilename,
            'total_size': flowTotalSize,
            'total_chunks': flowTotalChunks,
        })

        # validate the file form
        form = FlowFileForm(request.POST, request.FILES)
        if not form.is_valid():
            return http.HttpResponseBadRequest(form.errors)

        # avoiding duplicated chucks
        chunk, created = flow_file.chunks.get_or_create(number=flowChunkNumber, defaults={
            'file': form.cleaned_data['file'],
        })

        return http.HttpResponse(json.dumps({
            'identifier': flow_file.identifier,
            'url': flow_file.url,
            'name': flow_file.original_filename,
            'ext': flow_file.extension,
            'id': flow_file.id
        }), content_type="application/json")
        
def check_state(request):
    if request.method == 'GET':
        flow = get_object_or_404(
            FlowFile, identifier=request.GET.get('identifier', ''))
        return http.HttpResponse(flow.state)
    return http.HttpResponse("Only 'GET' is allowed'")

