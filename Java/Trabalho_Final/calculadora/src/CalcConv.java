import javax.swing.*; //gráfico
import java.awt.*; //gráfico
import java.awt.event.ActionEvent; //para eventos cliques etc
import java.awt.event.ActionListener; //para ele ouvir

public class CalcConv extends JFrame{

    private JTextField valorTextField;
    private JComboBox<String> unidadeOrigeComboBox;
    private JComboBox<String> unidadeDestinoComboBox;
    private JLabel resultadoLabel;

    public CalcConv(){
        setTitle("Calculadora Conversão")
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(300,200);
        setLocationRelativeTo(null);

        JPanel painel = new JPanel(new GridLayout(4,2));

        JLabel valorLabel = new JLabel("Valor");
        valorTextField = new JTextField();

        JLabel unidOrigem = new JLabel("De: ");
        unidadeOrigeComboBox = new JComboBox<>(new String[]{"metros", "km"});

        JLabel unidDestino = new JLabel("para: ");
        unidadeDestinoComboBox = new JComboBox<>(new String[]{"metros", "km"});

        JButton converterButton = new JButton("Converter");
        converterButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed (ActionEvent e){
                converter();
            }
        });

        resultadoLabel = new JLabel("Resultado");

        painel.add(valorLabel);
        painel.add(valorTextField);
        painel.add(unidOrigem);
        painel.add(unidadeOrigeComboBox);
        painel.add(unidDestino);
        painel.add(unidadeDestinoComboBox);
        painel.add(converterButton);
        painel.add(resultadoLabel);

        add(painel);
        setVisible(true);


    }
}


