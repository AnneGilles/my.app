from plumber import plumber
from yafowil.base import UNSET
from cone.tile import tile
#from my.app.browser.utils import (
#    make_url,
#    format_date,
#    )
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


@tile('content', 'templates/band.pt', interface=Band,
      permission='login', strict=False)
class BandTile(ProtectedContentTile):

    @property
    def estimated(self):
        return '%.2f h' % self.model.metadata.estimated

    @property
    def resource(self):
        resource = self.model.metadata.resource
        if not resource:
            return []
        if isinstance(resource, basestring):
            return [resource]
        return resource

    @property
    def account(self):
        account = self.model.metadata.account
        if not account:
            return []
        if isinstance(account, basestring):
            return [account]
        return account

    # @property
    # def registered(self):
    #     return format_date(self.model.metadata.beginning)

    # @property
    # def unregistered(self):
    #     return format_date(self.model.metadata.duedate)


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
        #print "BandAddForm: trying to save form data"
        print "setting self.model.__name__ = 'foo'"
        self.model.__name__ = 'foo'
        #print "setting self.model to be parent of self.model.name"
        import uuid
        self.model.parent[str(uuid.uuid4())] = self.model
        #print "setting attr title: " + data.fetch('bandform.title').extracted
        self.model.attrs['title'] = data.fetch('bandform.title').extracted
        #print "setting attr description: " + data.fetch(
        #    'bandform.description').extracted
        self.model.attrs['description'] = data.fetch(
            'bandform.description').extracted


@tile('editform', interface=Band, permission="edit")
class BandEditForm(BandForm, Form):
    __metaclass__ = plumber
    __plumbing__ = EditPart

    def save(self, widget, data):
        #print "BandEditForm: trying to save form data"
        #print "title: " + data.fetch('bandform.title').extracted
        #print "descr: " + data.fetch('bandform.description').extracted
        self.model.attrs['title'] = data.fetch('bandform.title').extracted
        self.model.attrs['description'] = data.fetch(
            'bandform.description').extracted
        update_creation_metadata(self.request, self.model.attrs)
