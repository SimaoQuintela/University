package ComercializadoresEnergia;

import CasaInteligente.CasaInteligente;
import CasaInteligente.SmartDevices.*;

import java.io.FileWriter;
import java.io.IOException;
import java.io.Serializable;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import static java.util.stream.Collectors.toMap;

/**
 * O Comercializador fornece serviço energetico as CasasInteligentes que tenham contrato com o mesmo.
 *
 * @author (your name)
 * @version (a version number or a date)
 */

public class Comercializador implements Serializable {
    private String nomeEmpresa;
    private int numeroDispositivos;
    private int valorBase;
    private int imposto;
    private Map<String, List<Fatura>> faturas;  // Proprietário -> Lista de Faturas

    /**
     * Construtor por omissao de Comercializador.
     */
    public Comercializador(){
        this.nomeEmpresa = "";
        this.numeroDispositivos = 0;
        this.valorBase = 0;
        this.imposto = 0;
        this.faturas = new HashMap<>();
    }

    /**
     * Construtor parametrizado de Comercializador.
     * @param nomeEmpresa Nome do Comercializador.
     */
    public Comercializador(String nomeEmpresa){
        this.nomeEmpresa = nomeEmpresa;
        this.numeroDispositivos = 0;
        this.valorBase = 0;
        this.imposto = 0;
        this.faturas = new HashMap<>();
    }

    /**
     * Construtor parametrizado de Comercializador.
     * @param nomeEmpresa Nome do Comercializador.
     * @param numeroDispositivos Número de dispositivos.
     * @param valorBase Valor minimo do custo do serviço.
     * @param imposto Imposto aplicado no calculo do custo final.
     */
    public Comercializador(String nomeEmpresa, int numeroDispositivos, int valorBase, int imposto){
        this.nomeEmpresa = nomeEmpresa;
        this.numeroDispositivos = numeroDispositivos;
        this.valorBase = valorBase;
        this.imposto = imposto;
        this.faturas = new HashMap<>();
    }

    /**
     * Construtor de copia de Comercializador.
     * @param c Comercializador que e copiada.
     */
    public Comercializador(Comercializador c){
        this(c.nomeEmpresa, c.numeroDispositivos, c.valorBase,/* c.consumoDispositivo,*/ c.imposto);
    }

    /**
     * Metodo que verifica a igualdade entre o Comercializador e um outro objeto.
     * @param o Objeto que e comparado com o Comercializador.
     * @return Booleano que indica o resultado da comparação.
     */
    public boolean equals(Object o){
        if (o == this)
            return true;

        if(o == null || o.getClass() != this.getClass())
            return false;

        Comercializador c = (Comercializador) o;

        return(
            this.nomeEmpresa.equals(c.nomeEmpresa)                 &&
            this.getNumeroDispositivos() == (c.numeroDispositivos) &&
            this.getValorBase() == (c.valorBase)                   &&
            this.imposto == (c.imposto)
        );
    }

    /**
     * Metodo que devolve uma copia da Comercializador recetora da mensagem.
     * @return Copia do comercializador.
     */
    public Comercializador clone(){
        return new Comercializador(this);
    }

    /**
     * Metodo que produz uma string na qual esta representado o Comercializador.
     * @return String que representa o comercializador.
     */
    public String toString(){
        StringBuilder sb = new StringBuilder();

        sb.append("Nome do comercializador: ").append(this.getNomeEmpresa()).append("\n");
        sb.append("Numero de Dispositivos: ").append(this.getNumeroDispositivos()).append("\n");
        sb.append("Valor Base: ").append(this.getValorBase()).append("\n");
        sb.append("Imposto: ").append(this.getImposto()).append("\n");

        return sb.toString();
    }

    /**
     * Metodo que calcula o valor total das faturas geradas.
     * @return Valor total das faturas geradas.
     */
    public float calculaFaturacao(){
        float faturacao = 0;
        for(List<Fatura> l: this.faturas.values()){
            for(Fatura f: l){
                faturacao += f.getTotal();
            }
        }

        return faturacao;
    }

