from cone.tile import registerTile
from cone.app.browser.layout import ProtectedContentTile
from my.app.model import (
    MyApp,
    Band,
    Track,
)

from pyramid.view import static
static_view = static('static')

registerTile('content',
             'cone.app:browser/templates/listing.pt',
             interface=MyApp,
             class_=ProtectedContentTile,
             permission='login',
             strict=False)


registerTile('content',
             'cone.app:browser/templates/listing.pt',
             interface=Band,
             class_=ProtectedContentTile,
             permission='login',
             strict=False)


registerTile('content',
             'my.app:browser/templates/track.pt',
             interface=Track,
             class_=ProtectedContentTile,
             permission='login',
             strict=False)
