from selenium.webdriver.common.by import By


class Locators:

    def __init__(self):
        pass
# OKTA

    textbox_loginid = "idp-discovery-username"
    nextbutton = "idp-discovery-submit"
    textbox_loginps = "password-with-toggle"
    loginbutton = "input[class='button button-primary']"
    HELP_SIGNUP_LINK = "Need help signing in?"
    pushbutton = "//input[@value='Send Push']"

# end user portal for incident module

    SEARCH_TEXTBOX_MODULE_END_USER = (By.XPATH, "//input[@placeholder= 'Search the knowledge database and service catalogue']")
    INCIDENT_MODULE_OPTION = (By.XPATH, "//span[@class='highlight mark']")
    CALLER = (By.ID, "select2-chosen-11")
    CATEGORY = (By.XPATH, "//*[@id='s2id_sp_formfield_category']")
    CATEGORY_SEARCH_BOX = (By.ID, "s2id_autogen1_search")
    # CATEGORY_SEARCH_BOX = (By.ID, "s2id_autogen3_search")
    URGENCY = (By.ID, "s2id_sp_formfield_urgency")
    URGENCY_SEARCH_BOX = (By.ID, "s2id_autogen2_search")
    TEST = (By.ID, "twotabsearchtextbox")

    SUMMARY_TEXTBOX = (By.ID, "sp_formfield_short_description")
    CONTACT_PHONE_NUMBER_TEXTBOX = (By.ID, "sp_formfield_contact_number1")
    DESCRIPTION_TEXTBOX = (By.ID, "sp_formfield_description")
    SUBMIT_BTN = (By.XPATH, "//button[text() = 'Submit']")

# ITIL Agent portal for incident module

    LEFT_FILTER_SEARCH_BOX = (By.XPATH, "//input[@id='filter']")
    ITIL_ALL_APPS_TAB = (By.ID, "allApps_tab")
    ITIL_ALL_INCIDENTS = (By.ID, "concourse_module_b55b4ab0c0a80009007a9c0f03fb4da9")
    ITIL_GLOBAL_SEARCH_ICON = (By.XPATH, "//span[@class= 'input-group-addon-transparent icon-search sysparm-search-icon']")
    ITIL_GLOBAL_SEARCH_TEXT_BOX = (By.XPATH, "//input[@id='sysparm_search']")
    INCIDENT_ASSIGNMENT_GROUP = (By.ID, "sys_display.incident.assignment_group")
    ITIL_INCIDENT_ASIGNEE = (By.ID, "sys_display.incident.assigned_to")
    ITIL_INCIDENT_OFFICE = (By.XPATH, "//input[@id ='sys_display.incident.location']")
    ITIL_INCIDENT_CATEGORY =(By.ID, "incident.category")
    ITIL_INCIDENT_UPDATE_BTN = (By.ID, "sysverb_update")
    ITIL_INCIDENT_STATE =(By.ID, "incident.state")








