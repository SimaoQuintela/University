// tudo ok, 100% testado
public class Triangulo {
    private Ponto p1;
    private Ponto p2;
    private Ponto p3;

    public Triangulo(){
        this.p1 = new Ponto();
        this.p2 = new Ponto();
        this.p3 = new Ponto();
    }

    public Triangulo(Ponto p1, Ponto p2, Ponto p3){
        this.setP1(p1);
        this.setP2(p2);
        this.setP3(p3);
    }

    public Triangulo(Triangulo t){
        this(t.getP1(), t.getP2(), t.getP3());
    }

    public boolean equals(Object t){
        if(t == this)
            return true;

        if((t == null) || t.getClass() != this.getClass())
            return false;

        Triangulo t2 = (Triangulo) t;

        return(
            this.getP1().equals(t2.getP1()) &&
            this.getP2().equals(t2.getP2()) &&
            this.getP3().equals(t2.getP3())
        );
    }

    public String toString(){
        StringBuilder sb = new StringBuilder();
        sb.append(this.getP1().toString() + "\n");
        sb.append(this.getP2().toString() + "\n");
        sb.append(this.getP3().toString() + "\n");

        return sb.toString();
    }

    public Triangulo clone(){
        return new Triangulo(this);
    }

    // 9. b)
    public double calculaAreaTriangulo(){
        double halfPerimetro = this.calculaPerimetroTriangulo()/2;
        double distP1P2 = dist2Pontos(this.getP1(), this.getP2());
        double distP1P3 = dist2Pontos(this.getP1(), this.getP3());
        double distP2P3 = dist2Pontos(this.getP2(), this.getP3());

        // heron's formula: area = sqrt(halfPerimetro*(halfPerimetro -p1)*(halfPerimetro -p2)*(halfPerimetro -p3))
        double area = Math.sqrt(halfPerimetro* (halfPerimetro-distP1P2)* (halfPerimetro-distP1P3)* (halfPerimetro-distP2P3));
        return area;
    }

    // 9. c)
    public double calculaPerimetroTriangulo(){
        double distP1P2 = dist2Pontos(this.getP1(), this.getP2());
        double distP1P3 = dist2Pontos(this.getP1(), this.getP3());
        double distP2P3 = dist2Pontos(this.getP2(), this.getP3());

        double perimetro = distP1P2 + distP1P3 + distP2P3;
        return perimetro ;
    }

    // 9. d)
    public double alturaTriangulo(){
        double maiorY = maiorY(this.getP1(), this.getP2(), this.getP3());
        double menorY = menorY(this.getP1(), this.getP2(), this.getP3());
        return maiorY - menorY;
    }

    // métodos auxiliares
    // distância entre 2 pontos
    public double dist2Pontos(Ponto p1, Ponto p2){
        double xP1 = p1.getX();
        double yP1 = p1.getY();

        double xP2 = p2.getX();
        double yP2 = p2.getY();


        // hip = sqrt(catm^2 + catM^2)
        double hip = Math.sqrt( Math.pow(xP2 - xP1, 2) + Math.pow(yP2 -yP1, 2) );
        return hip;
    }

    public double maiorY(Ponto p1, Ponto p2, Ponto p3){
        return Math.max(Math.max(p1.getY(),p2.getY()), p3.getY());
    }

    public double menorY(Ponto p1, Ponto p2, Ponto p3){
        return Math.min(Math.min(p1.getY(),p2.getY()), p3.getY());
    }

    // 9. a)
    // gets
    public Ponto getP1() {
        return this.p1.clone();
    }

    public Ponto getP2() {
        return this.p2.clone();
    }

    public Ponto getP3() {
        return this.p3.clone();
    }
    // sets
    public void setP1(Ponto p1) {
        this.p1 = p1.clone();
    }

    public void setP2(Ponto p2) {
        this.p2 = p2.clone();
    }

    public void setP3(Ponto p3) {
        this.p3 = p3.clone();
    }
}