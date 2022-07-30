package CasaInteligente;
import CasaInteligente.SmartDevices.SmartBulb;
import CasaInteligente.SmartDevices.SmartCamera;
import CasaInteligente.SmartDevices.SmartDevice;
import ComercializadoresEnergia.Comercializador;
import ComercializadoresEnergia.Fatura;

import java.io.FileWriter;
import java.io.IOException;
import java.io.Serializable;
import java.time.LocalDate;
import java.util.*;

import static java.util.stream.Collectors.toMap;

/**
 * A CasaInteligente faz a gestao dos SmartDevices que existem e dos
 * espaços (as salas) que existem na casa.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class CasaInteligente implements Serializable {
    private String proprietario;
    private int NIF;
    private String fornecedor;
    private Map<String, SmartDevice> devices; // identificador -> SmartDevice
    private Map<String, List<String>> locations; // Espaço -> Lista codigo dos devices

    private List<Fatura> faturas; // lista de faturas que foram geradas e associadas à casa

    /**
     * Construtor por omissao de CasaInteligente.
     */
    public CasaInteligente() {
        this.proprietario = "";
        this.NIF = 0;
        this.fornecedor = "";
        this.devices = new HashMap<>();
        this.locations = new HashMap<>();
        this.faturas = new ArrayList<>();
    }

    /**
     * Construtor parametrizado de CasaInteligente.
     * @param proprietario Nome do proprietario
     * @param NIF Numero de identificaçao fiscal do proprietario.
     * @param fornecedor Fornecedor.
     */
    public CasaInteligente(String proprietario, int NIF, String fornecedor){
        this.proprietario = proprietario;
        this.NIF = NIF;
        this.fornecedor = fornecedor;
        this.devices = new HashMap<>();
        this.locations = new HashMap<>();
        this.faturas = new ArrayList<>();
    }


    /**
     * Construtor parametrizado de CasaInteligente.
     * @param devices Dispositivos existentes na casa.
     * @param locations Divisoes da CasaInteligente.
     */
    public CasaInteligente(String proprietario, int NIF, String fornecedor, Map<String, SmartDevice> devices, Map<String, List<String>> locations){
        this(proprietario, NIF, fornecedor);
        this.devices = devices.entrySet()
                              .stream()
                              .collect(toMap(e->e.getKey(), e->e.getValue().clone()));

        this.locations = locations.entrySet()
                                  .stream()
                                  .collect(toMap(e-> e.getKey(), e->e.getValue()));
        this.faturas = new ArrayList<>();
    }

    /**
     * Construtor de copia de CasaInteligente.
     * @param c CasaInteligente que e copiada.
     */
    public CasaInteligente(CasaInteligente c){
        this(c.proprietario, c.NIF, c.fornecedor, c.devices, c.locations);
    }

    /**
     * Metodo que verifica a igualdade entre a CasaInteligente e um outro objeto.
     * @param o Objeto que e compara com a CasaInteligente.
     * @return Booleano que indica o resultado da comparaçao.
     */
    public boolean equals(Object o){
        if (o ==this)
            return true;

        if(o == null || o.getClass() != this.getClass())
            return false;

        CasaInteligente c = (CasaInteligente) o;

        return(
            this.proprietario.equals(c.proprietario)  &&
            this.NIF == c.NIF                         &&
            this.getFornecedor().equals(c.fornecedor) &&
            this.devices.equals(c.devices)            &&
            this.locations.equals(c.locations)        &&
            this.faturas.equals(c.faturas)
        );
    }

    /**
     * Metodo que devolve uma copia da CasaInteligente recetora da mensagem.
     * @return Copia da CasaInteligente.
     */
    public CasaInteligente clone(){
        return new CasaInteligente(this);
    }

    /**
     * Metodo que produz uma string na qual esta representada a CasaInteligente.
     * @return String que representa a CasaInteligente.
     */
    public String toString(){
        StringBuilder sb = new StringBuilder();

        sb.append("\n------------- Casa Inteligente -------------\n");
        sb.append("Proprietario: ").append(this.proprietario).append("\n");
        sb.append("NIF: ").append(this.NIF).append("\n");
        sb.append("Fornecedor: ").append(this.getFornecedor()).append("\n");

        sb.append("------------- Devices -------------\n");

        for(String id: this.devices.keySet()){
            String estado = "";
            if(this.devices.get(id).getOn()){
                estado = "On";
            } else {
                estado = "Off";
            }
            if(this.devices.get(id) instanceof SmartBulb){
                sb.append("     Smart Bulb ID:").append(id).append(" Estado: ").append(estado).append("\n");
            } else if(this.devices.get(id) instanceof SmartCamera){
                sb.append("     Smart Camera ID:").append(id).append(" Estado: ").append(estado).append("\n");
            } else {
                sb.append("     Smart Speaker ID: ").append(id).append(" Estado: ").append(estado).append("\n");
            }

            // CASO NAO QUEIRA MOSTRAR O CONTEÚDO DO DEVICE METO ISTO EM COMENTARIO
            //sb.append(this.devices.get(id).toString());
        }

        sb.append("------------- Locations -------------\n");
        for(String division: this.locations.keySet()){
            sb.append("Divisao: ").append(division);
            sb.append("\nIds dos dispositivos: ");
            for(String id: this.locations.get(division)){
                sb.append(id).append(" ");
            }
            sb.append("\n");
        }

        return sb.toString();
    }

    /**
     * Metodo que escreve a CasaInteligente num ficheiro de texto.
     * @param writer
     * @throws IOException
     */
    public void writeInFile(FileWriter writer) throws IOException {
        String line = "Casa:" + this.getProprietario() + "," + this.getNIF() + "," + this.getFornecedor() + "\n";
        writer.write(line);
        writer.flush();

        for(String loc: this.locations.keySet()){
            String line_aux = "Divisao:" + loc + "\n";
            writer.write(line_aux);
            writer.flush();
            for(String idDevice: this.locations.get(loc)){
                this.devices.get(idDevice).writeInFile(writer);
            }
        }
    }

    /**
     * Metodo que adiciona uma nova divisao a CasaInteligente.
     * @param s Nova divisao da CasaInteligente.
     */
    public void addRoom(String s) {
        List<String> roomDevices = new ArrayList<>();
        this.locations.put(s, roomDevices);
    }

    /**
     * Metodo que verifica se uma determinada divisao existe na CasaInteligente.
     * @param s Divisao que se pretende saber se existe na CasaInteligente.
     * @return Booleano que indica se a Divisao existe na CasaInteligente.
     */
    public boolean hasRoom(String s) {
        return this.locations.containsKey(s);
    }

    /**
     * Metodo que verifica se um determinado SmartDevice existe numa determinada divisao da CasaInteligente.
     * @param s1 Divisao da CasaInteligente.
     * @param s2 Codigo de identificaçao do SmartDevice.
     * @return Booleano que indica se o SmartDevice existe na divisao da CasaInteligente.
     */
    public boolean roomHasDevice(String s1, String s2) {
        return this.locations.get(s1).contains(s2);
    }

    /**
     * Metodo que verifica se um determinado SmartDevice existe na CasaInteligente.
     * @param id Codigo de identificaçao do SmartDevice.
     * @return Booleano que indica se o SmartDevice existe na Casa.
     */
    public boolean existsDevice(String id) {
        return this.devices.containsKey(id);
    }

    /**
     * Metodo que adiciona um SmartDevice a uma determinada divisao da CasaInteligente.
     * @param s SmartDevice que e adicionado.
     * @param location Divisao da casa a qual e adicionado o SmartDevice.
     */
    public void addDevice(SmartDevice s, String location) {
        this.devices.put(s.getID(), s);

        if (hasRoom(location)) {
            this.locations.get(location).add(s.getID());
        } else {
            List<String> ids = new ArrayList<>();
            ids.add(s.getID());
            this.addLocation(location, ids);
        }
    }

    /**
     * Metodo que remove um device da casa
     * @param id ID do SmartDevice.
     */
    public void removeDevice(String id){
        this.devices.remove(id);
        for(String s : this.locations.keySet()){
            if(this.locations.get(s).contains(id)){
                for(int i = 0; i<this.locations.get(s).size(); i+=1){
                    if(this.locations.get(s).get(i).equals(id)){
                        this.locations.get(s).remove(i);
                    }
                }
            }
        }
    }

    /**
     * Metodo que adiciona uma fatura a lista de faturas.
     * @param f Fatura que e adicionada.
     */
    public void addFatura(Fatura f){
        this.faturas.add(f);
    }

    /**
     * Metodo que calula o consumo total dos dispositivos perante uma simulaçao de tempo.
     * @param before Tempo inicial.
     * @param after Tempo final.
     * @param c Comercializador.
     * @return
     */
    public float simula(LocalDate before, LocalDate after, Comercializador c){
        float total = 0;
        double consumoDisp;
        for (String s : this.devices.keySet()) {
            consumoDisp = c.contaConsumoDispositivo(this.devices.get(s), before, after, this.devices.keySet().size());
            total += consumoDisp;
        }

        return total;
    }

    /**
     * Metodo que adiciona uma divisao a casa.
     * @param location Nova divisao da casa.
     * @param ids Lista de dispositivos dessa divisao.
     */
    public void addLocation(String location, List<String> ids){
        this.locations.put(location, ids);
    }

    // gets e sets
    /**
     * Metodo que devolve o nome do proprietario
     * @return Nome do proprietario da casa
     */
    public String getProprietario() {
        return this.proprietario;
    }

    /**
     * Metodo que devolve o NIF do proprietario da casa
     * @return NIF do proprietario da casa
     */
    public int getNIF() {
        return this.NIF;
    }

    /**
     * Metodo que devolve o nome do fornecedor de energia
     * @return Nome do fornecedor.
     */
    public String getFornecedor() {
        return this.fornecedor;
    }

    /**
     * Metodo que devolve um determinado SmartDevice atraves de um codigo de identificaçao.
     * @param s Codigo de identificaçao do SmartDevice.
     * @return SmartDevice.
     */
    public SmartDevice getDevice(String s) {
        return this.devices.get(s);
    }

    /**
     * Metodo que devolve a estrutura como todos os devices da casa
     * @return HashMap com os devices da casa
     */
    public Map<String, SmartDevice> getDevices() {
        Map<String, SmartDevice> new_devices = new HashMap<>();
        new_devices = this.devices.entrySet()
                                  .stream()
                                  .collect(toMap(e->e.getKey(), e->e.getValue()));


        return new_devices;
    }

    /**
     * Metodo que devolve o Map com as divisoes da casa associadas a lista de ID's de devices presentes nas respetivas divisoes.
     * @return Map com as divisoes da casa.
     */
    // dúvidas aqui ao adicionar os values
    public Map<String, List<String>> getLocations() {
        Map<String, List<String>> new_locations = new HashMap<>();
        new_locations = this.locations.entrySet()
                                      .stream()
                                      .collect(toMap(e->e.getKey(),  e->e.getValue()));


        return new_locations;
    }

    public List<Fatura> getFaturas() {

        return new ArrayList<>(this.faturas);
    }

    /**
     * Metodo que coloca na variavel proprietario o nome passado como parametro
     * @param proprietario String passada como parametro que vai ser colocada na variavel proprietario
     */
    public void setProprietario(String proprietario) {
        this.proprietario = proprietario;
    }

    /**
     * Metodo que coloca na variavel NIF o double passado como parametro
     * @param NIF Double passado como parametro que vai ser colocado na variavel NIF
     */
    public void setNIF(int NIF) {
        this.NIF = NIF;
    }

    /**
     * Metodo que coloca na variavel fornecedor o valor passado como parametro
     * @param fornecedor Nome do fornecedor
     */
    public void setFornecedor(String fornecedor) {
        this.fornecedor = fornecedor;
    }

    /**
     * Metodo que altera o Map com os ID's associados aos respetivos dispositivos.
     * @param devices Map com os dispositivos.
     */
    // discutir com o grupo estes dois métodos
    public void setDevices(Map<String, SmartDevice> devices) {
        this.devices = devices.entrySet()
                              .stream()
                              .collect(toMap(e->e.getKey(), e->e.getValue().clone()));
    }

    /**
     * Metodo que altera o Map com as divisoes da casa associadas a lista de dispositivos presentes nas respetivas divisoes.
     * @param locations Map com as divisoes da casa.
     */
    public void setLocations(Map<String, List<String>> locations) {
        this.locations = locations.entrySet()
                                  .stream()
                                  .collect(toMap(e-> e.getKey(), e->e.getValue()));
    }

    /**
     * Metodo que liga um SmartDevice atraves do seu codigo de identificaçao.
     * @param devCode Codigo de identificaçao do SmartDevice.
     */
    public void setDeviceOn(String devCode) {
        this.devices.get(devCode).turnOn();
    }

    /**
     * Metodo que desliga um SmartDevice atraves do seu codigo de identificaçao.
     * @param devCode Codigo de indentificaçao do SmartDevice.
     */
    public void setDeviceOff(String devCode){
        this.devices.get(devCode).turnOff();
    }

    /**
     * Metodo que atribui um estado a um determinado SmartDevice atraves do codigo de identificaçao.
     * @param s Codigo de identificaçao do SmartDevice.
     * @param b Estado atribuido ao SmartDevice.
     */
    public void setOn(String s, boolean b) {
        this.getDevice(s).setOn(b);
    }

    /**
     * Metodo que atribui um determinado estado a todos os SmartDevices da CasaInteligente.
     * @param b Estado atribuido a todos os SmartDevices.
     */
    public void setAllOn(boolean b) {
        this.devices.values().forEach(s -> s.setOn(b));
    }

    /**
     * Metodo que liga todos os SmartDevices de uma determinada divisao da CasaInteligente.
     * @param location Divisao da CasaInteligente.
     */
    public void turnOnDevicesFromLocation(String location){
        List<String> temp = this.locations.get(location);
        for(String code: temp){
            this.devices.get(code).turnOn();
        }
    }

    /**
     * Metodo que desliga todos os SmartDevices de uma determinada divisao da CasaInteligente.
     * @param location Divisao da CasaInteligente.
     */
    public void turnOffDevicesFromLocation(String location){
        List<String> temp = this.locations.get(location);
        for(String code: temp){
            this.devices.get(code).turnOff();
        }
    }

}
