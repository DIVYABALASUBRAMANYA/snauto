""" Locators for all the pages """

from selenium.webdriver.common.by import By


class Locators:

    def __init__(self):
        pass
# OKTA

    USER_NAME_OKTA_TEXTBOX = (By.ID, "idp-discovery-username")
    NEXT_OKTA_BUTTON = (By.ID, "idp-discovery-submit")
    PASSWORD_OKTA_TEXTBOX = (By.XPATH, "//input[@type = 'password']")
    SUBMIT_OKTA_BUTTON = (By.XPATH, "//*[@class = 'button button-primary']")
    SEND_PUSH_OKTA_BUTTON = (By.XPATH, "//*[@class = 'button button-primary']")

# end user portal for incident module

    SEARCH_TEXTBOX_MODULE_END_USER = (By.XPATH, "//input[@placeholder= 'Search the knowledge database and service catalogue']")
    INCIDENT_MODULE_OPTION = (By.XPATH, "//a[@href='?id=sc_cat_item&sys_id=a085ba90db6ae7404a017cde3b9619e5']")
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

# End user portal for Workday europe support model

    WORK_DAY_EUROPE_SUPPORT_OPTION = (By.XPATH, "//span[@class ='highlight mark']")
    DESCRIPTION_WORKDAY_EUROPE_TEXTBOX = (By.ID, "sp_formfield_desc")
    ISSUE_ENQUIRY_WORKDAY_EUROPE_DROPDOWN = (By.XPATH, "//*[@id='s2id_sp_formfield_issue_inquiry']")
    ISSUE_ENQUIRY_WORKDAY_EUROPE_TEXTBOX = (By.XPATH, "//label[text() = 'Issue / Inquiry Area']/following-sibling::input")
    # CALLER_WORKDAY_EUROPE_DROPDOWN = (By.XPATH, "//*[@id='s2id_sp_formfield_caller_id']")
    SUBMIT_BUTTON_WORKDAY_EUROPE_BUTTON = (By.XPATH, "//*[@class='btn btn-primary btn-block ng-binding ng-scope']")


# End user portal for I Need something

    I_NEED_SOMETHING_CLICK = (By.XPATH, "//*[@class = 'ta-img ng-scope']")
    SUMMARY_REQUEST_TEXTBOX = (By.ID, "sp_formfield_short_description")
    CONTACT_NUMBER_REQUEST_TEXTBOX = (By.ID, "sp_formfield_contact_number1")
    DESCRIPTION_REQUEST_TEXTBOX = (By.ID, "sp_formfield_description")
    CATEGORY_REQUEST_DROPDOWN = (By.XPATH, "//*[@id ='s2id_sp_formfield_category']")
    CATEGORY_REQUEST_TEXTBOX =(By.ID, "s2id_autogen1_search")
    URGENCY_REQUEST_DROPDOWN = (By.XPATH, "//*[@id ='s2id_sp_formfield_urgency']")
    URGENCY_REQUEST_TEXTBOX = (By.XPATH, "//*[@id = 's2id_autogen2_search']")
    REQUESTED_FOR_REQUEST_DROPDOWN = (By.XPATH, "//*[@id ='s2id_sp_formfield_requested_for']")
    SUBMIT_REQUEST_BUTTON = (By.XPATH, "//*[@class ='btn btn-primary btn-block ng-binding ng-scope']")
    FETCH_REQUEST_NUMBER = (By.XPATH, "//b[@class ='ng-binding']")

