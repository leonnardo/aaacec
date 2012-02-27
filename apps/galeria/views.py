# -*- coding: utf-8 -*-
import flickrapi
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
import logging
logging.basicConfig()

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

def require_flickr_auth(view):
    '''View decorator, redirects users to Flickr when no valid
    authentication token is available.
    '''

    def protected_view(request, *args, **kwargs):
        request.session['token'] = settings.FLICKR_API_TOKEN
        if 'token' in request.session:
            token = request.session['token']
            log.info('Getting token from session: %s' % token)
        else:
            token = None
            log.info('No token in session')

        f = flickrapi.FlickrAPI(settings.FLICKR_API_KEY,
               settings.FLICKR_API_SECRET, token=token,
               store_token=False)

        if token:
            # We have a token, but it might not be valid
            log.info('Verifying token')
            try:
                f.auth_checkToken()
            except flickrapi.FlickrError:
                token = None
                del request.session['token']

        if not token:
            # No valid token, so redirect to Flickr
            log.info('Redirecting user to Flickr to get frob')
            #(token, frob) = f.get_token_part_one(perms='write')
            url = f.web_login_url(perms='write')
            return HttpResponseRedirect(url)

        # If the token is valid, we can call the decorated view.
        log.info('Token is valid')

        return view(request, *args, **kwargs)

    return protected_view

def callback(request):
    log.info('We got a callback from Flickr, store the token')

    f = flickrapi.FlickrAPI(settings.FLICKR_API_KEY,
           settings.FLICKR_API_SECRET, store_token=False)

    frob = request.GET['frob']
    token = f.get_token(frob)
    request.session['token'] = token

    return HttpResponseRedirect('/content')

def flickr(request):
    token = settings.FLICKR_API_TOKEN
    f = flickrapi.FlickrAPI(settings.FLICKR_API_KEY,
            settings.FLICKR_API_SECRET,token=token,
            store_token=False)
    return f

# view que pega as informações de todos os albuns
def getPhotosets(flickr):
    photoset_list = flickr.photosets_getList().find('photosets').findall('photoset')
    photoset_list_array = []
    for photoset in photoset_list:
        photoset_id = photoset.attrib['id']
        photoset_title = photoset.find('title').text
        photoset_list_array.append({
                'id':photoset_id,
                'name':photoset_title})
    return photoset_list_array

def getPhotos(flickr,id):
        photoset_photos = flickr.photosets_getPhotos(photoset_id=id, extras='url_sq').find('photoset').findall('photo')
        photoset_photos_list = []
        for photo in photoset_photos:
            thumbnail = photo.attrib['url_sq']
            photo_id = photo.attrib['id']
            secret = photo.attrib['secret']
            farm = photo.attrib['farm']
            server = photo.attrib['server']
            title = photo.attrib['title']
            photo_url = 'http://farm%s.static.flickr.com/%s/%s_%s_b.jpg' % (farm,server,photo_id,secret) 
            photoset_photos_list.append({'url':photo_url,'thumb':thumbnail})
        return photoset_photos_list

@require_flickr_auth
def ListarFotos(request, id):
    f = flickr(request)
    fotos = getPhotos(f, id)
    return render_to_response(
                'templates/galeria/index.html',
                locals(),
                context_instance=RequestContext(request)
           )


@require_flickr_auth
def index(request):
    f = flickr(request)
    photosets = getPhotosets(f)
    output = []
    for photoset in photosets:
        photos = getPhotos(f,photoset['id'])
        output.append({
                        'album_name':photoset['name'],
                        'photo_list': photos})
                        
    context = {'output':output}
    return render_to_response('galeria/index.html', context, context_instance=RequestContext(request))
