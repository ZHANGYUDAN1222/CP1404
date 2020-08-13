def get_emails():
    emails=[]
    while True:
        email=input('Email:')
        if email=='':
            break
        else:
            emails.append(email)
    return emails

def get_name_from_emails(emails):
    email_name={}
    for email in emails:
        name=email.replace('.',' ').split('@')[0].title()
        email_name[email]=name
    return email_name

def change_name(email_name):
    for k,v in email_name.items():
        answer=input('''Email:%s
Is your name %s?(Y/N)'''%(k,v)).upper()
        if answer=='Y' or answer=='':
            pass
        else:
            name=input('Name:')
            email_name[k]=name
    return email_name

def main():
    emails=get_emails()
    email_name=get_name_from_emails(emails)
    email_name=change_name(email_name)
    for k,v in email_name.items():
        print('''Email:
%s(%s)'''%(v,k))

if __name__=="__main__":
    main()