package CasaInteligente.SmartDevices;

import java.io.FileWriter;
import java.io.IOException;
import java.io.Serializable;
import java.time.LocalDate;
import java.time.temporal.ChronoUnit;

import static java.lang.System.out;

/**
 * Uma SmartBulb e uma lampada inteligente que alem de ligar e desligar (ja que
 * e subclasse de SmartDevice) tambem permite escolher a intensidade da iluminaçao
 * (a cor da mesma).
 */
public class SmartBulb extends SmartDevice implements Serializable {
    private static final int WARM = 80;
    private static final int NEUTRAL = 60;
    private static final int COLD = 40;

    private int tone;
    private int dimensions;


    /**
     * Construtor por omissao de uma SmartBulb
     */
    public SmartBulb() {
        super();
        this.tone = NEUTRAL;
        this.dimensions = 0;
    }

    /**
     * Construtor parametrizado de uma SmartBulb.
     * @param id Codigo que identifica a SmartBulb.
     * @param tone Tonalidade da lampada.
     * @param dimensions Dimensoes da lampada.
     */
    public SmartBulb(String id, boolean status, int tone, int dimensions, float consumptionPerDay, int custoInstalacao) {
        super(id, status, consumptionPerDay, custoInstalacao);
        this.tone = tone;
        this.dimensions = dimensions;
    }

    /**
     * Construtor parametrizado de uma SmartBulb.
     * @param id Codigo que identifica a SmartBulb.
     */
    public SmartBulb(String id) {
        super(id);
        this.tone = NEUTRAL;
        this.dimensions = 0;
    }

    /**
     * Construtor parametrizado de uma SmartBulb.
     * @param id Codigo que identifica a SmartBulb.
     */
    public SmartBulb(String id, boolean status) {
        super(id, status);
        this.tone = NEUTRAL;
        this.dimensions = 0;
    }

    /**
     * Construtor de copia de uma SmartBulb.
     * @param s SmartBulb que e copiada para a nova.
     */
    public SmartBulb(SmartBulb s){
        super(s.getID(), s.getOn(), s.getConsumptionPerDay(), s.getCustoInstalacao());
        this.tone = s.getTone();
        this.dimensions = s.getDimensions();
    }

    /**
     * Metodo que cria uma copia da SmartBulb recetora da mensagem.
     * @return copia da SmartBulb recetora da mensagem.
     */
    public SmartBulb clone(){
        return new SmartBulb(this);
    }

    /**
     * Metodo que verifica a igualdade entre a SmartBulb e um outro objeto.
     * @param o Objeto comparado com a SmartBulb.
     * @return Booleano que indica se sao iguais.
     */
    public boolean equals(Object o){
        if(o == this)
            return true;

        if(o == null || this.getClass() != o.getClass())
            return false;

        SmartBulb s = (SmartBulb) o;

        return (
                this.tone == s.getTone()                           &&
                this.dimensions == s.getDimensions()
        );
    }

    /**
     * Metodo que produz uma string na qual esta representada a SmartBulb.
     * @return string que representa a SmartBulb.
     */
    public String toString(){
        StringBuilder sb = new StringBuilder();

        sb.append("Id: ").append(super.getID()).append("\n");
        sb.append("Estado: ").append(super.getOn()).append("\n");
        sb.append("Tonalidade: ").append(this.getTone()).append("\n");
        sb.append("Dimensoes: ").append(this.getDimensions()).append("\n");
        sb.append("Custo de instalacao: ").append(super.getCustoInstalacao()).append("\n");
        sb.append("Consumo por dia em Kw/H: ").append(super.getConsumptionPerDay()).append("\n");
        sb.append("Consumo total: ").append(super.getConsumption()).append("\n");

        return sb.toString();
    }

    /**
     * Metodo que escreve a SmartBulb num ficheiro.
     * @param writer Ficheiro.
     * @throws IOException
     */
    public void writeInFile(FileWriter writer) throws IOException {
        String tone = "";

        if(this.getTone() == 80){
            tone = "Warm";
        } else if(this.getTone() == 60) {
            tone = "Neutral";
        } else {
            tone = "Cold";
        }

        String line = "SmartBulb:" + tone + "," + this.getDimensions() + "," +
                      super.getConsumptionPerDay() + "\n";

        writer.write(line);
        writer.flush();
    }


    /**
     * Metodo que liga um SmartDevice
     */
    public void turnOn() {
        super.setOn(true);
        super.setTime(LocalDate.now());
    }

    /**
     * Metodo que desliga um SmartDevice
     */
    public void turnOff() {
        super.setOn(false);
        super.setTime(LocalDate.now());
    }

    /**
     * Metodo que calcula o consumo da SmartBulb.
     */
    public void consumo(LocalDate before, LocalDate after) {
        if(this.getOn()){
            float between = ChronoUnit.DAYS.between(before, after);
            super.setConsumption((float) (super.getConsumption() + this.getTone() * super.getConsumptionPerDay() * between));
            super.setTime(after);
        }

    }

    /**
     * Metodo que devolve a tonalidade da SmartBulb.
     * @return Tonalidade da SmartBulb.
     */
    public int getTone() {
        return this.tone;
    }

    /**
     * Metodo que devolve as dimensoes da SmartBulb.
     * @return Dimensoes da SmartBulb.
     */
    public int getDimensions(){
        return this.dimensions;
    }


    /**
     * Metodo que altera as dimensoes da SmartBulb.
     * @param dim Novas dimensoes da SmartBulb.
     */
    public void setDimensions(int dim){
        this.dimensions = dim;
    }


    /**
     * Metodo que altera a tonalidade da SmartBulb.
     * @param t Nova tonalidade da SmartBulb.
     */
    public void setTone(int t) {
        if (t>WARM) this.tone = WARM;
        else if (t<COLD) this.tone = COLD;
        else this.tone = t;
    }

}