# Product Platform Incident.

    PRODUCT_PLATFORM_INCIDENT_CLICK = (By.XPATH, "//*[@href='?id=sc_cat_item&sys_id=4ccde1a3dbc6ab007e5649ee3b961977']")
    PRODUCT_PRODUCT_PLATFORM = (By.ID, "s2id_sp_formfield_affected_website")
    PRODUCT_PRODUCT_PLATFORM_TEXTBOX = (By.ID, "s2id_autogen5_search")
    SUB_PRODUCT_PRODUCT_PLATFORM = (By.ID, "s2id_sp_formfield_sub_product")
    SUB_PRODUCT_PRODUCT_PLATFORM_TEXTBOX = (By.ID, "s2id_autogen7_search")
    URGENCY_PRODUCT_PLATOFORM = (By.ID, "s2id_sp_formfield_urgency")
    URGENCY_PRODUCT_PLATOFORM_SEARCH_BOX = (By.ID, "s2id_autogen1_search")
    INCIDENT_TYPE_PRODUCT_PLATFORM = (By.ID, "s2id_sp_formfield_please_specify_the_incident_type")
    INCIDENT_TYPE_PRODUCT_PLATFORM_TEXTBOX = (By.ID, "s2id_autogen2_search")
    DESCRIPTION_PRODUCT_PLATFORM_TEXTBOX = (By.ID, "sp_formfield_description")
    DEVICE_PRODUCT_PLATFORM_DROPDOWN = (By.ID, "s2id_sp_formfield_u_device")
    # DEVICE_PRODUCT_PLATFORM_TEXTBOX  = (By.CLASS_NAME, "select2-search-field")
    list= list((By.XPATH, "//li[@class = 'select2-search-field']//parent::ul//parent::div"))
    DEVICE_PRODUCT_PLATFORM_TEXTBOX = list[0]
    OPERATING_SYSTEM_PLATFORM = (By.ID, "s2id_sp_formfield_u_operating_system")
    OPERATING_SYSTEM_PLATFORM_TEXTBOX = (By.ID, "s2id_autogen346")
    BROWSER_PRODUCT_PLATFORM = (By.ID, "s2id_sp_formfield_u_browser")
    BROWSER_PRODUCT_PLATFORM_TEXTBOX = (By.ID, "s2id_autogen347")

    SUBMIT_PRODUCT_PLATFORM = (By.XPATH, "//*[@class ='btn btn-primary btn-block ng-binding ng-scope']")


# Password reset

    PASSWORD_RESET_MODULE_CLICK = (By.XPATH, "//a[@href='?id=sc_cat_item&sys_id=6d2a8290db9f23404a017cde3b9619c3']")
    APPLICATION_NAME_PASSWORD_REST_TEXTBOX = (By.ID, "sp_formfield_application")
    SUMMARY_PASSWORD_RESET_TEXTBOX = (By.ID, "sp_formfield_short_description")
    DESCRIPTION_PASSWORD_RESET_TEXTBOX = (By.ID, "sp_formfield_description")
    SUBMIT_PASSWORD_RESET_BUTTON = (By.XPATH, "//*[@class= 'btn btn-primary btn-block ng-binding ng-scope']")

# Ask a question

    ASK_A_QUESTION_CLICK = (By.XPATH, "//a[@href='?id=sc_cat_item&sys_id=a99df966db05f7804a017cde3b9619d8']")
    TITLE_ASK_A_QUESTION = (By.XPATH, "//h1[text()='Ask a Question']")
    SUMMARY_ASK_A_QUESTION_TEXTBOX = (By.ID, "sp_formfield_short_description")
    DESCRIPTION_ASK_A_QUESTION_TEXTBOX = (By.ID, "sp_formfield_description")
    SUBMIT_ASK_A_QUESTION_BUTTON = (By.XPATH, "//*[@class= 'btn btn-primary btn-block ng-binding ng-scope']")
    OFFICE_ASK_A_QUESTION_CLICK = (By.ID, "s2id_sp_formfield_location")
    OFFICE_ASK_A_QUESTION_TEXTBOX = (By.XPATH, '//label[text()="OfficeOffice"]/following-sibling::input')
    TEST = (By.XPATH, "//span[text()='Summary']")
    FULFILLMENT_ASK_A_QUESTION = (By.XPATH, "//*[text()=' Fulfillment ']")


# Access Module end user

    ACCESS_CLICK = (By.XPATH, "//a[@href='?id=sc_cat_item&sys_id=d9fd0d9cdb9b23404a017cde3b9619ed']")
    APPLICATION_REQUIRED_ACCESS_TEXTBOX = (By.ID, "sp_formfield_application_required")
    SUMMARY_ACCESS_TEXTBOX = (By.ID, "sp_formfield_short_description")
    DESCRIPTION_ACCESS_TEXTBOX = (By.ID, "sp_formfield_description")
    SUBMIT_ACCESS_BUTTON = (By.XPATH, "//button[text()= 'Submit']")


