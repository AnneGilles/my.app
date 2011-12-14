from cone.app.model import (
    BaseNode,
    Properties,
    NodeInfo,
    registerNodeInfo
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

    def __getitem__(self, name):
        try:
            return self.storage[name]
        except KeyError:
            self.storage[name] = Band()
            return self.storage[name]

info = NodeInfo()
info.title = 'MyApp'
info.description = 'This is my app'
info.addables = ['band']
info.icon = 'url/to/icon'
info.node = MyApp


class Band(BaseNode):

    node_info_name = 'band'

    @property
    def properties(self):
        props = Properties()
        props.in_navtree = True
        props.action_list = True
        props.action.add = True
        props.action_edit = True
        return props

    def __getitem__(self, name):
        try:
            return self.storage[name]
        except KeyError:
            self.storage[name] = Track()
            return self.storage[name]

info = NodeInfo()
info.title = 'Band'
info.description = 'This is a band'
info.addables = ['track']
info.icon = 'url/to/icon'
info.node = Band
registerNodeInfo('band', info)


class Track(BaseNode):

    node_info_name = 'track'

    @property
    def properties(self):
        props = Properties()
        props.in_navtree = True
        props.action_list = True
        props.action.add = True
        props.action_edit = True
        return props

info = NodeInfo()
info.title = 'Track'
info.description = 'This is a track'
info.addables = []
info.icon = 'url/to/icon'
info.node = Track
registerNodeInfo('track', info)
