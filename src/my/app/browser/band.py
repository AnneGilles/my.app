from plumber import plumber
from cone.tile import tile
from cone.app.browser.layout import ProtectedContentTile
from cone.app.browser.form import (
    Form,
    YAMLForm,
    )
from cone.app.browser.authoring import (
    AddPart,
    EditPart,
    )
from my.app.model import (
        Band,
    )


class BandForm(object):
    __metaclass__ = plumber
    __plumbing__ = YAMLForm

    form_template = 'my.app.browser:forms/band.yaml'

from cone.app.utils import (
    add_creation_metadata,
    update_creation_metadata,
    )


@tile('addform', interface=Band, permission="add")
class BandAddForm(BandForm, Form):
    __metaclass__ = plumber
    __plumbing__ = AddPart

    def save(self, widget, data):
        self.model.__name__ = self.model.uuid
        self.model.parent[str(self.model.uuid)] = self.model
        self.model.attrs['title'] = data.fetch('bandform.title').extracted
        self.model.attrs['description'] = data.fetch(
            'bandform.description').extracted
        add_creation_metadata(self.request, self.model.attrs)


@tile('editform', interface=Band, permission="edit")
class BandEditForm(BandForm, Form):
    __metaclass__ = plumber
    __plumbing__ = EditPart

    def save(self, widget, data):
        self.model.attrs['title'] = data.fetch('bandform.title').extracted
        self.model.attrs['description'] = data.fetch(
            'bandform.description').extracted
        update_creation_metadata(self.request, self.model.attrs)
