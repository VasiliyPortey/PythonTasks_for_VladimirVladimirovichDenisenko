public class Controller {

    private CalculatorModel calculatorModel;
    private FileManager fileManager;

    public Controller(CalculatorModel calculatorModel, FileManager fileManager){

        this.calculatorModel = calculatorModel;
        this.fileManager = fileManager;
    }
    public String calculate(String expression){
        String result;
        try {
            result = String.valueOf(calculatorModel.calculate(expression));
        }
        catch (Exception e){
            return "Формула введена некорректно!";
        }
        fileManager.updateHistory(expression, result);
        return result;
    }

    public String saveHistory(String path){
        try {
            return fileManager.saveHistoryFile(path);
        }
        catch (Exception e){
            return "Формула введена некорректно!";
        }
    }

    public String getHistory(){
        return fileManager.getHistory();
    }
}
