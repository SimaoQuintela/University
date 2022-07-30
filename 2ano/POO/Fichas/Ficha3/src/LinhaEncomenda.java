import java.lang.StringBuilder;

public class LinhaEncomenda {
    private String ref;
    private String descricao;
    private double precoAntes;
    private long quantidade;
    private double imposto;
    private double descontoComercial;

    public LinhaEncomenda(){
        this.setRef("");
        this.setDescricao("");
        this.setPrecoAntes(0);
        this.setQuantidade(0);
        this.setImposto(0.23);
        this.setDescontoComercial(0);
    }

    public LinhaEncomenda(String ref, String descricao, double preco, long quantidade, double imposto, double descontoComercial){
        this.setRef(ref);
        this.setDescricao(descricao);
        this.setPrecoAntes(preco);
        this.setQuantidade(quantidade);
        this.setImposto(imposto);
        this.setDescontoComercial(descontoComercial);
    }

    public LinhaEncomenda(LinhaEncomenda linEnc){
        this(linEnc.getRef(), linEnc.getDescricao(), linEnc.getPrecoAntes(), linEnc.getQuantidade(), linEnc.getImposto(), linEnc.getDescontoComercial());
    }


    public boolean equals(Object linEnc){
        if(this == linEnc)
            return true;
        if((linEnc == null) || linEnc.getClass() != this.getClass())
            return false;

        LinhaEncomenda linEnc2 = (LinhaEncomenda)linEnc;

        return(
            this.getRef().equals(linEnc2.getRef()) &&
            this.getDescricao().equals(linEnc2.getDescricao()) &&
            this.getPrecoAntes() == linEnc2.getPrecoAntes() &&
            this.getQuantidade() == linEnc2.getQuantidade() &&
            this.getImposto() == linEnc2.getImposto() &&
            this.getDescontoComercial() == linEnc2.getDescontoComercial()
        );
    }

    public String toString(){
        StringBuilder sb = new StringBuilder();
        sb.append("Referência: ").append(this.getRef());
        sb.append("\nDescrição: ").append(this.getDescricao());
        sb.append("\nPreço antes de imposto: ").append(this.getPrecoAntes());
        sb.append("\nQuantidade encomendada: ").append(this.getQuantidade());
        sb.append("\nRegime de imposto: ").append(this.getImposto());
        sb.append("\nDesconto comercial: ").append(this.getDescontoComercial());

        return sb.toString();
    }

    public LinhaEncomenda clone(){
        return new LinhaEncomenda(this);
    }

    // 7. b)
    public double calculaValorLinhaEnc(){
        double preco = this.getPrecoAntes() * (1+this.getImposto());
        double desconto = this.getPrecoAntes() * this.getDescontoComercial();
        return(this.getQuantidade() * (preco-desconto));
    }

    // 7. c)
    public double calculaValorDesconto(){
        double precoSemDesconto = this.calculaValorLinhaEnc();
        double precoComDesconto = this.getPrecoAntes() * this.getDescontoComercial();
        return (precoSemDesconto - precoComDesconto);
    }

    // 7. a)
    // gets
    public String getRef() {
        return this.ref;
    }

    public String getDescricao(){
        return this.descricao;
    }

    public double getPrecoAntes() {
        return this.precoAntes;
    }

    public long getQuantidade() {
        return this.quantidade;
    }

    public double getImposto() {
        return this.imposto;
    }

    public double getDescontoComercial() {
        return this.descontoComercial;
    }

    // sets
    public void setRef(String ref) {
        this.ref = ref;
    }

    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }

    public void setPrecoAntes(double precoAntes) {
        this.precoAntes = precoAntes;
    }

    public void setQuantidade(long quantidade) {
        this.quantidade = quantidade;
    }

    public void setImposto(double imposto) {
        this.imposto = imposto;
    }

    public void setDescontoComercial(double descontoComercial) {
        this.descontoComercial = descontoComercial;
    }
}


