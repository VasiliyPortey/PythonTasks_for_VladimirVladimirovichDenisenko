import java.io.*;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.Files;


public class FileManager {

    private File historyFile;
    private File userHistoryFile;
    private FileWriter writer;
    private Path defaultHistoryPath;
    public FileManager() {
        historyFile = new File("history.txt");
        /*defaultHistoryPath = Path.of("history.txt");*/
        try {
            if(!historyFile.exists())
                historyFile.createNewFile();
        } catch (IOException e) {
            System.out.println("Возникла какая-то ошибка при работе с файлом 'history.txt'");
            e.printStackTrace();
        }
    }

    public void updateHistory(String formula, String result){
        try{
            writer = new FileWriter(historyFile, true);
            writer.append(formula.concat(" = ").concat(result).concat("\n"));
            writer.flush();
            writer.close();
        }
        catch (IOException e){
            System.out.println("Возникла какая-то ошибка при работе с файлом 'history.txt'");
        }
    }

    public String saveHistoryFile(String path){
        if (path.equals(""))
            return "<html>Текущий путь к файлу с историей:<br><html>".concat(defaultHistoryPath.toAbsolutePath().toString());
        /*Path historyPath = Path.of(path);
        if(!historyPath.isAbsolute()|!historyPath.startsWith(path))
            return "Некорректно введён путь/расширение файла!";*/
        userHistoryFile = new File(path);
        try {
            writer = new FileWriter(userHistoryFile);
            if (userHistoryFile.isDirectory()) {
                userHistoryFile = new File(path, "log.log");
                userHistoryFile.createNewFile();
            }
            else
                userHistoryFile.createNewFile();
            try(FileInputStream fin=new FileInputStream(historyFile)){
                String history = "";
                int i;
                while((i=fin.read())!=-1)
                    history.concat(String.valueOf(i));
                writer.append(history);
                writer.flush();
            }
            catch (IOException e){
                return "Возникла какая-то ошибка при работе с файлом 'history.txt'";
            }
            return "Файл успешно сохранён!";
        } catch (IOException e) {
            e.printStackTrace();
            return "Некорректно введён путь/расширение файла!";
        }
    }

    public String getHistory(){
        try(FileInputStream fin=new FileInputStream("history.txt")){
            String history = "";
            int i;
            while((i=fin.read())!=-1)
                /*history.concat(String.valueOf(i));*/
                history+=(char)i;
            /*history = history.replaceAll("\n","<br>");
            history = history.concat("<html>");*/
            return history;
        }
        catch (IOException e){
            return "Возникла какая-то ошибка при работе с файлом 'history.txt'";
        }
    }
}
