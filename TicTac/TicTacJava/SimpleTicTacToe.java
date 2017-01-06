import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class SimpleTicTacToe implements ActionListener {

    private static JFrame frame;
    private static JPanel contentPane;
    private static JLabel lblEnterFirstPlayerName, lblEnterSecondPlayerName, lblFirstPlayerScore, lblSecondPlayerScore;
    private static JButton btnClearBoard, btnClearAll, btnCloseGame;
    private static JButton[] buttons = new JButton[9];
    private static JTextField txtEnterFirstPlayerName, txtEnterSecondPlayerName;

    private Font buttonFont = new Font("Arial", Font.PLAIN, 20);

    private static int width = 600;
    private static int length = 400;
    private static int firstPlayerScore = 0;
    private static int secondPlayerScore = 0;
    private static int playerTurn = 1;
    private static int roundComplete = 0;


    private SimpleTicTacToe(){

        frame = new JFrame("Tic Tac Toe by Darkling");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        contentPane = new JPanel();
        contentPane.setLayout(new GridLayout(6, 3, 10, 10));
        contentPane.setBorder(BorderFactory.createEmptyBorder(20, 20, 20, 20));

        for (int i = 0, n = buttons.length; i < n; i++) {
            buttons[i] = new JButton("");
            buttons[i].setFont(buttonFont);
            buttons[i].setAlignmentX(JButton.CENTER_ALIGNMENT);
            String temp = "CLICK0" + (i + 1);
            buttons[i].setActionCommand(temp);
            buttons[i].addActionListener(this);
            contentPane.add(buttons[i]);
        }

        lblEnterFirstPlayerName = new JLabel("Enter First Player's Name");
        contentPane.add(lblEnterFirstPlayerName);

        txtEnterFirstPlayerName = new JTextField("");
        contentPane.add(txtEnterFirstPlayerName);

        lblFirstPlayerScore = new JLabel("Score: " + firstPlayerScore);
        contentPane.add(lblFirstPlayerScore);

        lblEnterSecondPlayerName = new JLabel("Enter Second Player's Name");
        contentPane.add(lblEnterSecondPlayerName);

        txtEnterSecondPlayerName = new JTextField("");
        contentPane.add(txtEnterSecondPlayerName);

        lblSecondPlayerScore = new JLabel("Score: " + secondPlayerScore);
        contentPane.add(lblSecondPlayerScore);

        btnClearBoard = new JButton("Clear Board");
        btnClearBoard.setAlignmentX(JButton.CENTER_ALIGNMENT);
        btnClearBoard.setActionCommand("CLICKClearBoard");
        btnClearBoard.addActionListener(this);
        contentPane.add(btnClearBoard);

        btnClearAll = new JButton("Clear All");
        btnClearAll.setAlignmentX(JButton.CENTER_ALIGNMENT);
        btnClearAll.setActionCommand("CLICKClearAll");
        btnClearAll.addActionListener(this);
        contentPane.add(btnClearAll);

        btnCloseGame = new JButton("Close Game");
        btnCloseGame.setAlignmentX(JButton.CENTER_ALIGNMENT);
        btnCloseGame.setActionCommand("CLICKCloseGame");
        btnCloseGame.addActionListener(this);
        contentPane.add(btnCloseGame);

        frame.setContentPane(contentPane);
        frame.pack();
        frame.setSize(width,length);
        frame.setVisible(true);

    }

    public void actionPerformed(ActionEvent event) {
        String eventName = event.getActionCommand();

        if (eventName.startsWith("CLICK0")) {
            for (int i = 0, n = buttons.length; i < n; i++) {
                if (eventName.endsWith("" + (i + 1))) {
                    if (buttons[i].isEnabled()) {
                        switch (playerTurn) {
                            case 1:
                                buttons[i].setText("X");
                                playerTurn = 2;
                                buttons[i].setEnabled(false);
                                break;
                            case 2:
                                buttons[i].setText("O");
                                playerTurn = 1;
                                buttons[i].setEnabled(false);
                                break;
                            default:
                                break;
                        }
                    }
                }
            }
        } else if (eventName.contains("Clear")) {

            for (int i = 0, n = buttons.length; i < n; i++) {
                buttons[i].setText("");
                buttons[i].setEnabled(true);
            }

            playerTurn = 1;

            roundComplete = 0;

            if (eventName.endsWith("All")) {
                firstPlayerScore = 0;
                lblFirstPlayerScore.setText("Score: " + firstPlayerScore);
                secondPlayerScore = 0;
                lblSecondPlayerScore.setText("Score: " + secondPlayerScore);

                txtEnterFirstPlayerName.setText("");
                txtEnterSecondPlayerName.setText("");
            }

        } else if (eventName.endsWith("Game")) {
            System.exit(0);
        }

        score();
    }

    private static void switcherXO(String XO) {
        switch (XO) {
            case "X":
                firstPlayerScore += 1;
                lblFirstPlayerScore.setText("Score: " + firstPlayerScore);
                roundComplete = 1;
                break;
            case "O":
                secondPlayerScore += 1;
                lblSecondPlayerScore.setText("Score: " + secondPlayerScore);
                roundComplete = 1;
                break;
            default:
                break;
        }
    }

    private static void score(){
        if (roundComplete == 0) {
            for (int i = 0, j = 0; i < 9 || j < 3; i += 3, j++) {
                if (!buttons[i].getText().equals("")) {
                    if (buttons[i].getText().equals(buttons[i + 1].getText()) &&
                            buttons[i].getText().equals(buttons[i + 2].getText())) {
                        switcherXO(buttons[i].getText());
                        break;
                    }
                }

                if (!buttons[j].getText().equals("")) {
                    if (buttons[j].getText().equals(buttons[j + 3].getText()) &&
                            buttons[j].getText().equals(buttons[j + 6].getText())) {
                        switcherXO(buttons[j].getText());
                        break;
                    }
                }
            }

            if (!buttons[0].getText().equals("")) {
                if (buttons[0].getText().equals(buttons[4].getText()) &&
                        buttons[0].getText().equals(buttons[8].getText()))
                    switcherXO(buttons[0].getText());
            }

            if (!buttons[2].getText().equals("")) {
                if (buttons[2].getText().equals(buttons[4].getText()) &&
                        buttons[2].getText().equals(buttons[6].getText()))
                    switcherXO(buttons[2].getText());
            }
        }

        if (roundComplete == 1){
            for (int i = 0, n = buttons.length; i < n; i++)
                buttons[i].setEnabled(false);
        }
    }

    private static void runGUI() {
        SimpleTicTacToe greeting = new SimpleTicTacToe();
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                runGUI();
            }
        });
    }
}