import page
from base.base import Base


class PageJiamingceshi(Base):

    def pagejiamingceshi_click_start_study(self):
        self.base_click_element(page.wsy_start_study)

    def pagejiamingceshi_click_ceshi(self):
        self.base_click_element(page.study_1_ceshi)

    def pagejiamingceshi_get_ans(self):
        self.base_get_question_answer(page.study1_question,page.study1_ans)

    def pagejiamingceshi_click_confirm(self):
        self.base_click_element(page.study1_confirm)

    def pagejiamingceshi_if_confirm_exist(self):
        return self.base_if_element_exist(page.study1_confirm)
