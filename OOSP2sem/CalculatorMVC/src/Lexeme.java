public class Lexeme {
    CalculatorModel.LexemeType type;
    String value;

    public Lexeme(CalculatorModel.LexemeType type, String value) {
        this.type = type;
        this.value = value;
    }

    public Lexeme(CalculatorModel.LexemeType type, Character value) {
        this.type = type;
        this.value = value.toString();
    }

    @Override
    public String toString() {
        return "Lexeme{" +
                "type=" + type +
                ", value='" + value + '\'' +
                '}';
    }
}
