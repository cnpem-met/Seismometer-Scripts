import smtplib 
import email.message as em


def emailContent(nome):
    email_content = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Amigo Secreto IQ + ECA</title>
            
            <style>
    
                .title{
                    text-align: center;
                    width: 500px;
                    font-size: 40px;
                    font-size: 40px;
                    color: white;
                    z-index: 2;
                }
    
                .title2{
                    text-align: center;
                    width: 500px;
                    font-size: 25px;
                    color: white;
                    z-index: 2;
                }
    
                .nome{
                    text-align: center;
                    width: 450px;
                    font-size: 75px;
                    color: white;
                    z-index: 2;
                }
    
                .title3{
                    text-align: center;
                    width: 500px;
                    font-size: 15px;
                    color: white;
                    z-index: 2;
                }
    
    
            </style>
        </head>
    
        <body style="margin: 0; padding: 0;">
            <table width="100%" height="650px" style="background: url('https://thevideoink.com/wp-content/uploads/2019/11/5679216_110719-cc-ss-christmas-presents-generic-img.jpg'); background-size: cover;">
                <tr><td>
                    <table width=500px height=500px bgcolor="black" style="margin:auto">
                        <tr><td>
                            <table>
                                <tr><td class="title"><font face="Comic sans MS">AMIGO SECRETO <br> IQ + ECA</font></td></tr>
                                <tr><td> </td></tr>
                                <tr><td> </td></tr>
                                <tr><td> </td></tr>
                                <tr><td> </td></tr>
                                <tr><td> </td></tr>
                                <tr><td> </td></tr>
                                <tr><td class="title2"><font face="Verdana">Seu amigo secreto e:</font></td></tr>
                                <tr><td> </td></tr>
                                <tr><td> </td></tr>
                                <tr><td> </td></tr>
                                <tr><td> </td></tr>
                                <tr><td> </td></tr>
                                <tr><td> </td></tr>
                                <tr><td class="nome"><font face="Comic sans MS"><b>"""+nome.upper()+"""</b></font></td></tr>
                                <tr><td> </td></tr>
                                <tr><td> </td></tr>
                                <tr><td> </td></tr>
                                <tr><td> </td></tr>
                                <tr><td> </td></tr>
                                <tr><td> </td></tr>
                                <tr><td class="title3"><font face="Arial"><b>Boa sorte! Nos vemos dia 19/12 as 20:00</b></font></td></tr>
                            </table>
                        </td></tr>
                    </table>
                </td></tr>
            </table>
    
        </body>
    
    </html>
    """ 
    return email_content

class SendEmail:
    
    @staticmethod
    def send(nome, enderecoEmail):
        msg = em.Message()
        msg['Subject'] = 'Amigo Secreto - IQ + ECA'
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(emailContent(nome))
        email = smtplib.SMTP('smtp.gmail.com', 587) 
        email.starttls() 
        email.login("amigosecretoiqeca@gmail.com", "4m1g0s3cr3t01q3c4")
        email.sendmail("amigosecretoiqeca@gmail.com", enderecoEmail, msg.as_string()) 
        email.quit()