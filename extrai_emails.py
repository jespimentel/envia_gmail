texto = input ("Entre com a string que contém os e-mails: ")
texto = texto.lower().split()
emails = []
for t in texto:
  if '@' in t:
    emails.append(t)
print ('Foram encontrados ', len(emails), 'e-mails na string')
print(emails)
print ('-----------------')

# Para uso com o script
for e in emails:
  print (e, end=' ')