# Global support portal enhancement module

    GLOBAL_SUPPORT_PORTAL_CLICK = (By.XPATH, "//*[@href='?id=sc_cat_item&sys_id=493f02fddbfd73004a017cde3b961906']")
    URGENCY_GLOBAL_SUPPORT_PORTAL_ENHANCEMENT_DROPDOWN = (By.ID, "s2id_sp_formfield_urgency")
    URGENCY_GLOBAL_SUPPORT_PORTAL_ENHANCEMENT_TEXTBOX = (By.XPATH, "//label[text()='Urgency']/following-sibling::input")
    DATE_REQUIRED_TEXTBOX_GLOBAL_SUPPORT_PORTAL_ENHANCEMENT = (By.ID, "sp_formfield_due_date")
    SUMMARY_GLOBAL_SUPPORT_PORTAL_ENHANCEMENT_TEXTBOX = (By.ID, "sp_formfield_short_description")
    DESCRIPTION_GLOBAL_SUPPORT_PORTAL_ENHANCEMENT_TEXTBOX = (By.ID, "sp_formfield_description")
    SUBMIT_GLOBAL_GLOBAL_SUPPORT_PORTAL_ENHANCEMENT_BUTTON = (By.XPATH, "//*[text()='Submit']")
    ENHANCEMENT_TYPE_GLOBAL_SUPPORT_PORTAL_ENHANCEMENT_DROPDOWN = (By.ID, "s2id_sp_formfield_enhancement_type")
    ENHANCEMENT_TYPE_GLOBAL_SUPPORT_PORTAL_ENHANCEMENT_TEXTBOX = (By.XPATH, "//label[text()='Enhancement type']/following-sibling::input")


# Editorial system support

    EDITORIAL_SYSTEMS_CLICK = (By.XPATH, "//a[@href='?id=sc_cat_item&sys_id=58b33fa6db4637407e5649ee3b961990']")
    EDITORIAL_SYSTEMS_TITLE = (By.XPATH, "//h1[text() = 'Editorial Systems Incident']")
    OFFICE_EDITORIAL_SYSTEMS = (By.ID, "s2id_sp_formfield_location")
    OFFICE_EDITORIAL_SYSTEMS_TEXTBOX = (By.XPATH, "//label[text() = 'OfficeOffice']/following-sibling::input")
    AFFECTED_USER_EDITORIAL_SYSTEMS = (By.ID, "s2id_sp_formfield_u_affected_end_user")
    AFFECTED_USER_EDITORIAL_SYSTEMS_TEXTBOX = (By.XPATH, "//label[text() = 'Affected user']/following-sibling::input")
    URGENCY_EDITORIAL_SYSTEMS = (By.ID, "s2id_sp_formfield_urgency")
    URGENCY_EDITORIAL_SYSTEMS_TEXTBOX = (By.XPATH, "//label[text() = 'Urgency']/following-sibling::input")
    EDITORIAL_PLATFORM_EDITORIAL_SYSTEMS = (By.ID, "s2id_sp_formfield_cmdb_ci")
    EDITORIAL_PLATFORM_EDITORIAL_SYSTEMS_TEXTBOX = (By.XPATH, "//label[text() = 'Editorial PlatformEditorial Platform']/following-sibling::input")
    ISSUE_TYPE_EDITORIAL_SYSTEMS = (By.ID, "s2id_sp_formfield_issue_type")
    ISSUE_TYPE_EDITORIAL_SYSTEMS_TEXTBOX = (By.XPATH, "//label[text() = 'Issue type']/following-sibling::input")
    DEVICE_EDITORIAL_SYSTEMS = (By.ID, "s2id_sp_formfield_device")
    DEVICE_EDITORIAL_SYSTEMS_TEXTBOX = (By.XPATH, "//label[text() = 'Device']/following-sibling::input")
    OPERATING_SYSTEM_EDITORIAL_SYSTEMS = (By.ID, "s2id_sp_formfield_operating_system")
    OPERATING_SYSTEM_EDITORIAL_SYSTEMS_TEXTBOX = (By.XPATH, "//label[text() = 'Operating system']/following-sibling::input")
    BROWSER_EDITORIAL_SYSTEMS = (By.ID, "s2id_sp_formfield_browser")
    BROWSER_EDITORIAL_SYSTEMS_TEXTBOX = (By.XPATH, "//label[text() = 'Browser']/following-sibling::input")
    SUMMARY_EDITORIAL_SYSTEMS_TEXTBOX = (By.ID, "sp_formfield_short_description")
    DESCRIPTION_EDITORIAL_SYSTEMS_TEXTBOX = (By.ID, "sp_formfield_description")
    SUBMIT_BUTTON_EDITORIAL_SYSTEMS = (By.XPATH, "//button[text() = 'Submit']")
    START_EDITIORIAL_SYSTEMS_INCIDENT = (By.XPATH, "//span[text()='Start']")