    /**
     * Metodo que adiciona uma Fatura a lista de Faturas de um determinado proprietario.
     * @param prop Proprietario da CasaInteligente.
     * @param f Fatura que e adicionada.
     */
    public void adicionaFatura(String prop, Fatura f){
        if(this.faturas.containsKey(prop)) {
            this.faturas.get(prop).add(f);
        } else {
            List<Fatura> listaFaturas = new ArrayList<>();
            listaFaturas.add(f);
            this.faturas.put(prop, listaFaturas);
        }
    }


    /**
     * Metodo que calcula o consumo de um Dispositivo.
     */
    public double contaConsumoDispositivo(SmartDevice s, LocalDate before, LocalDate after, int numDevices){
        double r = 0;
        s.consumo(before, after);
        if(numDevices > this.numeroDispositivos) {
            r = s.getConsumption()/1500 * (1 + ((float)this.imposto)/100) * 0.9;
        } else {
            r = s.getConsumption()/1500 * (1 + ((float)this.imposto)/100) * 0.75;
        }
        r = Math.round(r*100)/100;

        return r;
    }

    /**
     * Metodo que escreve o objeto em ficheiro.
     * @param writer Descritor de escrita.
     * @throws IOException
     */
    public void writeInFile(FileWriter writer) throws IOException{
        String line = "Fornecedor:" + this.getNomeEmpresa() + "," + this.getNumeroDispositivos() + "\n";
        writer.write(line);
        writer.flush();
    }



    /**
     * Metodo que devolve o numero de dispositivos.
     * @return Numero de dispositivos.
     */
    public int getNumeroDispositivos(){
        return this.numeroDispositivos;
    }

    /**
     * Metodo que devolve o valor base.
     * @return Valor base.
     */
    public int getValorBase(){
        return this.valorBase;
    }

    /**
     * Metodo que devolve o nome do comercializador correspondente
     * @return Nome do comercializador
     */
    public String getNomeEmpresa() {
        return this.nomeEmpresa;
    }

    /**
     * Metodo que devolve a taxa de imposto.
     * @return Taxa de imposto.
     */
    public int getImposto(){
        return this.imposto;
    }

    /**
     * Metodo que devolve o Map que contem as Faturas associadas aos respetivos proprietarios de CasasInteligentes.
     * @return Map com mapeamento de proprietario de uma CasaInteligente para a sua lista de Faturas.
     */
    public Map<String, List<Fatura>> getFaturas() {
        Map<String, List<Fatura>> new_faturas = new HashMap<>();
        new_faturas = this.faturas.entrySet()
                                  .stream()
                                  .collect(toMap(e->e.getKey(), e->e.getValue()));

        return new_faturas;
    }

    /**
     * Metodo que devolve a lista de Faturas de um determinado proprietario de uma CasaInteligente.
     * @param prop Proprietario da CasaInteligente.
     * @return Lista de Faturas de uma CasaInteligente.
     */
    public List<Fatura> getListaFaturas(String prop){
        return this.faturas.get(prop);
    }

    /**
     * Coloca na variavel de instancia nomeEmpresa a string passada como parametro
     * @param nomeEmpresa Nome do comercializador
     */
    public void setNomeEmpresa(String nomeEmpresa) {
        this.nomeEmpresa = nomeEmpresa;
    }

    /**
     * Metodo que altera o numero de dispositivos.
     * @param num Numero de dispositivos.
     */
    public void setNumeroDispositivos(int num){
        this.numeroDispositivos = num;
    }

    /**
     * Metodo que altera o valor base.
     * @param valor Valor base.
     */
    public void setValorBase(int valor){
        this.valorBase = valor;
    }

    /**
     * Metodo que altera a taxa de imposto.
     * @param imposto Taxa de imposto.
     */
    public void setImposto(int imposto){
        this.imposto = imposto;
    }


}
