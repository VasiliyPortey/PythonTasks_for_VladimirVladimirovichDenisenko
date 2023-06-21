public class Main {
    public static void main(String[] args) throws Exception {
        CalculatorModel calculatorModel = new CalculatorModel();
        FileManager fileManager = new FileManager();
        Controller controller = new Controller(calculatorModel, fileManager);
        UserView userView = new UserView(controller);
        userView.init();
    }
}