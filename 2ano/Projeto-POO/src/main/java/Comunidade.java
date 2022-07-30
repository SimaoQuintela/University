import CasaInteligente.CasaInteligente;
import ComercializadoresEnergia.Comercializador;

import java.io.Serializable;
import java.util.HashMap;
import java.util.Map;
import static java.util.stream.Collectors.toMap;


/**
 * A Comunidade faz a gestao de um determinado grupo de CasasInteligentes.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class Comunidade implements Serializable {
    private String nomeDaComunidade;
    private Map<String, CasaInteligente> casas;
    private Map<String, Comercializador> mercado;

    /**
     * Construtor que inicializa a classe Comunidade
     */
    public Comunidade(){
        this.nomeDaComunidade = "Jackson";
        this.casas = new HashMap<>();
        this.mercado = new HashMap<>();
    }

    /**
     * Construtor que inicializa a classe Comunidade
     * @param nomeDaComunidade Nome da comunidade
     */
    public Comunidade(String nomeDaComunidade){
        this.nomeDaComunidade = nomeDaComunidade;
        this.casas = new HashMap<>();
        this.mercado = new HashMap<>();
    }

    /**
     * Construtor que inicializa a classe Comunidade
     * @param nomeDaComunidade Nome da Comunidade
     * @param casas Estrutura que mapeia todas as casas da comunidade em que a Key e a morada e o Value e a Casa
     * @param mercado Estrutura que mapeia todos os comercializadores de energia em que a Key e o nome da companhia e o Value e a Companhia
     */
    public Comunidade(String nomeDaComunidade, Map<String, CasaInteligente> casas, Map<String, Comercializador> mercado){
        this.nomeDaComunidade = nomeDaComunidade;
        this.casas = casas.entrySet()
                          .stream()
                          .collect(toMap(e->e.getKey(), e->e.getValue().clone()));
        this.mercado = mercado.entrySet()
                              .stream()
                              .collect(toMap(e->e.getKey(), e->e.getValue().clone()));

    }

    /**
     * Construtor que inicializa a classe Comunidade
     * @param c Objeto Comunidade
     */
    public Comunidade(Comunidade c){
        this(c.getNomeDaComunidade(), c.getCasas(), c.getMercado());
    }

    /**
     * Metodo equals que verifica se o objeto passado como parametro e igual ao objeto em questão
     * @param o Objeto passado como parametro
     * @return true se for igual false se for diferente
     */
    public boolean equals(Object o){
        if (o ==this)
            return true;

        if(o == null || o.getClass() != this.getClass())
            return false;

        Comunidade c = (Comunidade) o;

        return(this.nomeDaComunidade.equals(c.nomeDaComunidade) &&
               this.casas.equals(c.getCasas())                       &&
               this.mercado.equals(c.getMercado())
        );
    }

    /**
     * Metodo que cria um clone do objeto atual
     * @return copia do objeto atual
     */
    public Comunidade clone(){
        return new Comunidade(this);
    }

    /**
     * Metodo que devolve uma String com informaçao acerca da classe
     * @return Devolve uma String com informaçao acerca da classe
     */
    public String toString(){
        StringBuilder sb = new StringBuilder();

        sb.append("Nome da comunidade: ").append(this.getNomeDaComunidade());
        for(CasaInteligente c : this.casas.values()){
            sb.append(c.toString());
            sb.append("\n\n");
        }

        sb.append("\n------------- Comercializador -------------\n");
        for(Comercializador c : this.mercado.values()){
            sb.append(c.toString());
            sb.append("\n");
        }

        return sb.toString();
    }

    /**
     * Devolve a casa correspondente a string passada como parametro
     * @param proprietario Proprietario da casa
     * @return Casa cuja morada corresponde a passada como parametro
     */
    public CasaInteligente getCasa(String proprietario){
        return this.casas.get(proprietario);
    }

    /**
     * Metodo que devolve um Comercializador existente na comunidade mediante o seu nome.
     * @param fornecedor nome do Comercializador.
     * @return Comercializador.
     */
    public Comercializador getFornecedor(String fornecedor){
        return this.mercado.get(fornecedor);
    }

    /**
     * Adiciona uma casa a comunidade
     * @param proprietario Proprietario da casa
     * @param casa Objeto Casa Inteligente que vai ser adicionado a comunidade
     */
    public void addCasa(String proprietario, CasaInteligente casa){
        this.casas.put(proprietario, casa.clone());
    }


    //gets e sets
    /**
     * Metodo que devolve o nome da Comunidade
     * @return Nome da comunidade
     */
    public String getNomeDaComunidade() {
        return this.nomeDaComunidade;
    }

    /**
     * Metodo que devolve uma copia da estrutura das casas
     * @return Devolve uma copia da estrutura das casas
     */
    public Map<String, CasaInteligente> getCasas() {
        Map<String, CasaInteligente> new_casas = new HashMap<>();
        new_casas = this.casas.entrySet()
                              .stream()
                              .collect(toMap(e->e.getKey(), e->e.getValue()));

        return new_casas;
    }

    /**
     * Metodo que devolve uma copia da estrutura dos comercializadores de energia
     * @return Devolve uma copia da estrutura dos comercializadores de energia
     */
    public Map<String, Comercializador> getMercado() {
        Map<String, Comercializador> new_mercado = new HashMap<>();
        new_mercado = this.mercado.entrySet()
                                  .stream()
                                  .collect(toMap(e->e.getKey(), e->e.getValue()));

        return new_mercado;
    }

    /**
     * Metodo que define o nomeDaComunidade
     * @param nomeDaComunidade Nome da Comunidade
     */
    public void setNomeDaComunidade(String nomeDaComunidade) {
        this.nomeDaComunidade = nomeDaComunidade;
    }

    /**
     * Metodo que adiciona uma casa a estrutura das casas
     * @param proprietario Proprietario da casa
     * @param casa Objeto Casa qeu vai ser associado a morada passada como parametro
     */
    public void setCasas(String proprietario, CasaInteligente casa) {
        this.casas.put(proprietario, casa.clone());
    }

    /**
     * Metodo que adiciona uma companhia a estrutura dos comercializadores de energia
     * @param companhia Nome da companhia
     * @param comercializador Objeto comercializador de energia
     */
    public void setMercado(String companhia, Comercializador comercializador){
        this.mercado.put(companhia, comercializador.clone());
    }

}
