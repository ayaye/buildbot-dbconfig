from klein import Klein
from twisted.internet import defer
from twisted.internet import threads
import json

from buildbot import config

def getDbConfigObjectId(master, name="config"):
    return master.db.state.getObjectId(name, "DbConfig")

class Api(object):
    app = Klein()

    def __init__(self, ep):
        self.ep = ep
        self._cfg = {}

    @app.route("/config", methods=['GET'])
    @defer.inlineCallbacks
    def getConfig(self, request):
        request.setHeader('Content-Type', 'application/json')
        name = request.args.get(b'name',['_'])[0].decode('utf8')
        if name not in self._cfg:
            self._cfg[name] = yield self.loadCfg(name)
        defer.returnValue(json.dumps(self._cfg[name]))

    @app.route("/config", methods=['PUT'])
    @defer.inlineCallbacks
    def putConfig(self, request):
        """I save the config, and run check_config, potencially returning errors"""
        request.setHeader('Content-Type', 'application/json')
        name = request.args.get(b'name',['_'])[0].decode('utf8')
        cfg = json.loads(request.content.read())
        if name not in self._cfg or cfg != self._cfg[name]:
            self._cfg[name] = cfg
            try:
                err = yield self.saveCfg(name,cfg)
            except Exception as e:  # noqa
                err = [repr(e)]
            if err is not None:
                defer.returnValue(json.dumps({'success': False, 'errors': err}))

        yield defer.returnValue(json.dumps({'success': True}))

    @defer.inlineCallbacks
    def saveCfg(self,name,cfg):
        oid = yield getDbConfigObjectId(self.ep.master)
        yield self.ep.master.db.state.setState(oid, name, cfg)

    @defer.inlineCallbacks
    def loadCfg(self,name):
        oid = yield getDbConfigObjectId(self.ep.master)
        try:
            cfg = yield self.ep.master.db.state.getState(oid, name)
            defer.returnValue(cfg)
        except Exception as e:
            defer.returnValue(json.dumps({}))
       
