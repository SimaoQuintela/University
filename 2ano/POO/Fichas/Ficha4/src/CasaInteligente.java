import java.util.*;

public class CasaInteligente {
    private ArrayList<Lampada> lampadas;
    private String nomeDaCasa;


    public CasaInteligente(){
        this.lampadas = new ArrayList<>();
        this.nomeDaCasa = "";
    }

    public CasaInteligente(ArrayList<Lampada> l, String nomeDaCasa){
        this.lampadas = new ArrayList<>(l);
        this.nomeDaCasa = nomeDaCasa;
    }

    public CasaInteligente(CasaInteligente c){
        this(c.lampadas, c.nomeDaCasa);
    }

    public boolean equals(Object o){
        if(this == o)
            return true;

        if(o == null || o.getClass() != this.getClass())
            return false;

        CasaInteligente c = (CasaInteligente) o;
        // se der falso nem entra no ciclo
        boolean same = this.nomeDaCasa.equals(c.nomeDaCasa);

        for(int i=0; i<this.lampadas.size() && same; i+=1){
            if(! (this.lampadas.get(i).equals(c.lampadas.get(i))))
                same = false;
        }

        return same;
    }

    public CasaInteligente clone(){
        return new CasaInteligente(this);
    }

    //3 b. i.
    public void addLampada(Lampada l){
        this.lampadas.add(l);
    }

    //3 b. ii.
    public void ligaLampadaNormal(int index){
        this.lampadas.get(index).lampON();
    }

    //3 b. iii.
    public void ligaLampadaEco(int index){
        this.lampadas.get(index).lampECO();
    }

    //3 b. iv.
    public int qtEmEco(){
        return (int)this.lampadas.stream()
                                 .filter(l -> l.getModo() == Lampada.Modo.ECO)
                                 .count();
    }

    //3 b. v.
    public void removeLampada(int index){
        this.lampadas.remove(index);
    }

    //3 b. vi.
    public void ligaTodasEco(){
        //this.lampadas.stream().map(Lampada::lampECO);
        for(Lampada l: this.lampadas)
            l.setModo(Lampada.Modo.ECO);
    }

    public void ligaTodasMax(){
        for(Lampada l: this.lampadas)
            l.setModo(Lampada.Modo.ON);
    }

    //3 b. vii.
    public double consumoTotal(){
        double r = 0;

        for(Lampada l: this.lampadas)
            r+=l.getConsumoTotal();

        return r;
    }


    //3 b. viii.
    public Lampada maisGastadora() {
        double maxConsumo = 0;
        Lampada r = null;
        for (Lampada l : this.lampadas)
            if (l.getConsumoTotal() > maxConsumo) {
                maxConsumo = l.getConsumoTotal();
                r = l.clone();
            }

        return r;

        // tentar fazer com iterador interno
    }

    //3 b. ix.
    public Set<Lampada> podiumEconomia(){
        Set<Lampada> r = new TreeSet<>();
        ArrayList<Lampada> aux = new ArrayList<>(this.lampadas);
        aux.sort(Comparator.comparing(Lampada::getConsumoTotal));

        r.add(aux.get(0));
        r.add(aux.get(1));
        r.add(aux.get(2));
        return r;
    }

    //3 b. x.
    public void reset(){
        for(Lampada l: this.lampadas)
            l.setPeriodoConsumo(0);
    }

}
