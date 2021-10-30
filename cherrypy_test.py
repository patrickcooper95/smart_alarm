import os

import cherrypy

cherrypy.config.update({"server.socket_port": 80})


class OAuth2Server():
    @cherrypy.expose
    def index(self):
        return f"Hello, and welcome to the Fitbit Smart Alarm server."


config = {
    "global": {
        "server.socket_host": "0.0.0.0",
        "server.socket_port": int(os.environ.get("PORT", 80))
    }
}


cherrypy.quickstart(OAuth2Server(), "/", config=config)
