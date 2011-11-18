from cone.tile import registerTile
from cone.app.browser.layout import ProtectedContentTile
from my.app.model import MyApp

registerTile('content',
             'your.app:browser/templates/myapp.pt',
             interface=MyApp,
             class_=ProtectedContentTile,
             permission='login')
