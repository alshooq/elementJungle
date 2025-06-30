from flask import Flask, jsonify, render_template

from typing import List, Dict, Callable
from types import ModuleType

from functools import wraps

from pathlib import Path

class Config:
    """
    Configuration class to set the views modules.
    """
    
    def __init__(self, application: Flask):
        """
        Initialize the Config class with a Flask application.

        This class contains all the views of the application.
        The views are imported and stored in a dictionary, with the key being the route and the value being the view function.

        :param application: The Flask application
        :type application: Flask
        """
        
        from .views import (
            home,
            about,
            nickel,
            palladium,
            platinum,
            darmstadtium,
            docs,
            data,
            nickelFamily,
        )
        
        self.app: Flask = application
        
        self.home: ModuleType = home
        self.about: ModuleType = about
        self.nickel: ModuleType = nickel
        self.palladium: ModuleType = palladium
        self.platinum: ModuleType = platinum
        self.darmstadtium: ModuleType = darmstadtium
        self.docs: ModuleType = docs
        self.data: ModuleType = data
        self.nickelFamily: ModuleType = nickelFamily
        
        self._views: Dict[int, ModuleType] = {
            0: self.home,
            1: self.about,
            2: self.nickel,
            3: self.palladium,
            4: self.platinum,
            5: self.darmstadtium,
            6: self.docs,
            7: self.data,
            8: self.nickelFamily,
        }
    
    def configViews(self, view: Callable, type_: str, local_: str, method_: List[str]):
        """
        Configure a view function to format its response based on the given type.
        
        If type_ is 'json', the function will return a JSON response using the jsonify() method.
        If type_ is 'html', the function will return an HTML response using the render_template() method.
        If type_ is invalid, the function will raise a ValueError.
        
        The given view function is wrapped with a wrapper function that formats the response according to the type.
        The wrapper function is then registered as a route with the given local_ and methods.
        
        :param view: The view function to be configured
        :type view: Callable
        :param type_: The type of response to be returned
        :type type_: str
        :param local_: The local path to be used for the route
        :type local_: str
        :param method_: The HTTP methods to be used for the route
        :type method_: List[str]
        :return: The wrapped view function
        :rtype: Callable
        """
        
        @wraps(view)
        def wrapper():
            """
            A wrapper function to format the response of the given view function based on the given type.
        
            If type_ is 'json', the function will return a JSON response using the jsonify() method.
            If type_ is 'html', the function will return an HTML response using the render_template() method.
            If type_ is invalid, the function will raise a ValueError.
            """
            
            if type_ == 'json':
                return jsonify(view())
        
            elif type_ == 'html':
                return render_template(view())
        
            else:
                raise ValueError("Invalid type specified. Use 'json' or 'html'.")
        
        self.app.route(local_, methods=method_)(wrapper)
        
        return wrapper
    
    @property
    def views(self) -> Dict[int, ModuleType]:
        """
        Returns a dictionary of all views modules.
        """
        
        return self._views
    
    @views.setter
    def views(self, value: Dict[int, ModuleType]):
        """
        Sets the views modules.
        """
        
        if not isinstance(value, dict):
            raise TypeError("Views must be a dictionary.")
        
        for key, view in value.items():
            if not isinstance(view, ModuleType) or not isinstance(key, int):
                raise TypeError(f"The value for {key} must be a module type and key must be an integer.")
        
        self._views = value
        

class TotalViews:
    """
    TotalViews class to manage all views in the application.
    """
    
    def __init__(self):
        """
        Initializes the TotalViews class.

        This class contains all the views of the application.
        The views are imported and stored in a dictionary, with the key being the route and the value being the view function.

        :ivar _totalViews: A dictionary of all views, with the key being the route and the value being the view function.
        :type _totalViews: Dict[int, Callable]
        """
        
        from .views.home.home import home
        from .views.about.about import about
        from .views.nickel.nickel import nickel
        from .views.palladium.palladium import palladium
        from .views.platinum.platinum import platinum
        from .views.darmstadtium.darmstadtium import darmstadtium
        from .views.docs.docs import docs
        from .views.data.data import data
        from .views.nickelFamily.nickelFamaily import nickelFamily

        
        self.home: Callable = home
        self.about: Callable = about
        self.nickel: Callable = nickel
        self.palladium: Callable = palladium
        self.platinum: Callable = platinum
        self.darmstadtium: Callable = darmstadtium
        self.docs: Callable = docs
        self.data: Callable = data
        self.nickelFamily: Callable = nickelFamily
        
        
        self._totalViews: Dict[int, Callable] = {
            
            0: self.home,
            1: self.about,
            2: self.nickel,
            3: self.palladium,
            4: self.platinum,
            5: self.darmstadtium,
            6: self.docs,
            7: self.data,
            8: self.nickelFamily,
            
        }
    
    @property
    def totalViews(self) -> Dict[int, Callable]:
        """
        Returns a dictionary of all views in the application.

        :return: A dictionary where keys are integers representing routes
             and values are callables for the respective view functions.
        :rtype: Dict[int, Callable]
        """

        return self._totalViews
    
    @totalViews.setter
    def totalViews(self, value: Dict[int, Callable]):
        """
        Sets the total views dictionary.

        :param value: The dictionary of views where keys are integers representing
            routes and values are callables for the respective view functions.
        :type value: Dict[int, Callable]
        :raises TypeError: If the value is not a dictionary or if the dictionary
            contains non-integer keys or non-callable values.
        """
        
        if not isinstance(value, dict):
            raise TypeError("totalViews must be a dictionary.")
        
        for key, view in value.items():
            if not callable(view) or not isinstance(key, int):
                raise TypeError(f"The value must respect the typing: Dict[int, Callable].")
        
        self._totalViews = value

