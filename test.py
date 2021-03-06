import dropbox
class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token
    def uploadFile(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        f=open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token='sl.AsXumhtKDMmHN8BEg-yQiPo1k1GtZhDI6sCxEoV1VVoRJJImBW8jCFzEUpsMjMyx4-tf9OLOjyCiKoz6K5WOntSzsfEGGAYxaOG1UTdk2UxLLEM82WWkxQNRBMS9NUMS-WFXiePI'
    TransferData1=TransferData(access_token)
    file_from=input("Enter the file path to transfer from device")
    file_to=input("Enter the file path to upload to dropbox")
    TransferData1.uploadFile(file_from,file_to)
    print("File has been moved")

main()