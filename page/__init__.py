from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

'''
—————————————————————————————————————————————————————————————
启动页面配置信息
_____________________________________________________________
'''
approve = By.ID, 'com.izaodao.gps:id/jurisdiction_cradtv5'
skip_user_desc = By.ID, 'com.izaodao.gps:id/tv_start1'

'''
—————————————————————————————————————————————————————————————
五十音页面配置信息
_____________________________________________________________
'''
wsy_tab = By.XPATH, '//android.widget.ImageView[@content-desc="五十音"]'
wsy_touxiang = By.ID, 'com.izaodao.gps:id/kana_img'
wsy_jiaming = By.ID, 'com.izaodao.gps:id/kana_tv'
wsy_zixuanfuxi = By.ID, 'com.izaodao.gps:id/home_tv_exam'
wsy_lianliankan = By.ID, 'com.izaodao.gps:id/home_tv_link'
wsy_ad = By.ID, 'com.izaodao.gps:id/img_ads'
'''
—————————————————————————————————————————————————————————————
开始学习页面配置信息
_____________________________________________________________
'''
wsy_start_study = By.ID, 'com.izaodao.gps:id/tvHomeStartLearning'

'''
—————————————————————————————————————————————————————————————
学习页面配置信息
_____________________________________________________________
'''
study_title1 = By.XPATH, "//	android.widget.TextView[@text = '清音阶段']"
study_title2 = By.XPATH, "//	android.widget.TextView[@text = '浊音阶段']"
study_title3 = By.XPATH, "//	android.widget.TextView[@text = '拗音阶段']"
study_title4 = By.XPATH, "//	android.widget.TextView[@text = '长音·促音·音调']"
study_1 = By.XPATH, "//android.widget.TextView[@text = 'あ']"
study_1_xuexi = By.XPATH, "//android.widget.TextView[@text = 'あ']/../../" \
                          "android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]"
study_1_ceshi = By.XPATH, "//android.widget.TextView[@text = 'あ']/../../" \
                          "android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout[2]"
study1_title = By.XPATH, "//android.widget.TextView[@text = '1/20']"
study1_question = By.ID, "com.izaodao.gps:id/tv_stem"
study1_ans = By.ID, "com.izaodao.gps:id/v_1"
study1_confirm = By.ID, 'com.izaodao.gps:id/tv_confirm'
study1_next = By.ID, 'com.izaodao.gps:id/tv_next'
study1_back = By.ID, 'com.izaodao.gps:id/defaultBackButton'
study1_back_confirm = By.ID, 'com.izaodao.gps:id/tv_negative'
study1_back_cancel = By.ID, 'com.izaodao.gps:id/tv_positive'
study1_share_report = By.ID, 'com.izaodao.gps:id/school_report_tv'
study1_score = By.ID, 'com.izaodao.gps:id/tv_questions_score'
study1_question_count = By.ID, 'com.izaodao.gps:id/tv_questions_count'
study1_time = By.ID, 'com.izaodao.gps:id/tv_questions_time'
studt1_report_back = By.ID, 'com.izaodao.gps:id/iv_back'
'''
—————————————————————————————————————————————————————————————
发现页面配置信息
_____________________________________________________________
'''
fx_banner = By.ID, 'com.izaodao.gps:id/tvDiscoveryToolbarTitle'
fx_daily_word = By.ID, 'com.izaodao.gps:id/tvDiscoveryHeaderDailyTitle'
fx_AI_study = By.ID, 'com.izaodao.gps:id/tvDiscoveryHeaderAiTitle'
'''
—————————————————————————————————————————————————————————————
跟老师学页面配置信息
列表元素定位需要考虑
_____________________________________________________________
'''
glsx_title = By.XPATH, "//android.widget.TextView[@text = '跟老师学']"
glsx_ljzaodao = By.ID, 'com.izaodao.gps:id/tv_understand'
glsx_banner = By.ID, 'com.izaodao.gps:id/img_banner'
glsx_sub_title = By.ID, 'com.izaodao.gps:id/tvDiscoveryTypeCoverTitle'
glsx_list_1 = By.XPATH, "//android.support.v7.widget.RecyclerView[@resource-id= 'com.izaodao.gps:id/rvDiscoveryTypeCoverContent']" \
                        "/android.widget.RelativeLayout[1]"
glsx_ad = By.ID, 'com.izaodao.gps:id/img_ads'
glsx_ad_close = By.ID, 'com.izaodao.gps:id/iv_close'

