from fastapi import FastAPI,UploadFile,File
from db import *
import uvicorn
import s3
app=FastAPI(title="APi Developer With S3 Buket")

@app.get("/all/images", tags="Show All Images")
async def show():
    d = s3.show_all()
    return d

@app.get("/download/{name}", tags="Download one Image")
async def download_one_fle(name):
    f = s3.downloadone(name)
    return f

@app.post("/uploadfile", tags="Upload One Image")
async def upload_one_file(file:UploadFile = File()):
    name=file.filename
    f=file.file
    d = s3.uploadfile(f,name)
    return str(d)

@app.delete("/delete/{name}", tags="Delete One Image")
async def delet_one_file(name):
    r=s3.delete_file(name)
    return str(r)

if __name__=="__main__":
    uvicorn.run(app="main:app",port=5800, host="0.0.0.0", reload=True)
    #dfdjfdj