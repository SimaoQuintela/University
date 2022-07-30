import java.time.LocalDateTime;
import java.time.temporal.ChronoUnit;
import java.util.Scanner;
import static java.lang.System.out;
public class Ficha3 {

    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        out.println("Exercício: ");
        int ex = scan.nextInt();
        out.println("Alínea: ");
        String alinea = scan.next();

        switch(ex){
            case 1:
                Circulo circulo = new Circulo(1, 1, 9);

                switch(alinea){
                    case "a":
                        double x = circulo.getX();
                        out.println("Valor em x: " + x);
                        break;
                    case "b":
                        double y = circulo.getY();
                        out.println("Valor em y: " + y);
                        break;
                    case "c":
                        double raio = circulo.getRaio();
                        out.println("Valor do raio: " + raio);
                        break;
                    case "d":
                        circulo.setX(2);
                        circulo.setY(2);
                        circulo.setRaio(16);
                        out.println("X: " + circulo.getX());
                        out.println("Y: " + circulo.getY());
                        out.println("Raio: " + circulo.getRaio());
                        break;
                    case "e":
                        circulo.alteraCentro(10, 10);
                        out.println("X: " + circulo.getX());
                        out.println("Y: " + circulo.getY());
                        break;
                    case "f":
                        out.println("Área: " + circulo.calculaArea());
                        break;
                    case "g":
                        out.println("Perímetro: " + circulo.calculaPerimetro());
                        break;
                    default:
                        out.println("Não existe essa alínea");
                        break;
                }
                break;
            case 2:
                Telemovel telemovel = new Telemovel("Huawei", "P20 Lite",300, 600, 40,10000,4000, 6000);
                telemovel.instalaApp("Youtube", 1000);
                telemovel.instalaApp("Instagram", 1000);
                telemovel.instalaApp("Twitter", 1000);
                telemovel.instalaApp("Twitch", 1000);
                telemovel.instalaApp("Blackboard", 1000);
                switch (alinea){
                    case "a":
                        boolean espaco = telemovel.existeEspaco(3000);
                        out.println("Existe espaço: " + espaco);

                        espaco = telemovel.existeEspaco(5000);
                        out.println("Existe espaço: " + espaco);

                        espaco = telemovel.existeEspaco(2000);
                        out.println("Existe espaço: " + espaco);
                        break;
                    case "b":
                        String[] apps = telemovel.getNomeAppsInstaladas();
                        out.println("-------------- Apps instaladas --------------");
                        for(int i=0; i< telemovel.getNumAppsInstaladas(); i+=1){
                            out.println(apps[i]);
                        }
                        break;
                    case "c":
                        telemovel.recebeMsg("I'm not great at the advice.");
                        telemovel.recebeMsg("Can I interest you in a sarcastic comment?");
                        telemovel.recebeMsg("Some cheese?");
                        String[] mensagens = telemovel.getMensagens();
                        out.println("-------------- Mensagens --------------");
                        for(int i =0; i<telemovel.getNumeroMensagens(); i+=1){
                            out.println(mensagens[i]);
                        }
                        break;
                    case "d":
                        double tamMedio = telemovel.tamMedioApps();
                        out.println("Tamanho medio das apps: " + tamMedio);
                        break;
                    case "e":
                        String maiorMsg = telemovel.maiorMsg();
                        out.println("Maior mensagem: " + maiorMsg);
                        break;
                    case "f":
                        telemovel.removeApp("Twitter", 1000);
                        telemovel.removeApp("Youtube", 1000);
                        telemovel.removeApp("Blackboard", 1000);

                        String[] appps = telemovel.getNomeAppsInstaladas();
                        out.println("-------------- Apps instaladas --------------");
                        for(int i=0; i< telemovel.getNumAppsInstaladas(); i+=1){
                            out.println(appps[i]);
                        }
                        break;
                    default:
                        out.println("Não existe essa alínea");
                        break;
                }
                break;

            case 3:
                char[] conteudo = new char[10];
                Youtube video1 = new Youtube("10 reasons why Computer Science is so cool! ", conteudo, LocalDateTime.now(), 1024, 10,30);
                Youtube video2 = new Youtube("Chandler being sarcastic for 10 minutes", conteudo, LocalDateTime.now(), 1024, 10,0);
                switch (alinea){
                    case "b":
                        video1.insereComentario("Loved it!");
                        video1.insereComentario("Agreed with every single one!");
                        video1.insereComentario("DAMN IT! I WANT TO STUDY COMPUTER SCIENCE NOW!");

                        video2.insereComentario("I want 10 more!");
                        video2.insereComentario("Miss Chanandler Bong never disappoints!");
                        video2.insereComentario("Could he be more sarcastic?");

                        out.println("---------------- Comentários video 1 ----------------");
                        String[] comentarios = video1.getComentarios();
                        for(int i = 0; i<comentarios.length; i+=1)
                            out.println("Comentário " + (i+1) +": " + comentarios[i]);

                        out.println("---------------- Comentários video 2 ----------------");
                        String[] comentarios2 = video2.getComentarios();
                        for(int i = 0; i<comentarios2.length; i+=1)
                            out.println("Comentário " + (i+1) +": " + comentarios2[i]);
                        break;
                    case "c":
                        out.println("Passaram " + video1.qtsDiasDepois() + " dias");
                        out.println("Passaram " + video2.qtsDiasDepois() + " dias");
                        break;
                    case "d":
                        for(int i = 0; i< 100; i+=1)
                            video1.thumbsUp();
                        out.println("Likes: " + video1.getLikes());
                        break;
                    default:
                        out.println("Alínea inexistente");
                        break;
                }
                break;
            /*
            case 4:
                Lampada l = new Lampada(0); // desligada

                LocalDateTime inicioOn = LocalDateTime.now();
                l.lampON();
                out.println("Estado: " + l.getEstado());
                LocalDateTime fimOn = LocalDateTime.now();

                long timeOn = ChronoUnit.MILLIS.between(inicioOn, fimOn);

                LocalDateTime inicioEco = LocalDateTime.now();
                l.lampECO();
                out.println("Estado: " + l.getEstado());
                LocalDateTime fimEco = LocalDateTime.now();

                long timeEco = ChronoUnit.MILLIS.between(inicioEco, fimEco);

                l.lampOFF();
                out.println("Estado: " + l.getEstado());

                long consumo = timeOn * 10 + timeEco * 5;
                out.println(l.totalConsumo() + " == " + consumo);
                out.println(l.periodoConsumo());
                break;
             */
            case 5:
                Futebol jogo = new Futebol(0,0,0);
                out.println("Estado do jogo: " + jogo.getEstado());
                jogo.startGame();
                out.println("Estado do jogo: " + jogo.getEstado());
                jogo.goloVisitado();
                jogo.goloVisitado();
                jogo.goloVisitado();
                jogo.goloVisitante();
                out.println("Visitado: " + jogo.getGolosEquipaVisitada());
                out.println("Visitante: " + jogo.getGolosEquipaVisitante());
                jogo.endGame();
                out.println("Estado do jogo: " + jogo.getEstado());
                out.println(jogo.resultadoActual());
                break;
            case 8:
                Encomenda enc = new Encomenda("Supermercados Coviran", 123456789, "Rua sem nome", 47, LocalDateTime.now());
                LinhaEncomenda l1 = new LinhaEncomenda("1234", "Chipicao", 0.99, 300, 13, 5);
                LinhaEncomenda l2 = new LinhaEncomenda("2341", "Bollycao", 0.99, 300, 13, 5);
                LinhaEncomenda l3 = new LinhaEncomenda("3412", "Iogurte Grego Pack-4", 0.99, 100, 23, 5);
                LinhaEncomenda l4 = new LinhaEncomenda("4123", "Massa Milaneza", 1.25, 200, 23, 10);
                enc.adicionaLinha(l1);
                enc.adicionaLinha(l2);
                enc.adicionaLinha(l3);
                enc.adicionaLinha(l4);

                out.println("Valor total: " + enc.calculaValorTotal());
                out.println("Valor desconto: " + enc.calculaValorDesconto());
                out.println("Número total de produtos: " + enc.numeroTotalProdutos());
                out.println("Existe encomenda para o código 2341: " + enc.existeProdutoEncomenda("2341"));
                out.println("Existe encomenda para o código 2349: " + enc.existeProdutoEncomenda("2349"));

                out.println("------------ Produtos --------------");
                for(LinhaEncomenda l: enc.getLinhasEncomenda()){
                    out.println("Produto: " + l.getDescricao());
                }

                enc.removeProduto("2341");
                enc.removeProduto("1234");
                enc.removeProduto("3412");
                enc.removeProduto("4123");
                out.println("------------ Produtos --------------");
                for(LinhaEncomenda l: enc.getLinhasEncomenda()){
                    out.println("Produto: " + l.getDescricao());
                }
                break;
            case 9:
                Ponto p1 = new Ponto(0,0);
                Ponto p2 = new Ponto(5,0);
                Ponto p3 = new Ponto(0, 5);
                Triangulo t = new Triangulo(p1,p2,p3);
                Triangulo t2 = new Triangulo(p1,p2,p3);

                // prova de que estou a usar bem a composição
                out.println(t.getP1());
                out.println(t2.getP1());
                p1.setX(20);
                p1.setY(2);
                // altero o valor das coordenadas do ponto p1 mas
                // os pontos dos triangulos t1 e t2 não mudam pq lhes
                // passei um clone
                out.println(t.getP1());
                out.println(t2.getP1());

                out.println("Perímetro: " + t.calculaPerimetroTriangulo());
                out.println("Área: " + t.calculaAreaTriangulo());
                out.println("Altura: " + t.alturaTriangulo());
                break;
        }

    }


}
