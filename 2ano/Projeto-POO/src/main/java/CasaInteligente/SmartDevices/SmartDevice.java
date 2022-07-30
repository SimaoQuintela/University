package CasaInteligente.SmartDevices;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.Serializable;
import java.time.LocalDate;
import java.time.LocalDateTime;

/**
 * A classe SmartDevice e um contactor simples.
 * Permite ligar ou desligar circuitos.
 */
public abstract class SmartDevice implements Serializable {
    private String id;
    private boolean on;
    private LocalDate time;
    private float consumption;
    private float consumptionPerDay;
    private int custoInstalacao;

    /**
     * Construtor por omissao de um SmartDevice.
     */
    public SmartDevice() {
        this.id = "";
        this.on = false;
        this.consumption = 0;
        this.consumptionPerDay = 0;
        this.time = LocalDate.now();
        this.custoInstalacao = 0;
    }

    /**
     * Construtor parametrizado de um SmartDevice.
     * @param id Codigo que identifica o SmartDevice.
     */
    public SmartDevice(String id) {
        this.id = id;
        this.on = false;
        this.consumption = 0;
        this.consumptionPerDay = 0;
        this.time = LocalDate.now();
        this.custoInstalacao = 0;
    }

    /**
     * Construtor parametrizado de um SmartDevice.
     * @param id Codigo que identifica o SmartDevice.
     * @param status Estado do SmartDevice.
     */
    public SmartDevice(String id, boolean status) {
        this.id = id;
        this.on = status;
        this.consumption = 0;
        this.consumptionPerDay = 0;
        this.time = LocalDate.now();
        this.custoInstalacao = 0;
    }

    /**
     * Construtor parametrizado de um SmartDevice.
     * @param id Codigo que identifica o SmartDevice.
     * @param status Estado (ligado ou desligado) do SmartDevice.
     */
    public SmartDevice(String id, boolean status, float consumptionPerDay, int custoInstalacao){
        this.id = id;
        this.on = status;
        this.consumption = 0;
        this.consumptionPerDay = consumptionPerDay;
        this.time = LocalDate.now();
        this.custoInstalacao = custoInstalacao;
    }

    /**
     * Construtor de copia de um SmartDevice.
     * @param s SmartDevice utilizado no processo de copia para o novo SmartDevice.
     */
    public SmartDevice(SmartDevice s) {
        this(s.getID(), s.getOn(), s.getConsumptionPerDay(), s.getCustoInstalacao());
    }

    /**
     * Metodo que devolve uma copia do SmartDevice recetor da mensagem.
     * @return copia do SmartDevice recetor da mensagem.
     */
    public abstract SmartDevice clone();

    /**
     * Metodo que verifica a igualdade entre um objeto e o SmartDevice recetor da mensagem.
     * @param o objeto comparado com o SmartDevice.
     * @return booleano que indica se sao iguais.
     */
    public abstract boolean equals(Object o);

    /**
     * Metodo que produz uma String na qual esta representado o SmartDevice.
     * @return string que representa o SmartDevice.
     */
    public abstract String toString();

    public abstract void writeInFile(FileWriter writer) throws IOException;

    /**
     * Metodo que liga o SmartDevice.
     */
    public abstract void turnOn();

    /**
     * Metodo que desliga o SmartDevice.
     */
    public abstract void turnOff();

    /**
     * Metodo que calcula o consumo do SmartDevice.
     */
    public abstract void consumo(LocalDate before, LocalDate after);

    /**
     * Metodo que devolve o estado do SmartDevice.
     * @return Estado do SmartDevice.
     */
    public boolean getOn() {return this.on;}

    /**
     * Metodo que devolve o codigo que identifica o SmartDevice.
     * @return Codigo que identifica o SmartDevice.
     */
    public String getID() {return this.id;}

    /**
     * Metodo que devolve o consumo de energia do SmartDevice.
     * @return Consumo do SmartDevice.
     */
    public float getConsumption(){
        return this.consumption;
    }

    /**
     * Metodo que devolve o consumo diario do SmartDevice.
     * @return Consumo diario do SmartDevice.
     */
    public float getConsumptionPerDay() {
        return this.consumptionPerDay;
    }

    /**
     * Metodo que devolve o custo de instalaçao do SmartDevice.
     * @return Custo de instalaçao do SmartDevice.
     */
    public int getCustoInstalacao() {
        return this.custoInstalacao;
    }

    /**
     * Metodo que devolve o momento em que o estado do SmartDevice foi alterado pela ultima vez.
     * @return Momento em que o estado do SmartDevice foi alterado pela ultima vez.
     */
    public LocalDate getTime() {
        return this.time;
    }

    /**
     * Metodo que altera o estado do SmartDevice.
     * @param b Novo estado do SmartDevice.
     */
    public void setOn(boolean b) {this.on = b;}

    /**
     * Coloca em id o valor passado como parâmetro
     * @param id Id do SmartDevice
     */
    public void setId(String id) {
        this.id = id;
    }

    /**
     * Metodo que altera o consumo energetico da SmartCamera.
     * @param consumption Novo consumo energetico da SmartCamera.
     */
    public void setConsumption(float consumption){
        this.consumption = consumption;
    }

    /**
     * Metodo que altera o custo de instalaçao do SmartDevice.
     * @param custoInstalacao Custo de instalaçao do SmartDevice.
     */
    public void setCustoInstalacao(int custoInstalacao) {
        this.custoInstalacao = custoInstalacao;
    }

    /**
     * Metodo que altera o consumo diario do SmartDevice.
     * @param consumptionPerDay Consumo diario do SmartDevice.
     */
    public void setConsumptionPerDay(float consumptionPerDay) {
        this.consumptionPerDay = consumptionPerDay;
    }

    /**
     * Metodo que altera o momento em que o estado do SmartDevice foi alterado pela ultima vez.
     * @param time Momento em que o estado do SmartDevice foi alterado pela ultima vez.
     */
    public void setTime(LocalDate time) {
        this.time = time;
    }
}
