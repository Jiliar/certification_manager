from enum import Enum

class Error(Enum):
    E001 = ("E001", "Error trying to configure application logs.")
    E002 = ("E002", "Error when trying to upload files to FTP server.")
    E003 = ("E003", "Error trying to get Certificates to read them.")
    
    E004 = ("E004", "Error trying to create table in DB.")
    E005 = ("E005", "Error trying to insert data into DB.")
    E006 = ("E006", "Error trying to get data from DB.")
    E007 = ("E007", "Error trying to list data from DB.")
    E008 = ("E008", "Error trying to update data in DB.")
    E009 = ("E009", "Error trying to delete data in DB.")
