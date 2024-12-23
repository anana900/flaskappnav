import connexion
import os
import pathlib

basedir = os.path.abspath(os.path.curdir)
basedir = pathlib.Path(__file__).parent.resolve()
connex_app = connexion.App(__name__, specification_dir=basedir)
app = connex_app

