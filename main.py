with open("./Input/Names/invited_names.txt", "r") as recipients:
    recipients_list = recipients.readlines()
    stripped_name = [recipient.strip() for recipient in recipients_list]


def create_new_mail(name):
    with open("./Input/Letters/starting_letter.txt", "r") as email_form:
        content_list = email_form.readlines()

        new_name_line = content_list[0].replace("[name]", name)

        new_lines = [new_name_line] + content_list[1:]
        write_mail = "".join(new_lines)
        return write_mail


def write_mail(name):
    with open(f"./Output/ReadyToSend/{name}.txt", "w") as file:
        new_mail = create_new_mail(name)
        file.write(new_mail)

    for recipient in recipients_list:
        write_mail(recipient)
