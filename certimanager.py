import fitz
import os
import json
import ftplib

from datetime import datetime
from app.utils.log import Log
from app.utils.error import Error
from app.utils.config import Config as config
from app.models.certificates_user import CertificateUser
from app.models.certificates_user_audit import CertificateUserAudit
from app.controllers.certificates_user_audit_controller import CertificateUserAuditController
from app.controllers.certificates_user_controller import CertificateUserController
from app.controllers.user_controller import UserController


current_datetime = datetime.now()
logging = Log.init_log_config()


def load_file(remotefile, localfile):
    try:
        ftp = ftplib.FTP(config.get_param('ftp','server'))
        ftp.login(config.get_param('ftp','user'), config.get_param('ftp','password'))
        with open(localfile, "rb") as file:
            ftp.storbinary('STOR %s' % remotefile, file)
    except Exception as e:
        logging.error("load_file(): {0} - Details: {1}".format(Error.E002.value, str(e)))
        
def get_details_from_files():
    try:
        path = config.get_param('paths','certificates')
        entries = [x for x in os.listdir(path) if '.pdf' in x]
        coords_header = (72, 86, 117, 96)
        result = []
        for entry in entries:
            origin_path = path+entry
            doc = fitz.open(origin_path)
            page1 = doc[0]
            words = page1.get_text("words")
            counter = 0
            identification_header = ''
            identification_paragraph = ''
            data = []
            for word in words:
                #C.C. Header
                if coords_header[0] == int(word[0]) and coords_header[1] == int(word[1]):
                    identification_header = word[4].replace('.', '')
                #C.C. Paragraph
                if word[4] == 'CC.':
                    identification_paragraph = words[counter + 1][4].replace('.', '')
                counter = counter + 1
            if identification_header != '' and identification_paragraph != '':
                data = dict([
                                ('identification_header', identification_header),
                                ('identification_paragraph', identification_paragraph),
                                ('origin_path', origin_path),
                            ])
                result.append(data)
    except Exception as e:
            logging.error("get_details_from_files(): {0} - Details: {1}".format(Error.E003.value, str(e)))
            
    return result


if __name__ == '__main__':
    #Verify FTP connection
    #Verify DB connection
    files = get_details_from_files()
    logging.info(json.dumps(files, sort_keys=True, indent=4))
    certificate_user_audit_ctrl = CertificateUserAuditController()
    certificate_user_ctrl = CertificateUserController()
    user_ctrl = UserController()
    
    for file in files:
         time_name = current_datetime.strftime("%d%m%Y_%H%M%S")
         time_formated = current_datetime.strftime("%d/%m/%Y %H:%M:%S")
         sql_time = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
         year = int(current_datetime.strftime("%Y"))
         name_file = file["identification_header"]+"_"+time_name+".pdf"
         ftp_path = config.get_param('ftp','http_path') + name_file
         log_msg = "Uploading file [ {0} ] - date: [ {1} ] - origin path: [ {2} ] - ftp path: [ "+ftp_path+" ]"
         msg = log_msg.format(name_file, time_formated, file["origin_path"], name_file)
         logging.info(msg)
         user_db = user_ctrl.get_by_identification(file["identification_header"])[0]
         certificate_user = CertificateUser(None, user_db.id, year, ftp_path, 1, sql_time)
         certificate_user_ctrl.insert(certificate_user)
         certificate_user_audit = CertificateUserAudit(None, msg, sql_time)
         certificate_user_audit_ctrl.insert(certificate_user_audit)