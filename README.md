# envia_gmail
Envia e-mails pela conta do Gmail

O presente programa foi criado para a campanha do Conselho Superior do MPSP, biênio 2022-2023, para atender à chapa "Legitimidade e Compromisso dom o MP".

O script "extrai_emails.py" recebe a relação de nomes e cargos de uma determinada Regional e lista os e-mails encontrados no texto.

O script "envia_email.py" envia e-mails individualizados para cada colega, usando o serviço GMail, para convidá-lo para a reunião de campanha.

As informações de usuário e senha devem ser colocadas no arquivo "secreto.py", da seguinte forma:


usuario = 'xxxxxx@gmail.com'

senha = 'xxxxxx'