# PRINTER ISSUE

    PRINTER_ISSUE_CLICK = (By.XPATH, "//*[@href='?id=sc_cat_item&sys_id=0fb93f4adbeb00507e5649ee3b961903']")
    OFFICE_PRINTER_ISSUE = (By.ID, "s2id_sp_formfield_location")
    OFFICE_PRINTER_ISSUE_TEXTBOX = (By.XPATH, "//label[text() = 'OfficeOffice']/following-sibling::input")
    PRINTER_ISSUE_PRINTER_ISSUE = (By.ID, "s2id_sp_formfield_subcategory")
    PRINTER_ISSUE_PRINTER_ISSUE_TEXTBOX = (By.XPATH, "//label[text() = 'Printer Issue']/following-sibling::input")
    PRINTER_ID_PRINTER_ISSUE = (By.ID, "s2id_sp_formfield_printer")
    PRINTER_ID_PRINTER_ISSUE_TEXTBOX = (By.XPATH, "//label[text() = 'Printer ID']/following-sibling::input")
    SUMMARY_PRINTER_ISSUE= (By.ID, "sp_formfield_short_description")
    DESCRIPTION_PRINTER_ISSUE = (By.ID, "sp_formfield_description")
    SUBMIT_BUTTON_PRINTER_ISSUE = (By.XPATH, "//button[text() = 'Submit']")


# Movers Request End User

    MMOVERS_REQUEST_CLICK = (By.XPATH, "//a[@href='?id=sc_cat_item&sys_id=c3f79c19dba640904a017cde3b961904']")
    CURRENT_LOCATION_MOVER_REQUEST = (By.ID, "s2id_sp_formfield_location")
    CURRENT_LOCATION_MOVER_REQUEST_TEXTBOX = (By.XPATH, "//label[text()='Current LocationCurrent Location']/following-sibling::input")
    CURRENT_DESK_POSITION_MOVER_REQUEST_TEXTBOX = (By.ID, "sp_formfield_please_provide_the_current_desk_floor_location_for_this_person")
    LOCATION_PERSON_IS_MOVING_MOVER_REQUEST = (By.ID, "s2id_sp_formfield_location_the_person_is_moving")
    LOCATION_PERSON_IS_MOVING_MOVER_REQUEST_TEXTBOX_MOVERS_REQUEST = (By.XPATH, "//label[text()='Please select the location the person is moving to:Please select the location the person is moving to:']/following-sibling::input")
    DESK_FLOOR_LOCATION_THE_PERSON_IS_MOVING_TO_MOVERS_REQUEST = (By.ID, "sp_formfield_please_provide_the_desk_floor_location_this_person_is_moving_to")
    SUBMIT_MOVERS_REQUEST = (By.XPATH, "//button[text()='Submit']")

# DAM Enhancement Request

    DAM_ENHANCEMENT_REQUEST_CLICK = (By.XPATH, "//*[@href='?id=sc_cat_item&sys_id=dcd73b6edb4637407e5649ee3b961940']")
    OFFICE_DAM_ENHANCEMENT_REQUEST = (By.ID, "s2id_sp_formfield_location")
    OFFICE_DAM_ENHANCEMENT_REQUEST_TEXTBOX = (By.XPATH, "//label[text() = 'OfficeOffice']/following-sibling::input")
    URGENCY_DAM_ENHANCEMENT_REQUEST = (By.ID, "s2id_sp_formfield_urgency")
    URGENCY_DAM_ENHANCEMENT_REQUEST_TEXTBOX = (By.XPATH, "//label[text() = 'Urgency']/following-sibling::input")
    DAM_PLATFORM_DAM_ENHANCEMENT_REQUEST = (By.ID, "s2id_sp_formfield_cmdb_ci")
    DAM_PLATFORM_DAM_ENHANCEMENT_REQUEST_TEXTBOX = (By.XPATH, "//label[text() = 'DAM platformDAM platform']/following-sibling::input")
    EDITORIAL_ROLE_DAM_ENHANCEMENT_REQUEST = (By.ID, "s2id_sp_formfield_editorial_role")
    EDITORIAL_ROLE_DAM_ENHANCEMENT_REQUEST_TEXTBOX = (By.XPATH, "//label[text() = 'Editorial role']/following-sibling::input")
    BRAND_DAM_ENHANCEMENT_REQUEST = (By.ID, "s2id_sp_formfield_brand")
    BRAND_DAM_ENHANCEMENT_REQUEST_TEXTBOX = (By.XPATH ,"//label[text() = 'Brand']/following-sibling::input")
    SUMMARY_DAM_ENHANCEMENT_REQUEST_TEXTBOX = (By.ID, "sp_formfield_short_description")
    BUSINESS_JUSTIFICATION_DAM_ENHANCEMENT_REQUEST_TEXTBOX = (By.ID, "sp_formfield_business_justification")
    USE_CASE_DAM_ENHANCEMENT_REQUEST_TEXTBOX = (By.ID, "sp_formfield_description")
    SUBMIT_DAM_ENHANCEMENT_REQUEST_TEXTBOX = (By.XPATH, "//*[text() = 'Submit']")

