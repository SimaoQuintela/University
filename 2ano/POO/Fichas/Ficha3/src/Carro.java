import java.lang.StringBuilder;
// classe duvidosa
public class Carro {
    private boolean ligado;
    private String marca;
    private String modelo;
    private int anoConstrucao;
    private int consumoKm;
    private int kmRealizados;
    private int mediaConsumo;
    private int kmsUltimoPercurso;
    private int mediaConsumoUltPer;
    private int capReg;

    public Carro(){
        this.setLigado(false);
        this.setMarca("");
        this.setModelo("");
        this.setAnoConstrucao(0);
        this.setConsumoKm(0);
        this.setKmRealizados(0);
        this.setMediaConsumo(0);
        this.setKmsUltimoPercurso(0);
        this.setMediaConsumoUltPer(0);
        this.setCapReg(0);
    }

    public Carro(boolean ligado, String marca, String modelo, int anoConstr, int consumoKm, int capReg){
        this.setLigado(ligado);
        this.setMarca(marca);
        this.setModelo(modelo);
        this.setAnoConstrucao(anoConstr);
        this.setConsumoKm(consumoKm);
        this.setKmRealizados(0);
        this.setMediaConsumo(0);
        this.setKmsUltimoPercurso(0);
        this.setMediaConsumoUltPer(0);
        this.setCapReg(capReg);
    }

    public Carro(Carro umCarro){
        this(umCarro.getLigado(), umCarro.getMarca(), umCarro.getModelo(), umCarro.getAnoConstrucao(), umCarro.getConsumoKm(), umCarro.getCapReg());
    }

    public boolean equals(Object umCarro){
        if(umCarro == this)
            return true;

        if((umCarro == null) || umCarro.getClass() != this.getClass())
            return false;

        Carro c = (Carro)umCarro;

        return(
                this.getLigado() == c.getLigado() &&
                this.getMarca().equals(c.getMarca()) &&
                this.getModelo().equals(c.getModelo()) &&
                this.getAnoConstrucao() == c.getAnoConstrucao() &&
                this.getConsumoKm() == c.getConsumoKm() &&
                this.getKmRealizados() == c.getKmRealizados() &&
                this.getMediaConsumo() == c.getMediaConsumo() &&
                this.getKmsUltimoPercurso() == c.getKmsUltimoPercurso() &&
                this.getMediaConsumoUltPer() == c.getMediaConsumoUltPer() &&
                this.getCapReg() == c.getCapReg()
        );
    }

    public Carro clone(){
        return new Carro(this);
    }

    public String toString(){
        StringBuilder sb = new StringBuilder();
        sb.append("Ligado: ")
        .append(this.getLigado() + "\n")
        .append("Marca: ")
        .append(this.getMarca() + "\n")
        .append("Modelo: ")
        .append(this.getModelo() + "\n")
        .append("Ano Construção: ")
        .append(this.getAnoConstrucao() + "\n")
        .append("Consumo p/km: ")
        .append(this.getConsumoKm() + "\n")
        .append("Kms realizados: ")
        .append(this.getKmRealizados() +"\n")
        .append("Média Consumo: ")
        .append(this.getMediaConsumo() + "\n")
        .append("Kms último percurso: ")
        .append(this.getKmsUltimoPercurso() +"\n")
        .append("Média consumo último percurso")
        .append(this.getMediaConsumoUltPer() + "\n")
        .append("Capacidade de regeneração: ")
        .append(this.getCapReg() + "\n");

        return sb.toString();
    }

    // 6. b)
    public void ligaCarro(){
        this.setLigado(true);
        this.resetUltimaViagem();
    }

    // 6. c)
    public void desligaCarro(){
        this.setLigado(false);
        this.setKmsUltimoPercurso(this.getKmRealizados() - this.getKmsUltimoPercurso());
    }

    // 6. d)
    public void resetUltimaViagem(){
        this.setKmsUltimoPercurso(0);
        this.setMediaConsumoUltPer(0);
    }

    // 6. e)
    public void avancaCarro(double metros, double velocidade){
        // dúvidas nisto
    }

    // 6. f)
    public void travaCarro(double metros){
        // dúvidas nisto
    }


    // 6. a)
    // gets
    public boolean getLigado(){
        return this.ligado;
    }

    public String getMarca() {
        return this.marca;
    }

    public String getModelo() {
        return this.modelo;
    }

    public int getAnoConstrucao() {
        return this.anoConstrucao;
    }

    public int getConsumoKm() {
        return this.consumoKm;
    }

    public int getKmRealizados() {
        return this.kmRealizados;
    }

    public int getMediaConsumo() {
        return this.mediaConsumo;
    }

    public int getKmsUltimoPercurso() {
        return this.kmsUltimoPercurso;
    }

    public int getMediaConsumoUltPer() {
        return this.mediaConsumoUltPer;
    }

    public int getCapReg() {
        return this.capReg;
    }

    //sets
    public void setLigado(boolean ligado) {
        this.ligado = ligado;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public void setModelo(String modelo) {
        this.modelo = modelo;
    }

    public void setAnoConstrucao(int anoConstrucao) {
        this.anoConstrucao = anoConstrucao;
    }

    public void setConsumoKm(int consumoKm) {
        this.consumoKm = consumoKm;
    }

    public void setKmRealizados(int kmRealizados) {
        this.kmRealizados = kmRealizados;
    }

    public void setMediaConsumo(int mediaConsumo) {
        this.mediaConsumo = mediaConsumo;
    }

    public void setKmsUltimoPercurso(int kmsUltimoPercurso) {
        this.kmsUltimoPercurso = kmsUltimoPercurso;
    }

    public void setMediaConsumoUltPer(int mediaConsumoUltPer) {
        this.mediaConsumoUltPer = mediaConsumoUltPer;
    }

    public void setCapReg(int capReg) {
        this.capReg = capReg;
    }
}
