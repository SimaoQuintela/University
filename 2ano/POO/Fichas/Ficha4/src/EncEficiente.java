import java.time.LocalDateTime;
import java.util.ArrayList;

public class EncEficiente {
    private String nome;
    private long NIF;
    private String morada;
    private long numEnc;
    private LocalDateTime data;
    private ArrayList<LinhaEncomenda> linhaEnc;

    public EncEficiente(){
        this.nome = "";
        this.NIF = 0;
        this.morada = "";
        this.numEnc = -1;
        this.data = LocalDateTime.now();
        this.linhaEnc = new ArrayList<LinhaEncomenda>();
    }

    public EncEficiente(String nome, long NIF, String morada, long numEnc, LocalDateTime data, ArrayList<LinhaEncomenda> enc){
        this.nome = nome;
        this.NIF = NIF;
        this.morada = morada;
        this.numEnc = numEnc;
        this.data = data;
        this.linhaEnc = new ArrayList<LinhaEncomenda>(enc);
    }

    public EncEficiente(EncEficiente e){
        this(e.nome, e.NIF, e.morada, e.numEnc, e.data, e.linhaEnc);
    }

    public boolean equals(Object o){
        if(this == o)
            return true;

        if((o == null) || (this.getClass() != o.getClass()))
            return false;

        EncEficiente enc = (EncEficiente) o;

        return(
              this.nome.equals(enc.nome) && this.NIF == enc.NIF           &&
              this.morada.equals(enc.morada) && this.numEnc == enc.numEnc &&
              this.data.equals(enc.data) && this.linhaEnc.equals(enc.linhaEnc)
            );
    }

    public EncEficiente clone(){
        return new EncEficiente(this);
    }

    public String toString(){
        StringBuilder sb = new StringBuilder();
        sb.append("\nCliente: " + this.nome);
        sb.append("\nNIF: " + this.NIF);
        sb.append("\nMorada: " + this.morada);
        sb.append("\nNúmero de encomenda: " + this.numEnc);
        sb.append("\nData da encomenda: " + this.data);
        sb.append("\nLinhas de encomenda: " + this.linhaEnc.toString());

        return sb.toString();
    }

    //2 b. ii.
    public double calculaValorTotal(){
        return this.linhaEnc.stream()
                            .mapToDouble(LinhaEncomenda::calculaValorLinhaEnc)
                            .sum();
    }

    //2 b. iii.
    public double calculaValorDesconto(){
        return this.linhaEnc.stream()
                            .mapToDouble(LinhaEncomenda::getDescontoComercial)
                            .sum();
    }

    //2 b. iv.
    public int numeroTotalProdutos(){
        return this.linhaEnc.stream()
                            .mapToInt(LinhaEncomenda::getQuantidade)
                            .sum();
    }

    //2 b. v.
    public boolean existeProdutoEncomenda(String refProd){
        return this.linhaEnc.stream()
                            .anyMatch(l -> l.getRef().equals(refProd));
    }

    //2 b. vi.
    public void adicionaLinha(LinhaEncomenda linha){
        this.linhaEnc.add(linha.clone());
    }

    //2 b vii.
    public void removeProd(String codProd){
        this.linhaEnc.removeIf(l -> l.getRef().equals(codProd));
    }



    // gets e sets
    public String getNome() {
        return this.nome;
    }

    public long getNIF() {
        return this.NIF;
    }

    public String getMorada() {
        return this.morada;
    }

    public long getNumEnc() {
        return this.numEnc;
    }

    public LocalDateTime getData() {
        return this.data;
    }

    public ArrayList<LinhaEncomenda> getLinhaEnc() {
        ArrayList<LinhaEncomenda> novo = new ArrayList<LinhaEncomenda>();
        for(LinhaEncomenda l: this.linhaEnc){
            novo.add(l.clone());
        }
        return novo;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setNIF(long NIF) {
        this.NIF = NIF;
    }

    public void setMorada(String morada) {
        this.morada = morada;
    }

    public void setNumEnc(long numEnc) {
        this.numEnc = numEnc;
    }

    public void setData(LocalDateTime data) {
        this.data = data;
    }

    public void setLinhaEnc(ArrayList<LinhaEncomenda> linhaEnc) {
        this.linhaEnc = new ArrayList<>();
        for(LinhaEncomenda l: linhaEnc){
            this.linhaEnc.add(l.clone());
        }
    }

}

