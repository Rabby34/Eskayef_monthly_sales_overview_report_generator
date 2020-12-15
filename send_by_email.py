# import sys
#
# import Cover_pic
# import Cumulative_sales_target
# import add_text_to_cumulative
# import title_of_cumulative_sales_target
# import top5_brand_changed
# # import top5_brand_contribution
# import brand_contribution_image_change
# import top5_brand_return
# import top10_chemist_return
# # import top9_nsm
#
# # import top9_nsm_with_target_and_outstanding
# import all_nsm_box_style
#
# import outstanding_pie
# import aging_days
# import add_all
# import add_text_to_final_pic
# import add_customer_names_in_final_pic
# import add_aging_values_in_final_pic
# import All_kpi_values_added
# sys.exit()

import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ------------ Group email ----------------------------------------
msgRoot = MIMEMultipart('related')
me = 'erp-bi.service@gmail.com'                           #give from email
to = ['', '']
cc = ['', '']
bcc = ['md.fazle.rabby34@gmail.com', '']                  #give to email

recipient = to + cc + bcc

subject = "Sales Overview of SK+F Using Infographics"

email_server_host = ''                                      #give mail server
port =  44                                                    #give port number

msgRoot['From'] = me

msgRoot['To'] = ', '.join(to)
msgRoot['Cc'] = ', '.join(cc)
msgRoot['Bcc'] = ', '.join(bcc)
msgRoot['Subject'] = subject

msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

msgText = MIMEText('This is the alternative plain text message.')
msgAlternative.attach(msgText)

msgText = MIMEText("""
                       <img src="cid:report" height='3180', width='1270'><br>

                       """, 'html')

msgAlternative.attach(msgText)

# --------- Set Credit image in mail   -----------------------
fp = open('./final_photo_has_to_be_send.png', 'rb')
report = MIMEImage(fp.read())
fp.close()

report.add_header('Content-ID', '<report>')
msgRoot.attach(report)

# # ----------- Finally send mail and close server connection ---
print('-----------------------------------------------')
print('sending mail')
server = smtplib.SMTP(email_server_host, port)
server.ehlo()
server.sendmail(me, recipient, msgRoot.as_string())
server.close()
print('mail sent')
print('-----------------------------------------------')
