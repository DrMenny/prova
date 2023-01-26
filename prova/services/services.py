import sanic
from sanic import Sanic
from sanic_openapi import swagger_blueprint
from sanic_openapi.openapi2 import doc

from prova1.config.AppConfig import REPOPATH
from prova1.dao.fs_dao import JSONFSDAO

app = Sanic("Hello")
swagger_blueprint.url_prefix = "/api"
app.blueprint(swagger_blueprint)

dao = JSONFSDAO(repo_path=REPOPATH)


@app.get('/objects')
@doc.summary('Get all objects names')
async def list_objects(request):
    res = dao.all()
    return sanic.json(res)


@app.get('/objects/<name>')
@doc.consumes(doc.String(name='name'), location='path', required=True)
@doc.summary('Get single object')
async def get_object(request, name):
    res = dao.get_by_id(name)
    return sanic.json(res)


@app.post('/objects/<name>')
@doc.consumes(doc.JsonBody(), location='body', required=True)
@doc.consumes(doc.String(name='name'), location='path', required=True)
@doc.summary('Create new object')
async def create_object(request, name):
    obj = request.json
    dao.save(name, obj)
    print('OBJ:', obj)
    return sanic.json(f"object '{name}' saved")


@app.delete('/objects/<name>')
@doc.consumes(doc.String(name='name'), location='path', required=True)
@doc.summary('Delete object')
async def delete_object(request, name):
    dao.remove(name)
    return sanic.json(f"object '{name}' deleted")


app.run("0.0.0.0", port=8080, auto_reload=True)

