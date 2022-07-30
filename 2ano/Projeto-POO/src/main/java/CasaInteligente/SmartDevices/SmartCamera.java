package CasaInteligente.SmartDevices;

import java.io.FileWriter;
import java.io.IOException;
import java.io.Serializable;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.temporal.ChronoUnit;

/**
 * Uma SmartCamera e uma camera inteligente que liga e desliga (ja que
 * e subclasse de SmartDevice) e tambem contem informaçoes sobre a mesma.
 */
public class SmartCamera extends SmartDevice implements Serializable {
    private int xRes;
    private int yRes;
    private int fileSize;
    private float custoInstalacao;

    /**
     * Construtor por omissao de SmartCamera.
     */
    public SmartCamera(){
        super();
        this.xRes = 0;
        this.yRes = 0;
        this.fileSize = 0;
        this.custoInstalacao = 0;
    }

    /**
     * Construtor parametrizado.
     * @param id Codigo que identifica a SmartCamera.
     * @param status Estado da SmartCamera.
     * @param xRes Resoluçao da SmartCamera no eixo do x.
     * @param yRes Resoluçao da SmartCamera no eixo do y
     * @param fileSize Tamanho do ficheiro da SmartCamera.
     */
    public SmartCamera(String id, boolean status, int xRes, int yRes, int fileSize, float consumptionPerDay,  int custoInstalacao){
        super(id, status, consumptionPerDay, custoInstalacao);
        this.xRes = xRes;
        this.yRes = yRes;
        this.fileSize = fileSize;
        this.custoInstalacao = custoInstalacao;
    }

    /**
     * Construtor parametrizado.
     * @param id Codigo que identifica a SmartCamera.
     * @param status Estado da SmartCamera.
     */
    public SmartCamera(String id, boolean status){
        super(id, status);
        this.xRes = 0;
        this.yRes = 0;
        this.fileSize = 0;
        this.custoInstalacao = 0;
    }

    /**
     * Construtor de copia da SmartCamera.
     * @param s SmartCamera que e copiada para a nova.
     */
    public SmartCamera(SmartCamera s){
        super(s.getID(), s.getOn(), s.getConsumptionPerDay(), s.getCustoInstalacao());
        this.xRes = s.getxRes();
        this.yRes = s.getyRes();
        this.fileSize = s.getFileSize();
        this.custoInstalacao = s.getCustoInstalacao();
    }

    /**
     * Metodo que verifica a igualdade entre a SmartCamera e um outro objeto.
     * @param obj Objeto que e comparado com a SmartCamera.
     * @return Booleano que indica se sao iguais.
     */
    public boolean equals(Object obj){
        if(obj == this){
            return true;
        }
        if((obj == null) || (obj.getClass() != this.getClass())){
            return false;
        }

        SmartCamera c = (SmartCamera) obj;
        return (
                this.xRes == c.xRes                                &&
                this.yRes == c.yRes                                &&
                this.fileSize == c.getFileSize()
        );
    }

    /**
     * Metodo que devolve uma copia da SmartCamera.
     * @return copia da SmartCamera.
     */
    public SmartCamera clone(){
        return new SmartCamera(this);
    }

    /**
     * Metodo que produz uma string na qual esta representada a SmartCamera.
     * @return String que representa a SmartCamera.
     */
    public String toString(){
        StringBuilder sb = new StringBuilder();

        sb.append("Id: ").append(super.getID()).append("\n");
        sb.append("Estado: ").append(super.getOn()).append("\n");
        sb.append("Resolucao: ").append("\n");
        sb.append("X: ").append(this.getxRes()).append("\n");
        sb.append("Y: ").append(this.getyRes()).append("\n");
        sb.append("Tamanho do ficheiro gerado: ").append(this.getFileSize()).append("\n");
        sb.append("Consumo por dia em Kw/H: ").append(super.getConsumptionPerDay()).append("\n");
        sb.append("Consumo total: ").append(super.getConsumption()).append("\n");
        sb.append("Custo de instalacao: ").append(super.getCustoInstalacao()).append("\n");

        return sb.toString();
    }

    /**
     * Metodo que escreve a SmartCamera num ficheiro.
     * @param writer Ficheiro.
     * @throws IOException
     */
    public void writeInFile(FileWriter writer) throws IOException {
        String line = "SmartCamera:" + "(" + this.getxRes() + "x" + this.getyRes() + ")" +
                      "," + this.getFileSize() + "," + super.getConsumptionPerDay() + "\n";

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
     * Metodo que calcula o consumo da SmartCamera.
     */
    public void consumo(LocalDate before, LocalDate after){
        if(this.getOn()){
            float between = ChronoUnit.DAYS.between(before, after);
            super.setConsumption( super.getConsumption() + ( ((float)this.getxRes() *this.getyRes())/70000) * this.getFileSize() * super.getConsumptionPerDay() * between);
            super.setTime(after);
        }

    }

    /**
     * Getter que nos da a resolução no eixo do x
     * @return resoluçao no eixo do x
     */
    public int getxRes() {
        return this.xRes;
    }

    /**
     * Getter que nos da a resoluçao no eixo do y
     * @return resoluçao no eixo do y
     */
    public int getyRes() {
        return this.yRes;
    }

    /**
     * Metodo que devolve o tamanho do ficheiro da SmartCamera.
     * @return Tamanho do ficheiro.
     */
    public int getFileSize(){
        return this.fileSize;
    }


    /**
     * setter que nos coloca em xRes o valor passado como parâmetro
     * @param xRes resoluçao no eixo do x
     */
    public void setxRes(int xRes) {
        this.xRes = xRes;
    }

    /**
     * setter que nos coloca em yRes o valor passado como parametro
     * @param yRes resoluçao no eixo do y
     */
    public void setyRes(int yRes) {
        this.yRes = yRes;
    }

    /**
     * Metodo que altera o tamanho do ficheiro da SmartCamera.
     * @param size Novo tamanho do ficheiro.
     */
    public void setFileSize(int size){
        this.fileSize = size;
    }


}
