import httpx


class MakeScraper:
    
    def __init__(self):
        pass
    
    def ranking(self):
        """
        Global popularity ranking of the plugin as found in 
        https://www.make.com/en/integrations?community=1&verified=1
        """
        url = "https://www.make.com/en/integrations?community=1&verified=1"
        
        

        """        
        - Category: Categories (separated by a comma) where the plugin can be found (e.g., Google Sheet plugin found in "Productivity" https://www.make.com/en/integrations/category/productivity?community=1&verified=1)
        - Plugin Name: Name of the plugin
        - Plugin Description: Description of the plugin as found when clicking on it (ex: https://www.make.com/en/integrations/google-sheets)
        - Readme : Markdown version of the plugin documentation (e.g., https://www.make.com/en/help/app/google-sheets) -- You can find it in HTML and use an HTML to Markdown converter or use chatgpt
        - Type: Type of action (Action/Trigger/Search/etc.) (ex: https://www.make.com/en/integrations/google-sheets)
        -  Name: Name of the action found on the list of the plugin in make
        -  Description: High-level description of the action
        - Parameter : JSON of all the parameter of the action  as found in the documentation in the correct action (e.g., https://www.make.com/en/help/app/google-sheets#actions-964718)
        """