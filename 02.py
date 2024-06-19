
class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone):
        if all([name, phone.isdigit(), len(phone) == 12, name not in [contact['name'] for contact in self.contacts], phone not in [contact['phone'] for contact in self.contacts]]):
            self.contacts.append({'name': name, 'phone': phone})
            return True
        else:
            return False

    def remove_contact(self, name):
        self.contacts = [contact for contact in self.contacts if contact['name'] != name]

    def clear_contacts(self):
        self.contacts = []

# Пример использования
contact_manager = ContactManager()
contact_manager.add_contact("Татьяна", "380501112233")
contact_manager.add_contact("Роман", "380664445566")
contact_manager.remove_contact("Татьяна")
contact_manager.clear_contacts()




