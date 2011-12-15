from plumber import plumber
from cone.app.model import (
    BaseNode,
    Properties,
    BaseMetadata,
    NodeInfo,
    registerNodeInfo,
    UUIDAttributeAware
    )


class MyApp(BaseNode):

    node_info_name = 'myapp'

    @property
    def properties(self):
        props = Properties()
        props.in_navtree = True
        props.action_list = True
        props.action_add = True
        return props

    @property
    def metadata(self):
        md = BaseMetadata()
        md.title = 'My App'
        return md

info = NodeInfo()
info.title = 'MyApp'
info.description = 'This is my app'
info.addables = ['band']
#info.icon = 'url/to/icon'
info.node = MyApp
registerNodeInfo('myapp', info)


class Band(BaseNode):
    __metaclass__ = plumber
    __plumbing__ = UUIDAttributeAware

    node_info_name = 'band'

    @property
    def properties(self):
        props = Properties()
        props.in_navtree = True
        props.action_list = True
        props.action_add = True
        props.action_edit = True
        return props

    @property
    def metadata(self):
        md = BaseMetadata()
        md.title = self.attrs.get('title')
        md.description = self.attrs.get('description')
        md.uid = self.attrs.get('uuid')
        md.creator = self.attrs.get('creator')
        md.created = self.attrs.get('created')
        md.modified = self.attrs.get('modified')
        return md

info = NodeInfo()
info.title = 'Band'
info.description = 'This is a band'
info.addables = ['track']
info.icon = 'myapp-static/B16_16.png'
info.node = Band
registerNodeInfo('band', info)


class Track(BaseNode):
    __metaclass__ = plumber
    __plumbing__ = UUIDAttributeAware

    node_info_name = 'track'

    @property
    def properties(self):
        props = Properties()
        props.in_navtree = True
        props.action_list = True
        props.action_add = True
        props.action_edit = True
        return props

    @property
    def metadata(self):
        md = BaseMetadata()
        md.title = self.attrs.get('title')
        md.description = self.attrs.get('description')
        md.uid = self.attrs.get('uuid')
        md.creator = self.attrs.get('creator')
        md.created = self.attrs.get('created')
        md.modified = self.attrs.get('modified')
        return md

info = NodeInfo()
info.title = 'Track'
info.description = 'This is a track'
info.addables = []
info.icon = 'myapp-static/T16_16.png'
info.node = Track
registerNodeInfo('track', info)
