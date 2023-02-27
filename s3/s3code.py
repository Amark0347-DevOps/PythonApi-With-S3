import boto3
keys = boto3.Session(aws_access_key_id="AKIARWGZY7O4Q5JXXURG", aws_secret_access_key="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")
s3=keys.resource("s3")
mybukets=s3.Bucket("chauhanji1")
# def uplaodji(filesend):
#     mybukets.upload_file(filesend,"baby.pem")
#     return "Uploded"
def downloadone(myfile):
    mybukets.download_file(myfile, f"C:/Users/DevOps/Downloads/{myfile}")
    return "Downloads Success fully"

def uploadfile(myfile,filename1):
    hlo=myfile
    filename2=filename1
    mybukets.upload_fileobj(hlo,filename2)
    return "success"

def downlod():
    for i in mybukets.objects.all():
        print(i.key)
        mybukets.download_file(i.key, f'C:/Users/DevOps/Downloads/{i.key}')
    return "baby downloaded"

def delete_file(fileobj):
    mybukets.Object(fileobj).delete()
    # mybukets.delete(fileobj)
    return "Delete This file To The S3 Bucket"

def show_all():
    for i in mybukets.objects.all():
        yield i.key
#mybukets.upload_file(myfile2,filename2)
# for i in mybukets.objects.all():
#     print(i.key)
