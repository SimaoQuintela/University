import java.lang.StringBuilder;
// classe a utiliizar na classe Triângulo
public class Ponto {
    private double x;
    private double y;

    public Ponto(){
        this.setX(0);
        this.setY(0);
    }

    public Ponto(double x, double y){
        this.setX(x);
        this.setY(y);
    }

    public Ponto(Ponto p){
        this(p.getX(), p.getY());
    }

    public boolean equals(Object umPonto){
        if(umPonto == this)
            return true;

        if((umPonto == null)|| umPonto.getClass() != this.getClass())
            return false;

        Ponto p = (Ponto)umPonto;

        return(
            this.getX() == p.getX() &&
            this.getY() == p.getY()
        );
    }

    public Ponto clone(){
        return new Ponto(this);
    }

    public String toString(){
        StringBuilder sb = new StringBuilder();
        sb.append("Coordenada X: ");
        sb.append(this.getX() + "\n");
        sb.append("Coordenada Y: ");
        sb.append(this.getY() + "\n");

        return sb.toString();
    }


    // gets
    public double getX(){
        return this.x;
    }

    public double getY(){
        return this.y;
    }

    // sets
    public void setX(double x){
        this.x = x;
    }

    public void setY(double y) {
        this.y = y;
    }
}