'''
—————————————————————————————————————————————————————————————
我的页面配置信息
_____________________________________________________________
'''
wd_tab = MobileBy.ACCESSIBILITY_ID, '我的'
wd_tab_hongdian = By.ID, 'com.izaodao.gps:id/iv_my_new'
wd_username = By.XPATH, '//android.widget.TextView[@text = "测试号9001"]'
wd_login = By.ID, 'com.izaodao.gps:id/tvMeUserName'
wd_touxiang = By.ID, 'com.izaodao.gps:id/ivMeAvatar'
wd_daily_task = By.ID, 'com.izaodao.gps:id/tv_daily_mask_text'
wd_daily_task_hongdian = By.ID, 'com.izaodao.gps:id/iv_daily_new'
wd_study_management = By.XPATH, "//android.widget.TextView[@text = '学习管理']"
wd_score_management = By.XPATH, "//android.widget.TextView[@text = '积分商城']"
wd_share_app = By.XPATH, "//android.widget.TextView[@text = '分享App给好友']"
wd_yijianfankui = By.XPATH, "//android.widget.TextView[@text = '意见反馈']"
wd_update_tiku = By.XPATH, "//android.widget.TextView[@text = '更新题库']"
wd_setting = By.ID, 'com.izaodao.gps:id/ivMeSetting'
wd_coin = By.ID, 'com.izaodao.gps:id/tvMeCoinCount'
'''
—————————————————————————————————————————————————————————————
设置页面配置信息
_____________________________________________________________
'''
setting_title = By.ID, 'com.izaodao.gps:id/defaultTitleView'
setting_person = By.ID, 'com.izaodao.gps:id/tvSettingProfile'
setting_notice = By.ID, 'com.izaodao.gps:id/tvSettingNotice'
setting_clear_cache = By.ID, 'com.izaodao.gps:id/clSettingClearCache'
setting_security = By.ID, 'com.izaodao.gps:id/tvSettingSecurity'
setting_about = By.ID, 'com.izaodao.gps:id/tvSettingAbout'
setting_logout = By.ID, 'com.izaodao.gps:id/tvSettingLogout'
setting_back = By.ID, 'com.izaodao.gps:id/defaultBackButton'
'''
—————————————————————————————————————————————————————————————
个人资料页面配置信息
_____________________________________________________________
'''
person_back = By.ID, 'com.izaodao.gps:id/defaultBackButton'
person_title = By.ID, 'com.izaodao.gps:id/defaultTitleView'
person_change_touxiang = By.ID, 'com.izaodao.gps:id/clProfileAvatar'
person_username = By.ID, 'com.izaodao.gps:id/clProfileName'
person_gender = By.ID, 'com.izaodao.gps:id/clProfileGender'
person_change_touxiang_camera = By.ID, 'com.izaodao.gps:id/tvImageSelectDialogCamera'
person_change_touxiang_album = By.ID, 'com.izaodao.gps:id/tvImageSelectDialogAlbum'
person_change_touxiang_cancel = By.ID, 'com.izaodao.gps:id/tvImageSelectDialogCancel'
person_gender_male = By.ID, 'com.izaodao.gps:id/tvImageSelectGenderMale'
person_gender_female = By.ID, 'com.izaodao.gps:id/tvImageSelectGenderFemale'
person_gender_cancel = By.ID, 'com.izaodao.gps:id/tvImageSelectGenderCancel'
person_username_clear = By.ID, 'com.izaodao.gps:id/ivNameEditClear'
person_username_input = By.ID, 'com.izaodao.gps:id/tvNameEditContent'
person_username_save = By.ID, 'com.izaodao.gps:id/tvNameEditCommit'
person_username_back = By.ID, 'com.izaodao.gps:id/defaultBackButton'
'''
—————————————————————————————————————————————————————————————
登录页面配置信息
_____________________________________________________________
'''
login_otherstyle = By.ID, 'com.izaodao.gps:id/authsdk_switch_view'
login_namepwd = By.XPATH, '//android.view.View[@content-desc="密码登录"]'
login_username = By.XPATH, '//android.widget.EditText[@text = "请输入您的手机/邮箱/用户名"]'
login_password = By.XPATH, '//android.widget.EditText[@text = "请输入密码"]'
login_submit = By.XPATH, '//android.view.View[@content-desc="确定"]'
