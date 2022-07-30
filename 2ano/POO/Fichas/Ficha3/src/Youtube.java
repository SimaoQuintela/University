import java.time.LocalDateTime;
import java.time.temporal.ChronoUnit;
import java.lang.StringBuilder;
import java.util.Arrays;
//100% testado, tudo ok
public class Youtube {
    private String nomeVideo;
    private char[] conteudo;
    private LocalDateTime data;
    private int resolucao;
    private int minutos;
    private int segundos;
    private String[] comentarios;
    private int likes;
    private int dislikes;

    public Youtube(){
        this.setNomeVideo("");
        this.conteudo = new char[0];
        this.setData(LocalDateTime.now());
        this.setResolucao(720);
        this.setMinutos(0);
        this.setSegundos(0);
        this.comentarios = new String[0];
        this.setLikes(0);
        this.setDislikes(0);
    }

    public Youtube(String nomeVideo, char[] conteudo, LocalDateTime data, int resolucao, int minutos, int segundos){
        this.setNomeVideo(nomeVideo);
        this.conteudo = new char[conteudo.length];
        System.arraycopy(conteudo, 0, this.conteudo, 0, conteudo.length);
        this.setData(data);
        this.setResolucao(resolucao);
        this.setMinutos(minutos);
        this.setSegundos(segundos);
        this.comentarios = new String[0];
        this.setLikes(0);
        this.setDislikes(0);

    }

    public Youtube(Youtube v){
        this(v.getNomeVideo(), v.getConteudo(), v.getData(), v.getResolucao(), v.getMinutos(), v.getSegundos());
    }

    public boolean equals(Object umVideo){
        if(this == umVideo)
            return true;

        if((umVideo == null) || (this.getClass() != umVideo.getClass()) )
            return false;

        Youtube v = (Youtube)umVideo;

        return(this.getNomeVideo().equals(v.getNomeVideo()) && Arrays.equals(this.getConteudo(), v.getConteudo()) &&
               this.getData() == v.getData() && this.getResolucao() == v.getResolucao() && this.getMinutos() == v.getMinutos() &&
               this.getSegundos() == v.getSegundos() && Arrays.equals(this.getComentarios(), v.getComentarios()) &&
               this.getLikes() == v.getLikes() && this.getDislikes() == v.getDislikes()
        );
    }

    public String toString(){
        StringBuilder sb = new StringBuilder();

        sb.append("Nome vídeo: ").append(this.getNomeVideo());
        sb.append("\nData: ").append(this.getData());
        sb.append("\nResolução: ").append(this.getResolucao());
        sb.append("\nDuração: ").append(this.getMinutos()).append(":").append(this.getSegundos());
        sb.append("\nLikes: ").append(this.getLikes());
        sb.append("\nDislikes: ").append(this.getDislikes());

        return sb.toString();
    }

    public Youtube clone(){
        return new Youtube(this);
    }

    // 3. b)
    public void insereComentario(String comentario){
        String[] comentarios = this.getComentarios();
        String[] novo = new String[comentarios.length+1];
        System.arraycopy(comentarios, 0, novo, 0, comentarios.length);
        novo[comentarios.length] = comentario;
        this.setComentarios(novo);
    }

    // 3. c)
    public long qtsDiasDepois(){
        LocalDateTime present = LocalDateTime.now();
        LocalDateTime dataLancamento = this.getData();

        return (ChronoUnit.DAYS.between(dataLancamento,present));
    }

    // 3. d)
    public void thumbsUp(){
        this.setLikes(this.getLikes() +1);
    }

    // 3. e)
    public String processa(){
        StringBuilder r = new StringBuilder();
        char[] content = this.getConteudo();
        int i;
        for(i = 0; i<content.length ; i+=1){
            r.append(content[i]);
        }

        return r.toString();
    }


    // 3. a)
    // gets
    public String getNomeVideo(){
        return this.nomeVideo;
    }

    public char[] getConteudo(){
        char[] r = new char[this.conteudo.length];

        System.arraycopy(this.conteudo, 0, r, 0, this.conteudo.length);
        return r;
    }

    public LocalDateTime getData(){
        return this.data;
    }

    public int getResolucao(){
        return this.resolucao;
    }

    public int getMinutos(){
        return this.minutos;
    }

    public int getSegundos(){
        return this.segundos;
    }

    public String[] getComentarios(){
        String[] r = new String[this.comentarios.length];
        System.arraycopy(this.comentarios, 0, r, 0, this.comentarios.length);
        return r;
    }

    public int getLikes(){
        return this.likes;
    }

    public int getDislikes(){
        return this.dislikes;
    }

    // sets
    public void setNomeVideo(String nomeVideo){
        this.nomeVideo = nomeVideo;
    }

    public void setConteudo(char[] conteudo){
        this.conteudo = new char[conteudo.length];
        System.arraycopy(conteudo, 0, this.conteudo, 0, conteudo.length);
    }

    public void setData(LocalDateTime data){
        this.data = data;
    }

    public void setResolucao(int resolucao){
        this.resolucao = resolucao;
    }

    public void setMinutos(int minutos){
        this.minutos = minutos;
    }

    public void setSegundos(int segundos){
        this.segundos = segundos;
    }

    public void setComentarios(String[] comentarios){
        this.comentarios = new String[comentarios.length];
        System.arraycopy(comentarios, 0, this.comentarios, 0, comentarios.length);
    }

    public void setLikes(int likes){
        this.likes = likes;
    }

    public void setDislikes(int dislikes){
        this.dislikes = dislikes;
    }

}

