package CasaInteligente.SmartDevices;

import java.io.FileWriter;
import java.io.IOException;
import java.io.Serializable;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.temporal.ChronoUnit;

/**
 * Um SmartSpeaker e um SmartDevice que alem de ligar e desligar permite tambem
 * reproduzir som.
 * Consegue ligar-se a um canal (por simplificaçao uma radio online) e permite
 * a regulaçao do seu nivel de volume.
 */
public class SmartSpeaker extends SmartDevice implements Serializable {
    private static final int MAX = 100; //volume máximo

    private int volume;
    private String channel;
    private String brand;


    /**
     * Construtor por omissao de SmartSpeaker.
     */
    public SmartSpeaker() {
        // initialise instance variables
        super();
        this.channel = "";
        this.volume = 0;
        this.brand = "";
    }

    /**
     * Construtor parametrizado de SmartSpeaker.
     * @param id ID do dispositivo.
     * @param channel Canal de radio.
     * @param volume Volume da SmartSpeaker.
     * @param brand Marca da SmartSpeaker.
     */
    public SmartSpeaker(String id, String channel, String brand, int volume) {
        // initialise instance variables
        super(id);
        this.channel = channel;
        this.volume = volume;
        this.brand = brand;
    }

    /**
     * Construtor parametrizado de SmartSpeaker.
     * @param cod Codigo que identifica a SmartSpeaker.
     * @param channel Canal de radio.
     * @param volume Volume da SmartSpeaker.
     * @param brand Marca da SmartSpeaker.
     */
    public SmartSpeaker(String cod, boolean on, String channel, int volume, String brand, float consumptionPerDay, int custoInstalacao) {
        // initialise instance variables
        super(cod, on, consumptionPerDay, custoInstalacao);
        this.channel = channel;
        this.volume = volume;
        this.brand = brand;
    }

    /**
     * Construtor de copia de SmartSpeaker.
     * @param s SmartSpeaker que e copiada.
     */
    public SmartSpeaker(SmartSpeaker s){
        this(s.getID() , s.getOn(), s.getChannel(), s.getVolume(), s.getBrand(), s.getConsumptionPerDay(), s.getCustoInstalacao());
    }

    /**
     * Metodo que cria uma copia de uma SmartSpeaker.
     * @return Copia da SmartSpeaker.
     */
    public SmartSpeaker clone(){
        return new SmartSpeaker(this);
    }

    /**
     * Metodo que verifica a igualdade entre a SmartSpeaker e um outro objeto.
     * @param o objeto comparado com a SmartSpeaker.
     * @return Booleano que indica o resultado da comparaçao.
     */
    public boolean equals(Object o){
        if(this == o)
            return true;

        if(o == null || o.getClass() != this.getClass())
            return false;

        SmartSpeaker s = (SmartSpeaker) o;

        return(
                this.volume == s.getVolume()                       &&
                this.getChannel().equals(s.getChannel())           &&
                this.brand.equals(s.getBrand())
        );
    }

    /**
     * Metodo que produz uma string na qual esta representada a SmartSpeaker.
     * @return String que representa a SmartSpeaker.
     */
    public String toString(){
        StringBuilder sb = new StringBuilder();
        sb.append("Id: ").append(super.getID()).append("\n");
        sb.append("Estado: ").append(super.getOn()).append("\n");
        sb.append("Canal: ").append(this.getChannel()).append("\n");
        sb.append("Volume: ").append(this.getVolume()).append("\n");
        sb.append("Marca: ").append(this.getBrand()).append("\n");
        sb.append("Consumo por dia em Kw/H: ").append(super.getConsumptionPerDay()).append("\n");
        sb.append("Consumo total: ").append(super.getConsumption()).append("\n");
        sb.append("Custo de instalacao: ").append(super.getCustoInstalacao()).append("\n");

        return sb.toString();
    }

    /**
     * Metodo que escreve a SmartSpeaker num Ficheiro.
     * @param writer Ficheiro.
     * @throws IOException
     */
    public void writeInFile(FileWriter writer) throws IOException {
        String line = "SmartSpeaker:" + this.getVolume() + "," + this.getChannel() + "," +
                      this.getBrand() + "," + super.getConsumptionPerDay() + "\n";

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
     * Metodo que calcula o consumo da SmartSpeaker.
     */
    public void consumo(LocalDate before, LocalDate after){
        if(this.getOn()){
            float between = ChronoUnit.DAYS.between(before, after);
            super.setConsumption((float) (super.getConsumption() + this.getVolume()/20.0 * super.getConsumptionPerDay() * between));
            super.setTime(after);
        }

    }

    /**
     * Metodo que aumenta uma unidade no volume da SmartSpeaker.
     */
    public void volumeUp() {
        if (this.volume<MAX) this.volume++;
    }

    /**
     * Metodo que reduz uma unidade no volume da SmartSpeaker.
     */
    public void volumeDown() {
        if (this.volume>0) this.volume--;
    }

    /**
     * Metodo que devolve o volume da SmartSpeaker.
     * @return Volume da SmartSpeaker.
     */
    public int getVolume() {return this.volume;}

    /**
     * Metodo que devolve o canal de radio que esta a tocar na SmartSpeaker.
     * @return Canal de radio que esta a tocar na SmartSpeaker.
     */
    public String getChannel() {return this.channel;}

    /**
     * Metodo que devolve a marca da SmartSpeaker.
     * @return Marca da SmartSpeaker.
     */
    public String getBrand(){
        return this.brand;
    }


    /**
     * Metodo que altera o canal de radio que toca na SmartSpeaker.
     * @param c Novo canal de radio que toca na SmartSpeaker.
     */
    public void setChannel(String c) {this.channel = c;}

    /**
     * Metodo que altera a marca da SmartSpeaker.
     * @param s Nova marca da SmartSpeaker.
     */
    public void setBrand(String s){
        this.brand = s;
    }

    /**
     * Metodo que altera o volume da SmartSpeaker.
     * @param i Novo volume da SmartSpeaker.
     */
    public void setVolume(int i){
        if(i >= 0 && i <= 20 )
            this.volume = i;
    }


}
