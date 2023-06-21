import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class UserView extends JFrame {

    private String rules = "<html>Сложение - +<br>Вычитание - \"-\"<br>Умножение - *<br>Деление - /<br>Возведение в степень - ^<br>Отделение частей уравнения с помощью скобок - ()<html>";
    private Controller controller;
    private JButton calculateButton, saveButton, showHistoryButton;
    private JTextField expressionTextField;
    private JTextArea historyTextField;
    private JLabel resultLabel, rulesLabel, instructionsLabel;
    private JDialog historyDialog;
    private JScrollPane historyScrollPane;

    public UserView(Controller controller){
        this.controller = controller;
    }

    public void init(){

        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(null);
        setTitle("Калькулятор");
        setSize(600,540);
        setLocationRelativeTo(null);

        rulesLabel = new JLabel();
        add(rulesLabel);
        rulesLabel.setSize(400,200);
        rulesLabel.setLocation(100,20);
        rulesLabel.setText(rules);

        instructionsLabel = new JLabel();
        add(instructionsLabel);
        instructionsLabel.setSize(400,40);
        instructionsLabel.setLocation(100,230);
        instructionsLabel.setText("<html>Введите формулу либо название и путь файла для сохранения<br>истории вычислений<html>");

        expressionTextField = new JTextField();
        add(expressionTextField);
        expressionTextField.setSize(440,30);
        expressionTextField.setLocation(100,280);


        calculateButton = new JButton("Посчитать");
        add(calculateButton);
        calculateButton.setSize(440,30);
        calculateButton.setLocation(100,315);
        calculateButton.addActionListener(calculate ->{
            String expression = expressionTextField.getText();
            resultLabel.setText("Результат: ".concat(controller.calculate(expression)));
        });

        saveButton = new JButton("Сохранить историю");
        add(saveButton);
        saveButton.setSize(440,30);
        saveButton.setLocation(100,350);
        saveButton.addActionListener(save ->{
            String path = expressionTextField.getText();
            resultLabel.setText(controller.saveHistory(path));
        });

        showHistoryButton = new JButton("Показать историю вычислений");
        add(showHistoryButton);
        showHistoryButton.setSize(440,30);
        showHistoryButton.setLocation(100,385);
        showHistoryButton.addActionListener(showHistory ->{
            setSize(1200,540);

            historyTextField = new JTextArea();
            /*historyScrollPane = new JScrollPane(historyTextField);
            historyScrollPane.setVerticalScrollBarPolicy(ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS);
            getContentPane().add(historyScrollPane);*/
            add(historyTextField);

            historyTextField.setText(controller.getHistory());
            historyTextField.setSize(380,460);
            historyTextField.setLocation(600,20);
            /*revalidate();*/
        });

        resultLabel = new JLabel();
        add(resultLabel);
        resultLabel.setLocation(100,420);
        resultLabel.setSize(440,30);
        resultLabel.setText("");

        setVisible(true);
    }

}
