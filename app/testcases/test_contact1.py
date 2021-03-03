from app.page.app import App
from app.page.base_page import BasePage


class TestContact:
    def setup(self):
        self.app = App()
        self.main = self.app.start().main()

    def test_contact(self):
        invitepage = self.main.goto_addresslist().add_member()\
            .addmember_by_mamul().input_name()\
            .set_phonenum().click_save()
        assert  '成功' in invitepage.get_toast()

