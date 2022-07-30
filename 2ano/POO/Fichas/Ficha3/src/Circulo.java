import java.lang.Math;
import java.lang.StringBuilder;

// 100% testado, tudo ok
public class Circulo {
    private double x;
    private double y;
    private double raio;

    public Circulo(){
        this.setX(0);
        this.setY(0);
        this.setRaio(0);
    }

    public Circulo(double x, double y, double raio){
        this.setX(x);
        this.setY(y);
        this.setRaio(raio);
    }


    public Circulo(Circulo c){
        this(c.getX(), c.getY(), c.getRaio());
    }

    public boolean equals(Object circulo){
        if(circulo == this)
            return true;

        if( (circulo == null) || (this.getClass() != circulo.getClass()) )
            return false;

        Circulo circulo2 = (Circulo)circulo;

        return( this.getX() == circulo2.getX() &&
                this.getY() == circulo2.getY() &&
                this.getRaio() == circulo2.getRaio()
            );
    }

    public String toString(){
        StringBuilder sb = new StringBuilder();
        sb.append("Coordenada x: ").append(this.getX()).append("\n");
        sb.append("Coordenada y: ").append(this.getY()).append("\n");
        sb.append("Raio: ").append(this.getRaio()).append("\n");

        return sb.toString();
    }

    public Circulo clone(Circulo circulo){
        return new Circulo(this);
    }

    // 1. a)
    public double getX(){
        return this.x;
    }

    // 1. b)
    public double getY(){
        return this.y;
    }

    // 1. c)
    public double getRaio(){
        return this.raio;
    }

    // 1. d)
    public void setX(double x){
        this.x = x;
    }

    // 1. d)
    public void setY(double y){
        this.y = y;
    }

    // 1. d)
    public void setRaio(double raio){
        this.raio = raio;
    }

    // 1. e)
    public void alteraCentro(double x, double y){
        this.setX(x);
        this.setY(y);
    }

    // 1. f)
    public double calculaArea(){
        return ( (Math.PI) * (Math.pow(this.getRaio(),2) ));
    }

    // 1. g)
    public double calculaPerimetro(){
        return (2*Math.PI*this.getRaio());
    }




}
