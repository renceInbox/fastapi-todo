from fastapi import FastAPI, Form
from fastapi import Request, Response
from fastapi.responses import HTMLResponse

from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    context = {
        "request": request,
        "message": "Hello World",
        "title": "Home"
    }
    return templates.TemplateResponse("home.html", context)


@app.post("/add", response_class=HTMLResponse)
def post_add(request: Request, content: str = Form(...)):
    context = {"request": request, "content": content}
    return templates.TemplateResponse("todo/item.html", context)


@app.get("/edit/{item_id}", response_class=HTMLResponse)
def get_edit(request: Request, item_id: int):
    context = {"request": request, "content": "sample content"}
    return templates.TemplateResponse("todo/form.html", context)


@app.put("/edit/{item_id}", response_class=HTMLResponse)
def put_edit(request: Request, item_id: int):
    context = {"request": request, "content": "sample content"}
    return templates.TemplateResponse("todo/item.html", context)


@app.delete("/delete/{item_id}", response_class=Response)
def delete(item_id: int):
    pass