# TERMINATION REQUEST

    TERMINATION_REQUEST_CLICK = (By.XPATH, "//a[@href='?id=sc_cat_item&sys_id=6643285adb40c0507e5649ee3b9619ff']")
    MANAGER_TERMINATION_REQUEST = (By.ID ,"s2id_sp_formfield_manager")
    MANAGER_TERMINATION_REQUEST_TEXTBOX = (By.XPATH, "//label[text() = 'ManagerManager']/following-sibling::input")
    EMPLOYEE_NAME_TERMINATION_REQUEST = (By.ID, "s2id_sp_formfield_employee_name")
    EMPLOYEE_NAME_TERMINATION_REQUEST_TEXTBOX = (By.XPATH, "//label[text() = 'Employee nameEmployee name']/following-sibling::input")
    TERMINATION_DATE_TERMINATION_REQUEST = (By.ID, "sp_formfield_termination_date")
    ADDITIONAL_INFORMATION_TERMINATION_REQUEST = (By.ID, "sp_formfield_additional_information")
    SUBMIT_TERMINATION_REQUEST = (By.XPATH , "//*[text() = 'Submit']")


# Create Cloud Instance

    OFFICE_CREATE_CLOUD_INSTANCE = (By.ID, "s2id_sp_formfield_location")
    OFFICE_CREATE_CLOUD_INSTANCE_TEXTBOX = (By.XPATH, "//label[text() = 'OfficeOffice']/following-sibling::input")
    URGENCY_CREATE_CLOUD_INSTANCE = (By.ID, "s2id_sp_formfield_urgency")
    URGENCY_CREATE_CLOUD_INSTANCE_TEXTBOX = (By.XPATH, "//label[text() = 'Urgency']/following-sibling::input")
    DATE_REQUIRED_CLOUD_INSTANCE_TEXTBOX = (By.XPATH, "sp_formfield_date_required")
    INSTANCE_TYPE_CLOUD_INSTANCE = (By.ID, "s2id_sp_formfield_instance_type")
    INSTANCE_TYPE_CLOUD_INSTANCE_TEXTBOX = (By.XPATH, "//label[text() = 'Instance type']/following-sibling::input")


# AV Break Fix ticket

    CATEGORY_AV_BREAK_FIX_TICKET = (By.ID, "s2id_sp_formfield_category")
    CATEGORY_AV_BREAK_FIX_TICKET_TEXTBOX  = (By.XPATH, "//label[text() = 'Category']/following-sibling::input")
    LOCATION_AV_BREAK_FIX_TICKET = (By.ID, "sp_formfield_location")
    URGENCY_AV_BREAK_FIX_TICKET = (By.ID, "s2id_sp_formfield_urgency")
    URGENCY_AV_BREAK_FIX_TICKET_TEXTBOX = (By.XPATH , "//label[text() = 'Urgency']/following-sibling::input")
    SUMMARY_AV_BREAK_FIX_TICKET = (By.ID, "sp_formfield_short_description")
    DESCRIPTION_AV_BREAK_FIX_TICKET = (By.ID, "sp_formfield_description")
    SUBMIT_AV_BREAK_FIX_TICKET = (By.XPATH, "//*[text() = 'Submit']")


# DATABSE TASKS

