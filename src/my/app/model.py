from cone.app.model import (
    BaseNode,
    Properties,
    BaseMetadata,
    NodeInfo,
    registerNodeInfo
    )


class MyApp(BaseNode):

    node_info_name = 'myapp'

    def __init__(self, name=None, parent=None):
        self.__name__ = name
        self.__parent__ = parent
        for i in range(10):
            self[str(i)] = Band()
    
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

    node_info_name = 'band'
    
    def __init__(self, name=None, parent=None):
        self.__name__ = name
        self.__parent__ = parent
        for i in range(10):
            self[str(i)] = Track()

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
        md.title = 'Band: %s' % self.name
        return md

info = NodeInfo()
info.title = 'Band'
info.description = 'This is a band'
info.addables = ['track']
#info.icon = 'url/to/icon'
info.node = Band
registerNodeInfo('band', info)


class Track(BaseNode):

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
        md.title = 'Track: %s' % self.name
        return md

info = NodeInfo()
info.title = 'Track'
info.description = 'This is a track'
info.addables = []
#info.icon = 'url/to/icon'
info.node = Track
registerNodeInfo('track', info)
