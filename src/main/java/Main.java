import jep.SharedInterpreter;
import java.io.File;

public class Main {

    /**
     * The main entry point of the application.
     * <p>
     * Initializes the shared interpreter, configures the classpath,
     * and starts the Flask application.
     *
     * @param args Command-line arguments passed to the program.
     * @throws Exception if an error occurs during initialization or execution.
     */
    public static void main(String[] args) throws Exception {

        // Initialize the shared interpreter
        SharedInterpreter interp = initInterpreter();

        // Configure the classpath for the interpreter
        configClassPath(interp);

        // Start the Flask application
        startFlaskApp(interp);
        
    }

    /**
     * Initializes the shared interpreter, but does not configure the classpath.
     * <p>
     * If an error occurs during initialization, the error is caught and re-thrown
     * with a message indicating that the error occurred while executing the
     * Flask application.
     *
     * @return the initialized shared interpreter
     * @throws Exception if an error occurs during initialization
     */
    public static SharedInterpreter initInterpreter() throws Exception {

        // Try to create a new instance of SharedInterpreter;
        // If successful, return the interpreter instance;
        // If an error occurs, catch it and print an error message;

        try {

            SharedInterpreter interp = new SharedInterpreter();

            return interp;

        } catch (Exception e) {

            System.err.println("Error while executing flask application: " + e.getMessage());
            throw e;

        }

    }

    /**
     * Configures the class path for the provided shared interpreter.
     * <p>
     * This method appends the current directory (".") to the Python interpreter's
     * system path, allowing the interpreter to import modules from the current
     * directory.
     *
     * @param interp the shared interpreter whose class path is to be configured
     * @throws Exception if an error occurs while modifying the system path
     */

    public static void configClassPath(SharedInterpreter interp) throws Exception {

        // Try to append the current directory to the Python interpreter's system path;
        // If successful, the interpreter will be able to import modules from the current directory;
        // If an error occurs, catch it and print an error message

        try {

            String appPath = new File(".").getAbsolutePath();
            interp.eval("import sys");
            interp.eval("sys.path.append(r'" + appPath.replace("\\", "\\\\") + "')");
        
        } catch (Exception e) {

            System.err.println("Error while configuring class path: " + e.getMessage());
            throw e;

        }

    }

    /**
     * Starts the Flask application by calling the {@code start()} method of the
     * {@code flask_app} module.
     * <p>
     * This method is the entry point of the Flask application and is responsible for
     * starting the Flask development server.
     *
     * @param interp the shared interpreter to execute the flask application
     * @throws Exception if an error occurs while executing the flask application
     */
    public static void startFlaskApp(SharedInterpreter interp) throws Exception {

        // Try to import the flask_app module and call its start() method;
        // If successful, the Flask application will start;
        // If an error occurs, catch it and print an error message

        try {

            interp.eval("from app import main");
            interp.eval("main.start()");

        } catch (Exception e) {

            System.err.println("Error while executing flask application: " + e.getMessage());
            throw e;

        }
        
    }

}