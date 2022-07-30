import java.io.*;
import java.time.LocalDate;
import java.util.*;


import CasaInteligente.*;
import CasaInteligente.SmartDevices.SmartDevice;
import ComercializadoresEnergia.Fatura;

import static java.lang.System.out;

/**
 * Controller e o controlador que responde a pedidos da View.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class Controller implements Serializable {

    private Comunidade comunidade;
    private int idFatura;
    private LocalDate timeNow;


    /**
     * Construtor por omissao de Controller.
     */
    public Controller() {
        this.comunidade = new Comunidade();
        this.idFatura = 1;
        this.timeNow = LocalDate.now();
    }

    /**
     * Metodo que limpa a consola.
     * @throws IOException
     * @throws InterruptedException
     */
    public void cls() throws IOException, InterruptedException {
        new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
    }

    /**
     * Metodo que devolve uma CasaInteligente tendo em conta um determinado NIF.
     * @param NIF NIF do proprietario.
     * @return CasaInteligente do proprietario com um determinado NIF.
     */
    public CasaInteligente consultaCasa(int NIF){
        for(CasaInteligente c: this.getComunidade().getCasas().values()){
            if(c.getNIF() == NIF){
                return c;
            }
        }

        return null;
    }

    /**
     * Metodo que liga/desliga todos os SmartDevices de todas as Casas de uma Comunidade.
     * @param status Booleano que indica o efeito provocado pelo metodo (ligar/desligar).
     */
    public void ligarDesligarComunidade(boolean status){
        for(CasaInteligente c: this.getComunidade().getCasas().values()){
            ligarDesligarCasa(status, c.getNIF());
        }
    }

    /**
     * Metodo que liga/desliga todos os SmartDevices de uma determinada CasaInteligente.
     * @param status Booleano que indica o efeito provocado pelo metodo (ligar/desligar).
     * @param NIF NIF do proprietario da CasaInteligente.
     */
    public void ligarDesligarCasa(boolean status, int NIF){
        CasaInteligente casa = null;
        for(CasaInteligente c: this.getComunidade().getCasas().values()){
            if(c.getNIF() == NIF){
                casa = c;
            }
        }

        assert casa != null;
        for(SmartDevice s: casa.getDevices().values()) {
            if (!status) {
                s.turnOff();
            } else {
                s.turnOn();
            }
        }

    }

    /**
     * Metodo que diz qual a casa que mais gastou num certo periodo de tempo
     * @param periodo periodo de tempo
     * @return proprietario da casa que mais gastou durante o periodo passado como parametro
     */
    public Tuple casaQueMaisGastou(LocalDate periodo){
        float max = 0;
        String propMaisGastou = "";
        for(String prop: this.getComunidade().getCasas().keySet()){
            for(Fatura f: this.getComunidade().getCasa(prop).getFaturas()){
                if(f.getDataEmissao().equals(periodo) && f.getTotal() > max){
                    max = f.getTotal();
                    propMaisGastou = prop;
                }

            }
        }
        Tuple t = new Tuple(propMaisGastou, max);
        return t;
    }

    /**
     * Metodo que devolve o Comercializador com maior volume de faturaçao.
     * @return Tuplo com o Comercializador com maior volume de faturaçao associado ao respetivo valor de faturaçao.
     */
    public Tuple comercializadorQueMaisFatura(){
        String comMaisFaturou = "";
        float max = 0;
        for(String com: this.getComunidade().getMercado().keySet()){
            float faturacao = this.getComunidade().getFornecedor(com).calculaFaturacao();
            if(faturacao > max){
                max = faturacao;
                comMaisFaturou = com;
            }
        }

        Tuple t = new Tuple(comMaisFaturou, max);
        return t;
    }

    /**
     * Metodo que devolve um Map com toda a faturaçao de um determinado Comercializador.
     * @param fornecedor Nome do Comercializador.
     * @return Faturaçao de um determinado Comercializador.
     */
    public Map<String,List<Fatura>> listaFaturas(String fornecedor){
        return this.getComunidade().getFornecedor(fornecedor).getFaturas();
    }

    /**
     * Metodo que devolve um ordenaçao dos maiores consumidores de energia durante um determinado período de tempo.
     * @param periodo Periodo de tempo.
     * @return Lista de Tuplos ordenada decrescentemente conforme o valor total de faturaçao de cada Comercializador.
     */
    public List<Tuple> ordenaConsumidores(LocalDate periodo){
        List<Tuple> consumidores_ordenados = new ArrayList<>();

        for(String prop: this.getComunidade().getCasas().keySet()){
            float consumo = 0;
            for(Fatura f: this.getComunidade().getCasa(prop).getFaturas()){
                if(f.getDataEmissao().equals(periodo)){
                    consumo += f.getTotal();
                }
            }
            Tuple t = new Tuple(prop, consumo);
            consumidores_ordenados.add(t);
        }

        consumidores_ordenados.sort(new ConsumeComparator());
        return consumidores_ordenados;
    }

    /**
     * Metodo que guarda a Comunidade num ficheiro de texto.
     * @param textFile Ficheiro onde e guardada a Comunidade.
     * @throws IOException
     */
    public void saveProgramText(String textFile) throws IOException {
        SaveProgramText.saveTextMode(this.getComunidade(), textFile);
    }

    /**
     * Metodo que carrega o ficheiro que contem uma Comunidade.
     * @param textFile
     * @throws IOException
     */
    public void loadProgramText(String textFile) throws IOException{
        Parser.parse(this.getComunidade(), textFile);
    }

    /**
     * Metodo que guarda todos os objetos num ficheiro.
     * @param objectFile Ficheiro onde sao guardados os objetos.
     * @throws IOException
     */
    public void saveProgramObjects(String objectFile) throws IOException {
        FileOutputStream fos =  new FileOutputStream(objectFile);
        ObjectOutputStream oos = new ObjectOutputStream(fos);
        oos.writeObject(this);
        oos.flush();
        oos.close();
    }

    /**
     * Metodo que carrega o ficheiro que contem objetos.
     * @param file Ficheiro que e carregado.
     * @throws IOException
     * @throws ClassNotFoundException
     */
    public void loadProgramObjects(String file) throws IOException, ClassNotFoundException {
        FileInputStream fis = new FileInputStream(file);
        ObjectInputStream ois = new ObjectInputStream(fis);

        Controller new_controlador = (Controller) ois.readObject();
        this.comunidade.setNomeDaComunidade(new_controlador.comunidade.getNomeDaComunidade());
        new_controlador.comunidade.getCasas().forEach((k,v) -> this.comunidade.setCasas(k,v));
        new_controlador.comunidade.getMercado().forEach((k,v) -> this.comunidade.setMercado(k,v));


        ois.close();
        fis.close();
    }

    /**
     * Metodo que devolve a Comunidade.
     * @return Comunidade.
     */
    public Comunidade printComunity(){
        return this.getComunidade();
    }

    /**
     * Metodo responsavel pela execuçao da Simulaçao.
     * @param timeSimul Tempo que e avançado na simulaçao.
     * @param file Ficheiro de simulaçao.
     */
    public void simulacao(String timeSimul, String file) {
        LocalDate timeStart = this.timeNow;

        String[] timeSimulSplitted = timeSimul.split("/");
        Map<String, Float> consumos = new HashMap<>();  // consumo de cada casa associado ao valor do consumo total
        LocalDate timeEnd = LocalDate.of(Integer.parseInt(timeSimulSplitted[2]), Integer.parseInt(timeSimulSplitted[1]), Integer.parseInt(timeSimulSplitted[0]));

        if(file != null){
            int flag = 0;
            TreeMap<String, List<List<String>>> actions;
            actions = SimulParser.simulParser(file);
            LocalDate simulDate;
            for(String k: actions.keySet()) {
                String[] data = k.split("\\.");
                simulDate = LocalDate.of(Integer.parseInt(data[0]), Integer.parseInt(data[1]), Integer.parseInt(data[2])); // data para a qual vamos saltar
                out.println(simulDate);
                // feita a simulação e guardados os consumos no mapa consumos
                for(String prop: this.comunidade.getCasas().keySet()) {  // iterar sobre cada casa
                    CasaInteligente casaAtual = this.comunidade.getCasa(prop);
                    //Map<String, Float> consumos_temp = new HashMap<>();     // consumo de cada dispositivo da casa
                    //consumos_temp.putAll(casaAtual.simula(this.timeNow, simulDate, comunidade.getFornecedor(casaAtual.getFornecedor())));
                    float valorSimul = casaAtual.simula(this.timeNow, simulDate, comunidade.getFornecedor(casaAtual.getFornecedor()));

                    if (consumos.containsKey(prop)) {
                        consumos.replace(prop, consumos.get(prop) + valorSimul); // criar um novo consumo para um novo dispositivo
                    } else {
                        consumos.put(prop, valorSimul);           // incrementar ao consumo que existia
                    }

                }
                this.timeNow = simulDate;

                for (List<String> l : actions.get(k)) {
                    switch (l.get(2)) {
                        case "turnOff" -> {
                            String proprietario = l.get(0);
                            String id = l.get(1);
                            this.comunidade.getCasa(proprietario).getDevice(id).turnOff();

                        }
                        case "turnOn" -> {
                            String proprietario = l.get(0);
                            String id = l.get(1);
                            this.comunidade.getCasa(proprietario).getDevice(id).turnOn();

                        }
                        case "mudar" -> {
                            String proprietario = l.get(0);
                            String novoFornecedor = l.get(1);
                            this.comunidade.getCasa(proprietario).setFornecedor(novoFornecedor);

                        }
                        case "mudarNumDisp" -> {
                            String proprietario = l.get(0);
                            int numDisps = Integer.parseInt(l.get(1));
                            this.comunidade.getFornecedor(proprietario).setNumeroDispositivos(numDisps);
                        }
                        case "novaLoc" -> {
                            String proprietario = l.get(0);
                            String id = l.get(1);
                            String novaLoc = l.get(3);
                            SmartDevice device = this.comunidade.getCasa(proprietario).getDevice(id).clone();
                            this.comunidade.getCasa(proprietario).removeDevice(id);
                            this.comunidade.getCasa(proprietario).addDevice(device, novaLoc);

                        }
                        case "remover" -> {
                            String proprietario = l.get(0);
                            String id = l.get(1);
                            this.comunidade.getCasa(proprietario).removeDevice(id);
                        }
                    }
                }
            }
        }

        for(CasaInteligente casaAtual: this.comunidade.getCasas().values()) {
            // SALTO PARA O TEMPO FINAL
            float totalSimulacao = casaAtual.simula(this.timeNow, timeEnd, comunidade.getFornecedor(casaAtual.getFornecedor()));


            if (consumos.containsKey(casaAtual.getProprietario())) {
                consumos.replace(casaAtual.getProprietario(), consumos.get(casaAtual.getProprietario()) + totalSimulacao); // criar um novo consumo para um novo dispositivo
            } else {
                consumos.put(casaAtual.getProprietario(), totalSimulacao);           // incrementar ao consumo que existia
            }


            // GERA FATURA
            Fatura f = new Fatura(idFatura, consumos.get(casaAtual.getProprietario()), casaAtual.getFornecedor(), casaAtual.getNIF(), casaAtual.getProprietario(), timeEnd);
            out.println(f);
            casaAtual.addFatura(f);

            String fornecedor = casaAtual.getFornecedor();
            this.comunidade.getFornecedor(fornecedor).adicionaFatura(casaAtual.getProprietario(), f);
            this.idFatura += 1;

            this.timeNow = timeStart;
        }

        this.timeNow = timeEnd;

        // NO FIM COLOCAR O CONSUMO DE TODOS OS DISPOSITIVOS A 0
        for(CasaInteligente c : this.comunidade.getCasas().values()){
            for(SmartDevice s : c.getDevices().values()){
                s.setConsumption(0);
            }
        }
    }

    /**
     * Metodo que devolve a Comunidade.
     * @return Comunidade.
     */
    public Comunidade getComunidade() {
        return this.comunidade;
    }

    /**
     * Metodo que devolve o numero de identificaçao da Fatura.
     * @return ID da Fatura.
     */
    public int getIdFatura() {
        return this.idFatura;
    }

    /**
     * Metodo que devolve o tempo corrente.
     * @return Tempo corrente.
     */
    public LocalDate getTimeNow() {
        return this.timeNow;
    }

    /**
     * Metodo que altera o ID da Fatura.
     * @param idFatura Novo ID da Fatura.
     */
    public void setIdFatura(int idFatura) {
        this.idFatura = idFatura;
    }

    /**
     * Metodo que altera o tempo corrente.
     * @param timeNow Novo tempo corrente.
     */
    public void setTimeNow(LocalDate timeNow) {
        this.timeNow = timeNow;
    }
}
