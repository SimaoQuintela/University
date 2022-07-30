import java.time.LocalDateTime;
import java.util.Arrays;
// falta testar esta classe

public class Encomenda {
    private String nomeCliente;
    private double numFiscal;
    private String morada;
    private double numEnc;
    private LocalDateTime dataEnc;
    private LinhaEncomenda[] linhasEncomenda;

    public Encomenda(){
        this.setNomeCliente("");
        this.setNumFiscal(0);
        this.setMorada("");
        this.setNumEnc(0);
        this.setDataEnc(LocalDateTime.now());
        this.linhasEncomenda = new LinhaEncomenda[0];
    }

    public Encomenda(String nomeCliente, double numFiscal, String morada, double numEnc, LocalDateTime dataEnc){
        this.setNomeCliente(nomeCliente);
        this.setNumFiscal(numFiscal);
        this.setMorada(morada);
        this.setNumEnc(numEnc);
        this.setDataEnc(dataEnc);
        this.linhasEncomenda = new LinhaEncomenda[0];
    }

    public Encomenda(Encomenda enc){
        this(enc.getNomeCliente(), enc.getNumFiscal(), enc.getMorada(), enc.getNumEnc(), enc.getDataEnc());
    }

    public boolean equals(Object enc){
        if(this == enc)
            return true;

        if( (enc == null) || (enc.getClass() != this.getClass()))
            return false;

        Encomenda enc2 = (Encomenda) enc;

        return(
              this.getNomeCliente().equals(enc2.getNomeCliente()) &&
              this.getNumFiscal() == enc2.getNumFiscal()          &&
              this.getMorada().equals(enc2.getMorada())           &&
              this.getNumEnc() == enc2.getNumEnc()                &&
              this.getDataEnc() == enc2.getDataEnc()              &&
              Arrays.equals(this.getLinhasEncomenda(),enc2.getLinhasEncomenda())
            );
    }

    public Encomenda clone(){
        return new Encomenda(this);
    }

    public String toString() {
        StringBuilder sb = new StringBuilder("Encomenda{");
        sb.append("\nnomeCliente='").append(nomeCliente).append('\n');
        sb.append(", numFiscal=").append(numFiscal).append('\n');
        sb.append(", morada='").append(morada).append('\n');
        sb.append(", numEnc=").append(numEnc).append('\n');
        sb.append(", dataEnc=").append(dataEnc).append('\n');
        sb.append(", linhasEncomenda=").append(Arrays.toString(linhasEncomenda)).append('\n');
        sb.append('}').append('\n');

        return sb.toString();
    }
    //8. b)
    public double calculaValorTotal(){
        double total = 0;

        for(LinhaEncomenda l: this.getLinhasEncomenda())
            total += l.calculaValorLinhaEnc();

        return total;
    }

    //8. c)
    public double calculaValorDesconto(){
        double totalDesc = 0;

        for(LinhaEncomenda l : this.getLinhasEncomenda()){
            totalDesc += l.calculaValorDesconto();
        }

        return totalDesc;
    }

    // 8. d)
    public double numeroTotalProdutos(){
        long totalProds = 0;

        for(LinhaEncomenda l: this.getLinhasEncomenda())
            totalProds += l.getQuantidade();

        return totalProds;
    }

    // 8. e)
    public boolean existeProdutoEncomenda(String refProduto){
        boolean found = false;

        for(int i=0; i<this.linhasEncomenda.length && !found; i+= 1)
            if(this.linhasEncomenda[i].getRef().equals(refProduto))
                found = true;

        return found;
    }

    // 8. f)
    public void adicionaLinha(LinhaEncomenda linha){
        int n = this.linhasEncomenda.length;
        LinhaEncomenda[] encomenda = this.getLinhasEncomenda();
        LinhaEncomenda[] novo = new LinhaEncomenda[n+1];
        System.arraycopy(encomenda, 0, novo, 0, n);
        novo[n] = linha;
        this.setLinhasEncomenda(novo);
    }

    // 8. g)
    public void removeProduto(String codProd){
        // não vamos remover nada se não houver nada a remover
        if(this.linhasEncomenda.length > 0) {
            LinhaEncomenda[] enc = this.getLinhasEncomenda();
            LinhaEncomenda[] novo = new LinhaEncomenda[enc.length - 1];
            boolean found = false;

            int index = -1;
            for (int i = 0; i < enc.length && !found; i += 1) {
                if (enc[i].getRef().equals(codProd))
                    found = true;
                index = i;

            }

            System.arraycopy(enc, 0, novo, 0, index);
            System.arraycopy(enc, index + 1, novo, index, enc.length - index - 1);
            this.setLinhasEncomenda(novo);
        }
    }


    //8. a) métodos de acesso e alteração de variáveis de instância
    public String getNomeCliente() {
        return this.nomeCliente;
    }

    public double getNumFiscal() {
        return this.numFiscal;
    }

    public String getMorada() {
        return this.morada;
    }

    public double getNumEnc() {
        return this.numEnc;
    }

    public LocalDateTime getDataEnc() {
        return this.dataEnc;
    }

    public LinhaEncomenda[] getLinhasEncomenda() {
        LinhaEncomenda[] r = new LinhaEncomenda[this.linhasEncomenda.length];
        System.arraycopy(this.linhasEncomenda, 0, r, 0, this.linhasEncomenda.length);
        return r;
    }

    public void setNomeCliente(String nomeCliente) {
        this.nomeCliente = nomeCliente;
    }

    public void setNumFiscal(double numFiscal) {
        this.numFiscal = numFiscal;
    }

    public void setMorada(String morada) {
        this.morada = morada;
    }

    public void setNumEnc(double numEnc) {
        this.numEnc = numEnc;
    }

    public void setDataEnc(LocalDateTime dataEnc) {
        this.dataEnc = dataEnc;
    }

    public void setLinhasEncomenda(LinhaEncomenda[] linha) {
        this.linhasEncomenda = new LinhaEncomenda[linha.length];
        System.arraycopy(linha, 0, this.linhasEncomenda, 0, linha.length);
    }
}
