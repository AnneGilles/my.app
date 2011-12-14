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
#from my.band.browser.utils import myapp_resource_vocab


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


@tile('addform', interface=Band, permission="add")
class BandAddForm(BandForm, Form):
    __metaclass__ = plumber
    __plumbing__ = AddPart

    def save(self, widget, data):
        add_band(self.request,
                 self.model,
                 data.fetch('bandform.title').extracted,
                 data.fetch('bandform.description').extracted,
                 data.fetch('bandform.resource').extracted,
                 data.fetch('bandform.account').extracted,
                 data.fetch('bandform.estimated').extracted,
                 data.fetch('bandform.beginning').extracted,
                 data.fetch('bandform.duedate').extracted)


@tile('editform', interface=Band, permission="edit")
class BandEditForm(BandForm, Form):
    __metaclass__ = plumber
    __plumbing__ = EditPart

    def save(self, widget, data):
        update_band(self.request,
                    self.model,
                    data.fetch('bandform.title').extracted,
                    data.fetch('bandform.description').extracted,
                    data.fetch('bandform.resource').extracted,
                    data.fetch('bandform.account').extracted,
                    data.fetch('bandform.estimated').extracted,
                    data.fetch('bandform.beginning').extracted,
                    data.fetch('bandform.duedate').extracted)