class SetViews:
    """
    SetViews class to create and configure views in the application.
    This class initializes views based on the configuration provided in the Config class and the total views available in TotalViews.
    It iterates through the total views and applies the configuration for each view, allowing for dynamic view creation.
    """
    
    def __init__(self, config: Config, totalViews: TotalViews) -> None:
        """
        Initialize the SetViews class with a Config and TotalViews instance.
        """
        
        self.config: Config = config
        self.configuration: Dict[int, ModuleType] = config.views
        self.totalViews: Dict[int, Callable] = totalViews.totalViews
        
        self.createViews()
        
    def createViews(self, index: int = 0) -> None:
        """
        Create views based on the totalViews and configuration.
        """

        if index >= len(self.totalViews):
            return None
        
        self.makeViews(
            
            view=self.totalViews[index],
            type_=self.configuration[index].type_,
            local_=self.configuration[index].local_,
            method_=self.configuration[index].method_,
            
        )
        
        return self.createViews(index = index + 1)
        
    def makeViews(self, view: Callable, type_: str, local_: str, method_: List[str]):
        """
        Create a view with the specified parameters.
        """
        
        return self.config.configViews(view, type_, local_, method_)

class StreamToLogger:
    """
    A class that redirects stdout and stderr to a logger.
    Only meant to be used in a debugging/testing context.
    """
    
    def __init__(self, logger, log_level):
        """
        Initialize a StreamToLogger instance.

        :param logger: The logger to use for redirection of stdout and stderr.
        :type logger: logging.Logger
        :param log_level: The logging level to use for redirected output.
        :type log_level: int
        """
        
        self.logger = logger
        self.log_level = log_level

    def write(self, buf):
        """
        Write to the logger.

        :param buf: The string to write to the logger.
        :type buf: str
        """
        
        for line in buf.rstrip().splitlines():
            self.logger.log(self.log_level, line.rstrip())

    def flush(self):
        """
        Do nothing, as flushing is not needed for logging.
        """
        
        pass

class App:
    """
    Main application class to start the Flask app.
    """
    
    @staticmethod
    def create_app() -> Flask:
        """
        Create and configure the Flask application.
        """
        
        app = Flask(
            __name__, 
            template_folder = Path(__file__).parent / 'templates', 
            static_folder = Path(__file__).parent / 'static', 
            static_url_path='/',
        )
        
        return app
        
def start(debug: bool = False, use_reloader: bool = False) -> None:
    """
    Start the application with the given Flask app.
    """
    
    app: Flask = App.create_app()
    
    if debug:
        import logging
        import sys
        
        logging.basicConfig(
            level=logging.DEBUG, 
            format='%(asctime)s %(levelname)s %(name)s %(message)s'
        )
        
        sys.stdout = StreamToLogger(logging.getLogger("STDOUT"), logging.INFO)
        sys.stderr = StreamToLogger(logging.getLogger("STDERR"), logging.ERROR)
    
    config: Config = Config(app)
    totalViews: TotalViews = TotalViews()
    
    SetViews(config, totalViews)
    
    app.run(debug=debug, use_reloader=use_reloader, host='0.0.0.0', port=8080)

def start_app() -> Flask:
    """
    Start the application and return the Flask app instance.
    
    :return: The Flask app instance.
    :rtype: Flask
    """
    
    app: Flask = App.create_app()
    
    config: Config = Config(app)
    totalViews: TotalViews = TotalViews()
    
    SetViews(config, totalViews)
    
    return app

if __name__ == "__main__":
    """
    Main entry point to start the application.
    """
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        
        start(debug=True, use_reloader=True)
        
    else:
        
        start()
