import java.lang.StringBuilder;
// 100% testado, tudo ok
public class Futebol {
    private int estado; // 0 = Por iniciar, 1 = A decorrer, 2 = Terminado
    private int golosEquipaVisitante;
    private int golosEquipaVisitada;

    public Futebol(){
        this.setEstado(0);
        this.setGolosEquipaVisitante(0);
        this.setGolosEquipaVisitada(0);
    }

    public Futebol(int estado, int golosEquipaVisitante, int golosEquipaVisitada){
        this.setEstado(estado);
        this.setGolosEquipaVisitante(golosEquipaVisitante);
        this.setGolosEquipaVisitada(golosEquipaVisitada);
    }

    public Futebol(Futebol f){
        this(f.getEstado(), f.getGolosEquipaVisitante(), f.getGolosEquipaVisitada());
    }

    public boolean equals(Object umJogo){
        if(umJogo == this)
            return true;

        if((umJogo == null) || umJogo.getClass() != this.getClass())
            return false;

        Futebol jogo = (Futebol)umJogo;

        return( this.getEstado() == jogo.getEstado() &&
                this.getGolosEquipaVisitante() == jogo.getGolosEquipaVisitante() &&
                this.getGolosEquipaVisitada() == jogo.getGolosEquipaVisitada()
            );
    }

    public String toString(){
        StringBuilder sb = new StringBuilder();

        sb.append("Resultado: ")
        .append(this.getGolosEquipaVisitada())
        .append("x")
        .append(this.getGolosEquipaVisitante());

        return sb.toString();

    }

    public Futebol clone(){
        return new Futebol(this);
    }

    // 5. a)
    public void startGame(){
        this.setEstado(1);
        this.setGolosEquipaVisitante(0);
        this.setGolosEquipaVisitada(0);
    }

    // 5. b)
    public void endGame(){
        this.setEstado(2);
    }

    // 5. c)
    public void goloVisitado(){
        // só posso atribuir um golo à equipa se o jogo tiver a decorrer
        if(this.getEstado() == 1){
            this.setGolosEquipaVisitada(this.getGolosEquipaVisitada() +1);
        }
    }

    // 5. d)
    public void goloVisitante(){
        // só posso atribuir um golo à equipa se o jogo tiver a decorrer
        if(this.getEstado() == 1){
            this.setGolosEquipaVisitante(this.getGolosEquipaVisitante() +1);
        }
    }

    // 5. e)
    public String resultadoActual(){
        StringBuilder resultado = new StringBuilder();
        resultado.append(this.getGolosEquipaVisitada());
        resultado.append("x");
        resultado.append(this.getGolosEquipaVisitante());

        return resultado.toString();
    }



    // gets
    public int getEstado(){
        return this.estado;
    }

    public int getGolosEquipaVisitante(){
        return this.golosEquipaVisitante;
    }

    public int getGolosEquipaVisitada(){
        return this.golosEquipaVisitada;
    }

    // sets
    public void setEstado(int estado){
        this.estado = estado;
    }

    public void setGolosEquipaVisitante(int golosEquipaVisitante){
        this.golosEquipaVisitante = golosEquipaVisitante;
    }

    public void setGolosEquipaVisitada(int golosEquipaVisitada){
        this.golosEquipaVisitada = golosEquipaVisitada;
    }


}
