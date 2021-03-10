import dropbox
class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token
    def uploadFile(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        f=open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token='sl.AswLuTaRenW7iZgsRJFGGIOoysizQiSfqp215KB_MWQSnd86U_UFPke0xqKcN_RavO6Ag8eXN_6UZXfOo7LqkFQd2KatCko2Iw3tziqHlxesVgwjQNdPxVnzySOJEP8qOreImLrD'
    TransferData1=TransferData(access_token)
    file_from=input("Enter the file path to transfer from device")
    file_to=input("Enter the file path to upload to dropbox")
    TransferData1.uploadFile(file_from,file_to)
    print("File has been moved")

main()