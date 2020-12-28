import cv2
import dropbox
import time
import random

start_time = time.time()

def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = true
    while(result):
        ret,frame = videoCaptureObject.read()
        img_name = "img"+str(number)+".png"
        cv2.imwrite(img_name, frame)
        start_time = time.time
        result = false
    return img_nameprint("snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows



def upload_file(img_name):
    access_token = ""
    file = img_namefile_from = filefilke_to="/testFolder/+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)
        print("file uploaded")


def main():
    while(true):
        if((time.time() - start_time) >= 5):
            name = take_snapshot()
            upload_file(name)

main()                    