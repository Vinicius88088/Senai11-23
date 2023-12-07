import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

public class Arquivos {
    public static void main(String[] args) throws Exception {
        
        try{
        //Criando objeto do tipo arquivo
            File arquivo = new File("exemplo.txt");

        //Criar um objeto do tipo "escritor"
            FileWriter escritor = new FileWriter(arquivo);

        //Escrever no arquivo
            escritor.write("Esse é um arquivo de exemplo do Java");
        
        //Fechar o arquivo
            escritor.close();

            System.out.println("Dados foram gravados com sucesso!");
        } catch (IOException excessao) {
            System.out.println("Ocorreu um erro ao escrever o arquivo!");
        
        //Mostrar quando ocorre erro na execução
            excessao.printStackTrace();
        }
    }
}