# VERSO FEATURE REQUEST

    VERSO_FEATURE_REQUEST_CLICK = (By.XPATH, "//a[@href='?id=sc_cat_item&sys_id=d7ca3698db7568101f8fb4c4f396191e']")
    URGENCY_VERSO_FEATURE_REQUEST = (By.ID, "s2id_sp_formfield_urgency")
    URGENCY_VERSO_FEATURE_REQUEST_TEXTBOX = (By.XPATH, "//label[text() = 'Urgency']/following-sibling::input")
    BRAND_VERSO_FEATURE_REQUEST = (By.ID, "sp_formfield_reference_brand")
    BRAND_VERSO_FEATURE_REQUEST_TEXTBOX = (By.XPATH, "//label[text() = 'BrandBrand']/following-sibling::input")
    PAGE_VERSO_FEATURE_REQUEST_TEXTBOX =(By.ID, "sp_formfield_website")
    UNLOCK_VERSO_FEATURE_REQUEST_BUTTON = (By.XPATH, "//span[@class= 'fa fa-lock']")
    LOCK_VERSO_FEATURE_REQUEST_BUTTON = (By.XPATH, "//span[@class= 'fa fa-unlock']")
    DESCRIPTION_VERSO_FEATURE_REQUEST_TEXTBOX = (By.ID, "sp_formfield_description")
    JUSTIFICATION_VERSO_FEATURE_REQUEST_TEXTBOX = (By.ID, "sp_formfield_justification")
    SUBMIT_VERSO_FEATURE_REQUEST= (By.XPATH, "//*[text() = 'Submit']")


# IP INFRINGEMENT OR IMPERSONATION

    IP_INFRIGMENT_CLICK= (By.XPATH, "//*[@href='?id=sc_cat_item&sys_id=26e20b9cdbd224101f8fb4c4f396198c']")
    CATEGORY_IP_INFRINGEMENT_OR_IMPERSONATION = (By.ID, "s2id_sp_formfield_category")
    CATEGORY_IP_INFRINGEMENT_OR_IMPERSONATION_TEXTBOX = (By.XPATH, "//label[text() = 'Category']/following-sibling::input")
    SUMMARY_IP_INFRINGEMENT_OR_IMPERSONATION_TEXTBOX = (By.ID, "sp_formfield_short_description")
    DESCRIPTION_IP_INFRINGEMENT_OR_IMPERSONATION_TEXTBOX = (By.ID, "sp_formfield_description")
    SUBMIT_IP_INFRINGEMENT_OR_IMPERSONATION_BUTTON = (By.XPATH, "//*[text() = 'Submit']")

# PEN DRIVE

    PEN_DRIVE_CLICK = (By.XPATH, "//a[@href='?id=sc_cat_item&sys_id=8ed15b89dbb004904a017cde3b9619f7']")
    OFFICE_PEN_DRIVE = (By.ID, "s2id_sp_formfield_location")
    OFFICE_PEN_DRIVE_TEXTBOX = (By.XPATH, "//label[text() = 'OfficeOffice']/following-sibling::input")
    SUMMARY_PEN_DRIVE = (By.ID, "sp_formfield_short_description")
    INTENDED_USE_OF_EQUIPMENT_PEN_DRIVE = (By.ID, "sp_formfield_description")
    DATE_REQUIRED_PEN_DRIVE = (By.ID, "sp_formfield_date_required3")
    SUBMIT_PEN_DRIVE = (By.XPATH, "//*[text() = 'Submit']")

# USB PEN DRIVE

    USB_PEN_DRIVE_CLICK = (By.XPATH, "//a[@href='?id=sc_cat_item&sys_id=96053b1bdbd57bc04a017cde3b9619f4']")
    OFFICE_USB_PEN_DRIVE = (By.ID, "s2id_sp_formfield_location")
    OFFICE_USB_PEN_DRIVE_TEXTBOX = (By.XPATH, "//label[text() = 'OfficeOffice']/following-sibling::input")
    SUMMARY_USB_PEN_DRIVE = (By.ID, "sp_formfield_short_description")
    INTENDED_USE_OF_EQUIPMENT_USB_PEN_DRIVE = (By.ID, "sp_formfield_description")
    DATE_REQUIRED_USB_PEN_DRIVE = (By.ID, "sp_formfield_date_required2")
    SUBMIT_USB_PEN_DRIVE = (By.XPATH, "//*[text() = 'Submit']")

# REPORT ISSUE

    REPORT_ISSUE_CLICK = (By.XPATH, "//a[@href='?id=sc_cat_item&sys_id=7cc4e3585b120010e394e96d7981c785']")
    BRIEF_DESCRIPTION_REPORT_ISSUE_TEXTBOX = (By.ID, "sp_formfield_short_description")
    DETAILED_DESCRIPTION_REPORT_ISSUE_TEXTBOX = (By.ID, "sp_formfield_description")
    POSSIBLE_SUGGESTIONS_REPORT_ISSUE_TEXTBOX = (By.ID, "sp_formfield_recommendation")
    # ENTITY_ISSUE_REPORT_ISSUE = (By.ID, "")
    SUBMIT_REPORT_ISSUE_BUTTON = (By.XPATH, "//*[text() = 'Submit']")






