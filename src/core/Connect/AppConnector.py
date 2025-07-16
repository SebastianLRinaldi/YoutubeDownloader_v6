from src.apps.Basic.Functions import Logic as BasicLogic  
from src.apps.Web.Functions import Logic as WebLogic      
from src.apps.Second.Functions import Logic as SecondLogic
from src.apps.app0.Functions import Logic as App0Logic    

from src.apps.Basic.Layout import Layout as BasicLayout   
from src.apps.Web.Layout import Layout as WebLayout       
from src.apps.Second.Layout import Layout as SecondLayout 
from src.apps.app0.Layout import Layout as App0Layout     



class AppConnector:
    basic_logic: BasicLogic
    web_logic: WebLogic
    second_logic: SecondLogic
    app0_logic: App0Logic

    basic_ui: BasicLayout
    web_ui: WebLayout
    second_ui: SecondLayout
    app0_ui: App0Layout

    def __init__(self, apps: dict, logic: dict):
        self.apps = apps
        self.logic = logic

        self.init_connections()
        self.basic_ui.btn1.clicked.connect(self.second_logic.somefunction)

    """
    This basically just does this part for us:
    
    class AppConnector:
        basic_ui: BasicLayout
        second_logic: SecondLogic

        def __init__(self, apps, logic):
            self.basic_ui = apps["Basic"]
            self.second_logic = logic["Second"]

            self.basic_ui.btn1.clicked.connect(self.second_logic.somefunction)
    """
    def init_connections(self):
        for name in self.apps:
            setattr(self, f"{name.lower()}_ui", self.apps[name])
            setattr(self, f"{name.lower()}_logic", self.logic[name])








# class AppConnector:
#     basic_logic: BasicLogic
#     second_logic:SecondLogic
#     web_logic: WebLogic

#     basic_ui: BasicLayout
#     second_logic:SecondLayout
#     web_logic: WebLayout
    
#     def __init__(self, ):



#         self.basic_ui.btn1.clicked.connect(self.second_logic.somefunction)

#         self.logic["Basic"].ui.update_widget_btn.clicked.connect(
#             self.logic["Second"].update_widget
#         )

#         # self.logic["Basic"].ui.reset_widget_btn.clicked.connect(
#         #     lambda: self.logic["Second"].ui.name_label.setText("Updated Another Way")
#         # )
        